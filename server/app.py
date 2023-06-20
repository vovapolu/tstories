from flask import Flask, request, Response
from flask_cors import CORS
from promts import promts
import grpc
from openaiproxy import openaiproxy_pb2_grpc as openaiproxy_grpc
from openaiproxy import openaiproxy_pb2 as openaiproxy_msg
from google.protobuf import json_format
import os

auth_token = os.getenv("GPT_TOKEN")

app = Flask(__name__)
CORS(app)

channel = grpc.secure_channel(
    "openai-proxy-grpc.tcsbank.ru", grpc.ssl_channel_credentials()
)
stub = openaiproxy_grpc.OpenAIProxyStub(channel)


@app.route("/story_info/<id>")
def story_info(id: str):
    promt = next(p for p in promts if p["id"] == id)

    return {"from": promt["from"]}


@app.route("/gpt_stream", methods=["POST"])
def gpt_stream():
    jreq = request.get_json()
    promt = next(p for p in promts if p["id"] == jreq["id"])

    grpc_req = openaiproxy_msg.ChatCompletionV1Request()
    json_format.ParseDict(
        {
            "model": "gpt-3.5-turbo",
            "messages": [
                {
                    "role": "user",
                    "content": promt["promt"]
                    .replace("{{name}}", jreq["name"])
                    .replace("{{purchases}}", jreq["purchases"]),
                },
            ],
        },
        grpc_req,
    )
    metadata = [("authorization", f"Bearer {auth_token}")]

    def eventStream():
        for i, resp in enumerate(
            stub.ChatCompletionStreamV1(grpc_req, metadata=metadata)
        ):
            if i > 0:
                yield resp.choices[0].delta.content

    return Response(eventStream(), mimetype="text/event-stream")

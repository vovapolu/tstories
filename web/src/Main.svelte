<script lang="ts">
    import { Icon, ChevronDown, ChevronUp } from "svelte-hero-icons";
    let name = "Вася";
    let purchases = "Пятерочка молоко \nМагнит Хлеб \nBeerBar Пиво";

    let from = undefined;
    let story = "...";
    let curStoryId = undefined;
    let curId = undefined;

    let settingsOpened = false;

    function startStoryLoadingAnimation(storyId: string) {
        let loadingSteps = [".", "..", "..."];
        function nextStep() {
            if (storyId === curStoryId) {
                let idx = loadingSteps.indexOf(story);
                if (idx == -1) {
                    story = loadingSteps[0];
                } else {
                    story = loadingSteps[(idx + 1) % loadingSteps.length];
                }
            }
        }

        return setInterval(nextStep, 300);
    }

    async function fetchStreamGpt() {
        let storyId = Math.random().toString(36);
        curStoryId = storyId;
        let animId = startStoryLoadingAnimation(storyId);

        let gpt_stream_resp = await fetch(`http://127.0.0.1:5000/gpt_stream`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                id: curId,
                name: name,
                purchases: purchases,
            }),
        });

        if (!gpt_stream_resp.body) return;
        const reader = gpt_stream_resp.body
            .pipeThrough(new TextDecoderStream())
            .getReader();

        let idx = 0;
        while (true) {
            var { value, done } = await reader.read();
            if (idx == 0) {
                clearInterval(animId);
            }
            if (done) break;
            if (storyId === curStoryId) {
                if (idx == 0) {
                    story = "";
                }
                story += value;
                idx++;
            } else {
                await reader.cancel();
                break;
            }
        }
    }

    function fetchStoryInfo(id: string) {
        curId = id;
        story = "...";
        fetch(`http://127.0.0.1:5000/story_info/${id}`)
            .then((r) => r.json())
            .then((j) => (from = j["from"]));
    }
</script>

<div class="min-h-screen mx-32 flex flex-col items-start bg-white font-sans">
    <div class="max-w-2xl my-3 mx-auto">
        <span
            class="px-2 text-xl whitespace-nowrap font-semibold text-black bg-yellow-200"
        >
            Тинькоффские истории
        </span>
    </div>

    <div class="w-full">
        {#if from}
            <label for="from" class="block mb-1 text-lg font-medium text-black"
                >История от {from}</label
            >
        {/if}
        <p
            class="block w-full p-2.5 my-2 text-sm text-gray-900 bg-gray-50 border border-gray-300"
        >
            {story}
        </p>
    </div>

    <div class="flex items-center w-full justify-between">
        <div class="self-end flex flex-col items-start">
            <button
                class="px-2 my-2 border-2 border-black bg-yellow-300"
                on:click={fetchStreamGpt}
            >
                Сгенерировать историю
            </button>

            <button
                class="flex items-center px-2 border-2 border-black bg-yellow-300"
                on:click={() => (settingsOpened = !settingsOpened)}
            >
                <p>Настройка истории</p>
                {#if settingsOpened}
                    <Icon class="ml-1" src={ChevronUp} size="14" />
                {:else}
                    <Icon class="ml-1" src={ChevronDown} size="14" />
                {/if}
            </button>
        </div>

        <div class="flex">
            <button
                title="Лавкрафт"
                class="w-40 mx-2 border-2 border-black"
                on:click={() => fetchStoryInfo("lovecraft")}
            >
                <img
                    alt="Лавкрафт"
                    src="http://127.0.0.1:5000/static/lovecraft.png"
                />
            </button>

            <button
                title="Фрейд"
                class="w-40 mx-2 border-2 border-black"
                style="max-width: 10rem"
                on:click={() => fetchStoryInfo("freud")}
            >
                <img
                    alt="Фрейд"
                    class="object-fill"
                    src="http://127.0.0.1:5000/static/freud.jpg"
                />
            </button>
            <button
                title="Довлатов"
                class="w-40 mx-2 border-2 border-black"
                on:click={() => fetchStoryInfo("dovlatov")}
            >
                <img
                    alt="Довлатов"
                    src="http://127.0.0.1:5000/static/dovlatov.png"
                />
            </button>
            <button
                title="Донцова"
                class="w-40 mx-2 border-2 border-black"
                on:click={() => fetchStoryInfo("doncova")}
            >
                <img
                    alt="Донцова"
                    src="http://127.0.0.1:5000/static/doncova.png"
                />
            </button>
        </div>
    </div>

    {#if settingsOpened}
        <div class="flex flex-col w-full border-2 border-black p-2 mt-2">
            <div>
                <label
                    for="name"
                    class="block mb-1 text-sm font-medium text-gray-900"
                    >Имя</label
                >
                <input
                    type="text"
                    class="bg-gray-50 border border-gray-300 text-gray-900 text-sm focus:border-blue-500 block w-full p-2"
                    placeholder="Имя"
                    bind:value={name}
                    required
                />
            </div>
            <div class="mt-2">
                <label
                    for="shop_list"
                    class="block mb-1 text-sm font-medium text-gray-900"
                    >Список покупок</label
                >
                <textarea
                    rows="4"
                    class="block w-full p-2 text-sm text-gray-900 bg-gray-50 border border-gray-300 focus:border-blue-500"
                    placeholder="Список покупок"
                    bind:value={purchases}
                />
            </div>
        </div>
    {/if}
</div>

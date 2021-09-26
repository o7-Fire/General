// noinspection DuplicatedCode
const translate = require('translate-google')
const axios = require('axios');
const headers = {
    "accept": "*/*",
    "authorization": process.env.TOKEN || "OR YOUR TOKEN",
    "content-type": "application/json",
};

function sleep(ms) {
    return new Promise((resolve) => {
        setTimeout(resolve, ms);
    });
}

function updateCustom(text = "libtard") {
    return axios({
        method: "PATCH",
        url: "https://discord.com/api/v9/users/@me/settings",

        headers: headers,
        data: {
            custom_status: {
                text: text
            }
        }
    });
}

function updateStatus(status = "online") {
    return axios({
        url: "https://discord.com/api/v9/users/@me/settings",
        headers: headers,
        data: {
            status: status
        },
        method: "PATCH",
    })
}



async function getItems() {

    const language = []
    for(const id in translate.languages){
        if(id === "auto")continue;
        if((typeof translate.languages[id]) === "function")continue;
        language.push(id);
    }
    return language;
    //console.log(root)
}

async function assad() {
    const items = await getItems();
    const word = "fuck"
    const wordSrc = "en"
    console.log("Found:",items.length,"items")
    while (true) {
        await sleep(5000);
        const target = items[Math.floor(Math.random() * items.length)];
        try {
            const slur = await translate(word, {from: wordSrc, to: target})
            console.log("[",translate.languages[target],"]:", slur)
            await updateCustom(slur);
        } catch (e) {
            console.error(e);
        }
    }
}


//if(1 === 2)
assad().catch(console.error);
//test().catch(console.error);

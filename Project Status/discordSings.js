// noinspection DuplicatedCode

const axios = require('axios');
const HTMLParser = require('node-html-parser');
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
  //customize this to get other lyrics
    return (await axios.get("https://api.lyrics.ovh/v1/Sabaton/Bismarck")).data.lyrics;
    //console.log(root)
}

async function assad() {
    const lyrics = String(await getItems()).split("\n");
    let i = 0;
    console.log("Total:",lyrics.length,"lines of lyrics")
    while (true) {
        await sleep(5000);
        if(i >= lyrics.length)
            i = 0;
        let slur = lyrics[i++];
        try {
            console.log("Text:", slur)
            await updateCustom(slur);
            await updateStatus();
        } catch (e) {
            console.error(e);
        }
    }
}


//if(1 === 2)
assad().catch(console.error);
//test().catch(console.error);

const axios = require('axios');
const HTMLParser = require('node-html-parser');
//or just copy from the inspector
const headers = {
            "accept": "*/*",
            "authorization": "YOUR TOKEN",
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
    const arraaaay = []
    const {
        data
    } = await axios.get('http://www.rsdb.org/full');
    let root = HTMLParser.parse(data);
    root = root.querySelector('#slurs')
    root = root.childNodes[1].childNodes
    let i = 0;
    for (let r of root) {
        if (r.constructor.name === "TextNode") continue
        if (!r.id.startsWith("slur_")) continue
        console.log(r.childNodes[1].text) //0 is false, 1 is first row, 2 is false
        arraaaay.push(r.childNodes[1].text);
        i++;
        //if(i > 2)break;
    }
    return arraaaay;
    //console.log(root)
}

async function assad() {
    const slurs = await getItems();
    if (slurs.length < 10) {
        throw new Error("Not enough slurs")
    }
    while (true) {
        await sleep(5000);
        let slur = slurs[Math.floor(Math.random() * slurs.length)];
        slur = "Fucking " + slur;
        try {
            console.log("Text:", slur)
            await updateCustom(slur);
        } catch (e) {
            console.error(e);
        }
    }
}


//if(1 === 2)
assad().catch(console.error);
//test().catch(console.error);

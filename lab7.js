let token = "1320909136:AAHShEvqcKvHhhwjxoJM3RN0bomn1yXoGYY"

let getMessageButton = document.getElementById("getMessageButton")
let authorHeader = document.getElementById("authorHeader")
let messageHeader = document.getElementById("messageHeader")

let getMessage = () => {
    $.getJSON({
        url: `https://api.telegram.org/bot${token}/getUpdates?limit=1&offset=-1`,
        jsonp: "callback",
        dataType: "json"
    }).done(data => {
        if (data.result.length > 0) {
            let firstName = data.result[0].message.from.first_name
            let lastName = data.result[0].message.from.last_name
            messageHeader.innerText = `Автор: ${firstName} ${lastName}`
            authorHeader.innerText = `Текст: ${data.result[0].message.text}`
        }
    })
}

getMessageButton.onclick = e => {
    getMessage()
}
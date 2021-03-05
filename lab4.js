let accessToken = "e4697c386550a5703318dc3973e5c32173de2a42ce27dbb6385811fd656a1fb31afd50a2b75aca6d3bd0c"

let input = document.getElementById("status-input")
let submitButton = document.getElementById("submit-button")

let changeStatus = status => {
    let changeStatusRequest = `https://api.vk.com/method/status.set?text=${status}&access_token=${accessToken}&v=5.130`
    $.getJSON({
        url: changeStatusRequest,
        jsonp: "callback",
        dataType: "jsonp"
        }).done( res => {
            console.log(res)
        });
}

submitButton.onclick = e => {
    changeStatus(input.value)
} 

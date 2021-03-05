let accessToken = "e4697c386550a5703318dc3973e5c32173de2a42ce27dbb6385811fd656a1fb31afd50a2b75aca6d3bd0c"

let submitButton = document.getElementById("submit-button")
let input = document.getElementById("number-input")

let createPost = async groups => {
    let text = ''

    groups.forEach( el => {
        text += "Название: " + el.name + " " + "Количество: " + el.members_count + " "  
    });

    let createPostRequest = `https://api.vk.com/method/wall.post?owner_id=84105524&message=${text}&access_token=${accessToken}&v=5.130`

    return $.getJSON({
        url: createPostRequest,
        jsonp: "callback",
        dataType: "jsonp"
        }).promise()
}

let getGroups = async () => {
    let count = input.value
    let getGroupsRequest = `https://api.vk.com/method/groups.get?user_id=84105524&count=${count}&extended=1&access_token=${accessToken}&v=5.130&fields=members_count`

    return $.getJSON({
        url: getGroupsRequest,
        jsonp: "callback",
        dataType: "jsonp"
        }).promise()
}

submitButton.onclick = async e => {
    res = await getGroups()
    result = await createPost(res.response.items)
    console.log(result)
}
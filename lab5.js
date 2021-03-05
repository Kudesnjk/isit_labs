let accessToken = "a5a091004eea8ec5561403941ec17342b4e41af5489909a4fc61b172f6fce755eadb65ee585410c36b099"

let submitButton = document.getElementById("submit-button")
let input = document.getElementById("number-input")

let createPost = groups => {
    let text = ''

    groups.forEach( el => {
        text += "Название: " + el.name + " " + "Количество: " + el.members_count + " "  
    });

    let createPostRequest = `https://api.vk.com/method/wall.post?owner_id=84105524&message=${text}&access_token=${accessToken}&v=5.130`

    $.getJSON({
        url: createPostRequest,
        jsonp: "callback",
        dataType: "jsonp"
        }).done( res => {
            console.log(res)
        });
}

let getGroups = () => {
    
    let count = input.value
    let getGroupsRequest = `https://api.vk.com/method/groups.get?user_id=84105524&count=${count}&extended=1&access_token=${accessToken}&v=5.130&fields=members_count`

    $.getJSON({
        url: getGroupsRequest,
        jsonp: "callback",
        dataType: "jsonp"
        }).done( res => {
            console.log(res)
            createPost(res.response.items)
        });
}

submitButton.onclick = e => {
    getGroups()
}
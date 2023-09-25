document.addEventListener("DOMContentLoaded", () => {

document.querySelector("#main").innerHTML = "Здравствуйте"+window.Telegram.WebApp.initDataUnsafe.user.first_name
document.querySelector("#version").innerHTML = "Bot API version: "+window.Telegram.WebApp.version

}) // end of DOMContentLoaded event 
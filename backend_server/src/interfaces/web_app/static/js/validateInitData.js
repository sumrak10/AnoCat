if (window.Telegram.WebApp.initData === "") {
    window.location.replace("/bot/web_app/only_for_telegram_web_app");
} else {
    axios({
        method: 'post',
        url: 'validateInitData',
        data: {
            initData: window.Telegram.WebApp.initData
        }
    }).then(function (response) {
        if (response['data']['message'] != "ok") {
            window.Telegram.WebApp.HapticFeedback.notificationOccurred('error')
            window.Telegram.WebApp.showAlert("Произошла ошибка, попробуйте позже :(", (e) => {
                window.Telegram.WebApp.close()
            })
        }
    }).catch(function (error) {
        window.Telegram.WebApp.HapticFeedback.notificationOccurred('error')
        window.Telegram.WebApp.showAlert("Произошла ошибка, попробуйте позже :(")
        window.Telegram.WebApp.showAlert("Произошла ошибка, попробуйте позже :(", (e) => {
            window.Telegram.WebApp.close()
        })
    })
}
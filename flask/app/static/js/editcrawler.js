// 新增商品
function addTask(event) {
    console.log('Start addTask');
    // 取消瀏覽器重整畫面的行為
    event.preventDefault();
    // 定義Email, 密碼

    const data = {
        website: event.srcElement[1].value,
        name: event.srcElement[2].value,
        description: event.srcElement[3].value,
        link: event.srcElement[4].value,
        url: event.srcElement[5].value
    }
    axios.post('/crawler/add', data, {
            headers: {
                'x-csrf-token': csrf
            }
        })
        .then(response => {
            console.log(response)
            if (response.data.msg == 'ok') {
                $('#addProductModal').modal('hide')
                bootbox.dialog({
                    message: "新增成功",
                    title: "系統訊息",
                    buttons: {
                        OK: {
                            label: "確定",
                            className: "btn-green",
                            callback: function () {
                                // 重整畫面
                                location.reload()
                            }
                        }
                    }
                });
            } else {
                bootbox.dialog({
                    message: response.data.msg,
                    title: "系統訊息",
                    buttons: {
                        OK: {
                            label: "確定",
                            className: "btn-green",
                            callback: function () {
                                console.log(response.data.msg)
                                // 重整畫面
                                location.reload()
                            }
                        }
                    }
                });
            }
        })
}

// 刪除商品
function deleteTask(event, wid) {
    console.log('Start deleteProduct');
    // 取消瀏覽器重整畫面的行為
    event.preventDefault();
    const data = {
        wid: wid
    }

    axios.post('/crawler/delete', data, {
            headers: {
                'x-csrf-token': csrf
            }
        })
        .then(response => {
            console.log(response)
            if (response.data.msg == 'ok') {

                bootbox.dialog({
                    message: "刪除產品成功",
                    title: "系統訊息",
                    buttons: {
                        OK: {
                            label: "確定",
                            className: "btn-green",
                            callback: function () {
                                // 重整畫面
                                location.reload()
                            }
                        }
                    }
                });
            } else {
                bootbox.dialog({
                    message: response.data.msg,
                    title: "系統訊息",
                    buttons: {
                        OK: {
                            label: "確定",
                            className: "btn-green",
                            callback: function () {
                                // 重整畫面
                                location.reload()
                            }
                        }
                    }
                });
            }
        })
        .catch(err => {
            // 顯示錯誤訊息
            console.log(err);
        })
}


// 更新商品
function updataTask(event) {
    console.log('Start updataProduct');
    // 取消瀏覽器重整畫面的行為
    event.preventDefault();
    // 定義Email, 密碼

    const data = {
        website: event.srcElement[1].value,
        name: event.srcElement[2].value,
        description: event.srcElement[3].value,
        link: event.srcElement[4].value,
        website_url: event.srcElement[5].value,
        id: event.srcElement[6].value
    }
    axios.post('/crawler/updata', data, {
            headers: {
                'x-csrf-token': csrf
            }
        })
        .then(response => {
            console.log(response)
            if (response.data.msg == 'ok') {

                $('#updataProductModal').modal('hide')
                bootbox.dialog({
                    message: "更新成功",
                    title: "系統訊息",
                    buttons: {
                        OK: {
                            label: "確定",
                            className: "btn-green",
                            callback: function () {
                                // 重整畫面
                                location.reload()
                            }
                        }
                    }
                });
            } else {
                bootbox.dialog({
                    message: response.data.msg,
                    title: "系統訊息",
                    buttons: {
                        OK: {
                            label: "確定",
                            className: "btn-green",
                            callback: function () {
                                // 重整畫面
                                location.reload()
                            }
                        }
                    }
                });
            }
        }).catch(err => {
            // 顯示錯誤訊息
            console.log(err);
        })

}
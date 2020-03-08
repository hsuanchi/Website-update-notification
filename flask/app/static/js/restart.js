// 重啟爬蟲函數
function restart(event, id) {
    console.log('Start restart');
    // 取消瀏覽器重整畫面的行為
    event.preventDefault();
    const data_json = {
        id: id
    }
    console.log(data_json)
    $.ajax({
        url: '/status/restart',
        type: "POST",
        data: JSON.stringify(data_json),
        headers: {
            'x-csrf-token': csrf
        },
        contentType: 'application/json;charset=UTF-8',
        success: function (data) {
            if (data.msg == 'ok') {
                $('.dialog').hide();
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
                $('.dialog').hide();
                bootbox.dialog({
                    message: data.msg,
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
        },
        beforeSend: function () {
            $('.dialog').show();
        },
        complete: function () {},
    })
}
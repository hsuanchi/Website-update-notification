// 登入函數
function login(event) {
    console.log('Start login');
    // 取消瀏覽器重整畫面的行為
    event.preventDefault();
    // 定義Email, 密碼
    const data = {
        email: document.getElementById('loginEmail').value,
        password: document.getElementById('loginPassword').value
    }
    axios.post('/auth/login', data, {
            headers: {
                'x-csrf-token': csrf
            }
        })
        .then(response => {
            console.log(response)
            if (response.data.msg == 'ok') {
                // 回到首頁
                // location = '/'
                location.reload()
            } else {
                bootbox.dialog({
                    message: "帳號密碼錯誤",
                    title: "系統訊息",
                    buttons: {
                        OK: {
                            label: "確定",
                            className: "btn-green",
                            callback: function () {
                                // 重整畫面
                                // location.reload()
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


// 登出函數
function logout() {
    axios.post('/auth/logout', {}, {
            headers: {
                'x-csrf-token': csrf
            }
        })
        .then(response => {
            console.log(response)
            // 回到登入頁
            // location = '/auth/login'
            location.reload()
        })
        .catch(error => {
            console.log(error)
        })
}



// 註冊函數
function signUp(event) {
    console.log('Start signUp');
    // 取消瀏覽器重整畫面的行為
    event.preventDefault();
    // 取得填寫Email, 密碼
    const data = {
        email: document.getElementById('signUpEmail').value,
        password: document.getElementById('signUpPassword').value
    }
    console.log(data)
    axios.post('/auth/signup', data, {
            headers: {
                'x-csrf-token': csrf
            }
        })
        .then(response => {
            console.log(response)
            if (response.data.msg == '註冊成功') {
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
                                // location.reload()
                            }
                        }
                    }
                });
            }
        })
        .catch(error => {
            console.log(error)
        })
        .catch(err => {
            console.log(err);
            // 顯示錯誤訊息
            Swal.fire({
                title: err.code,
                text: err.message,
                type: 'error'
            });
        })
}
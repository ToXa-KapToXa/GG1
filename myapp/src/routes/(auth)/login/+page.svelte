<script>
    let email = ""
    let password = ""
    export let result = null
    async function auth () {
        console.log(email)
        console.log(password)
		const res = await fetch('http://localhost:1122/api/auth', {
			method: 'POST',
            headers: {
                'Content-Type': 'application/json'
                // like application/json or text/xml
            },
			body: JSON.stringify({
				email,
                password
			})
		})
		
		const json = await res.json()
        console.log(json)
        result = json['response_code']
        console.log(result)
        if (result == 200) {
            window.location.href = '/main';
        }
	}
</script>

<main>
    <!--Form-->
    <div class="wr">
        <div class="wrapper">
            <!-- error message -->
            <!-- <div th:if="${param.error}">
                <div class="alert alert-danger">Неверный email или пароль.</div>
            </div>
     -->
            <!-- logout message -->
            <!-- <div th:if="${param.logout}">
                <div class="alert alert-info">Вы вышли из аккаунта!</div>
            </div> -->
    
            <form href="/login" method="post">
                <h2 class="in">Вход</h2>
                <div class="heading-line" style="margin-bottom: 30px; margin-top: -3px"></div>
    
                <div class="field email">
                    <div class="input-area">
                        <input type="text" id ="username" bind:value={email} name = "username" placeholder="email" autofocus="autofocus">
                        <i class="fa fa-user" id="loginEmail"></i>
                        <i class="error error-icon fas fa-exclamation-circle"></i>
                    </div>
                </div>
    
                <div class="field password">
                    <div class="input-area">
                        <input type="password" bind:value={password} id="password" name = "password" placeholder="Password" autofocus="autofocus">
                        <i class="fa fa-lock" id="loginPassword"></i>
                        <i class="error error-icon fas fa-exclamation-circle"></i>
                    </div>
                </div>
    
                <div>
                    <button type="submit" name="login-submit" id="login-submit" on:click={auth}
                            class="form-control btn btn-primary" style="background: #9e8a78; border-color: #9e8a78;"><a href="/login">Войти</a></button>
                </div>
                <div>
                    <span class="spann">Нет аккаунта? <a style="color: #9e8a78" href="/registration">Зарегистрируйтесь.</a></span>
                </div>
            </form>
        </div>
    </div>
    <!--Form-->
</main>

<style>
.in {
    padding-bottom: 30px; margin-top: 10px; background-color: #FFFFFF;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

.wr {
    /* width: 100%; */
    display: flex;
    align-items: center;
    justify-content: center;
    background: #1E1F29;
    min-height: 100vh;
    background-position: right;
    background-size: cover;
    margin-left: -1%;
    margin-right: -1%;  
}
.wrapper {
    min-width: 380px;
    padding: 20px 30px 20px 30px;
    background: #fff;
    border-radius: 8px;
    text-align: center;
}

.wrapper header {
    font-size: 35px;
    font-weight: 600;
}

.wrapper form {
    margin: 40px 0;
    
}

form .field {
    width: 100%;
    margin-bottom: 20px;
}


form .field .input-area {
    height: 50px;
    width: 100%;
    position: relative;
}

form input {
    width: 100%;
    height: 100%;
    outline: none;
    padding: 0 45px;
    font-size: 18px;
    background: none;
    caret-color: black;
    border-radius: 5px;
    border: 1px solid #bfbfbf;
    border-bottom-width: 2px;
    transition: all 0.2s ease;
}

form .field input:focus,
form .field.valid input {
    border-color: black;
}

form .field.shake input,
form .field.error input {
    border-color: #dc3545;
}

.field .input-area i {
    position: absolute;
    top: 50%;
    font-size: 18px;
    pointer-events: none;
    transform: translateY(-50%);
}

.input-area .icon {
    left: 15px;
    color: #bfbfbf;
    transition: color 0.2s ease;
}

.input-area .error-icon {
    right: 15px;
    color: #dc3545;
}

form input:focus~.icon,
form .field.valid .icon {
    color: black;
}

form .field.shake input:focus~.icon,
form .field.error input:focus~.icon {
    color: #bfbfbf;
}

form input::placeholder {
    color: #bfbfbf;
    font-size: 17px;
}

form .field .error-txt {
    color: #dc3545;
    text-align: left;
    margin-top: 5px;
}

form .field .error {
    display: none;
}

form .field.shake .error,
form .field.error .error {
    display: block;
}

form .pass-txt {
    text-align: left;
    margin-top: -10px;
}


form input[type="submit"] {
    height: 50px;
    margin-top: 30px;
    color: #fff;
    padding: 0;
    border: none;
    background: black;
    cursor: pointer;
    border-bottom: 2px solid black;
    transition: all 0.3s linear;
}

form input[type="submit"]:hover {
    background: grey;
}

.btn {
    background-color: black;
    color: white;
}
</style>
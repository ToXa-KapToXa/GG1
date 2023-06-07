<script>
    import { onMount } from "svelte";

	const urlAuth = "https://gg1-back.onrender.com/api/check/22";
	export let code_response;
    let user_session = "22";
    export let user_id;

    onMount(async function () {
        const isAuth = await fetch(urlAuth);
        const dataAuth = await isAuth.json();
        console.log(dataAuth);
        code_response = dataAuth["response_code"];
        user_id = dataAuth["data"];
    });

  async function logout () {
        const res = await fetch('https://gg1-back.onrender.com/api/logout', {
        
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                user_session
            })
        })
    
        const json = await res.json()
        console.log(json)
        let result = json['response_code']
        console.log(result)
        if (result == 200) {
            window.location.href = '/main';
        }
	}

    export async function add_bucket (product_id) {
        const res = await fetch('https://gg1-back.onrender.com/api/add_bucket', {
        
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                user_id,
                product_id
            })
        })
    
        const json = await res.json()
        console.log(json)
        // result = json['response_code']
        // console.log(result)
        // if (result == 200) {
        //     window.location.href = '/main';
        // }
	}
</script>

<main>
    <header>
        <div id="header">
            <!-- БЛОК -->
            <div class="container">
                <!-- РЯД -->
                <div class="row">
                    <!-- ЛОГО -->
                    <div class="col-md-3">
                        <div class="header-logo">
                            <a href="/main" class="logo">
                                <img src="/logo.png" alt="">
                            </a>
                        </div>
                    </div>
                    <!-- /ЛОГО -->
                    <!-- ПОИСКОВИК -->
                    <div class="col-md-6">
                        <div class="header-search">
    
                            <input class="input" placeholder="Поиск по магазину">
    
                            
                        </div>
                    </div>
                    <!-- /ПОИСКОВИК -->
    
                    <div class="col-md-3 clearfix">
                        <div class="header-ctn">
                            <!-- КОРЗИНА -->
                            <!-- <div class="dropdown">
                                <a href="/" class="dropdown-toggle" data-toggle="dropdown" aria-expanded="true">
                                    <a href="/bucket" class="btn btn-entrance"><i class="fa fa-shopping-cart"></i>
                                        <span>Корзина</span>
                                        </a>
                                </a>
                            </div> -->
                            <!-- /КОРЗИНА -->
                            {#if code_response == 200}
                            <div class="dropdown">
                                <a href="/bucket" class="header-a-right">
                                    <span class="right-header">Корзина</span>
                                </a>
                            </div>
                            <div class="dropdown">
                                <a href="/main" class="header-a-right" on:click={logout}>
                                    <span class="right-header">Выйти</span>
                                </a>

                            </div>
                            {:else}
                            <div class="dropdown">
                                <a href="/login" class="header-a-right">
                                    <span class="right-header">Войти</span>
                                </a>
                            </div>
                            {/if}
                        <!-- <div>
                            <div class="nav-item dropdown">
                                <a sec:authorize="isAuthenticated()" class="btn btn-entrance dropdown-toggle" id="upp" data-toggle="dropdown" aria-expanded="true">
                                    <i class="fa fa-user-o"></i>
                                    <div sec:authorize="isAuthenticated()" sec:authentication="principal.username" id="navbarDropdown" class="nav-link username">
                                        Dropdown
                                    </div>
                                </a>
    
                                <ul sec:authorize="isAuthenticated()" class="dropdown-menu" aria-labelledby="upp">
                                    <li><a class="dropdown-item" href="#" th:href="@{/logout}">Выйти</a></li>
                                </ul>
                            </div>
                            <a href="#" sec:authorize="!isAuthenticated()" class="btn btn-entrance" th:href="@{/login}">
                                <i class="fa fa-user-o"></i>
                                <span>Войти</span>
                            </a>
                        </div> -->
                        </div>
                    </div>
                </div>
                <!-- РЯД -->
            </div>
            <!-- БЛОК -->
        </div>
    </header>
    
    <nav class="navigation">
        <div class="container">
          <div id="responsive-nav">
              <ul class="main-nav nav navbar-nav">
                  <li><a href="/main">Главная</a></li>
                  <li><a href="/discounts">Скидки</a></li>
                  <li><a href="/chairs">Кресла</a></li>
                  <li><a href="/sofa">Диваны</a></li>
                  <li><a href="/lockers">Шкафы</a></li>
                  <li><a href="/beds">Кровати</a></li>
                  <li><a href="/tables">Столы</a></li>
              </ul>
          </div>
        </div>
    </nav>
    <slot/>
    <footer id="footer">
        <div class="section">
            <!-- БЛОК -->
            <div class="container">
                <!-- РЯД -->
                <div class="row">
                    <div class="col-md-6 col-xs-6">
                        <div class="footer">
                            <h3 class="footer-title">О нас</h3>
                            <p>Интернет-магазин поддержанной мебели.</p>
                            <ul class="footer-links">
                                <li><a href="/"><i class="fa fa-map-marker"></i>Москва</a></li>
                                <li><a href="/"><i class="fa fa-phone"></i>+999-99-99-99</a></li>
                                <li><a href="/"><i class="fa fa-envelope-o"></i>email@email.com</a></li>
                            </ul>
                        </div>
                    </div>

                    <div class="col-md-6 col-xs-6">
                        <div class="footer">
                            <h3 class="footer-title">Категории</h3>
                            <ul class="footer-links">
                                <li><a href="/chairs">Кресла</a></li>
                                <li><a href="/sofa">Диваны</a></li>
                                <li><a href="/lockers">Шкафы</a></li>
                                <li><a href="/beds">Кровати</a></li>
                                <li><a href="/tables">Столы</a></li>
                            </ul>
                        </div>
                    </div>

                    <div class="clearfix visible-xs"></div>
                </div>
                <!-- /РЯД -->
            </div>
            <!-- /БЛОК -->
        </div>
    </footer>
</main>

<style>
.btn {
    text-decoration: none;
}

header {
    background-color: #15161D;
    display: flex;
    margin-left: -1%;
    margin-top: -15px;
    margin-right: -1%;  
    padding-left: 10%;
}

.header-logo {
    float: left;
}

.header-logo .logo img {
    display: block;
    height: 70px;
}

.navigation {
  margin-left: -1%;
  margin-right: -1%;
  background: #FFF;
  border-bottom: 2px solid #E4E7ED;
  border-top: 3px solid #D10024;
}

.main-nav {
    display: flex;
}

.main-nav>li+li {
  margin-left: 30px;
  margin-left: 15%;
}

.main-nav>li>a {
  padding: 20px 0px;
  color: rgb(73, 73, 73);
}

.main-nav>li>a:hover, .main-nav>li>a:focus, .main-nav>li.active>a {
  color: #D10024;
  background-color: transparent;
}

.main-nav>li>a:after {
  content: "";
  display: block;
  width: 0%;
  height: 2px;
  background-color: #D10024;
  -webkit-transition: 0.2s all;
  transition: 0.2s all;
}

.main-nav>li>a:hover:after, .main-nav>li>a:focus:after, .main-nav>li.active>a:after {
  width: 100%;
}

.header-a-right{
    padding-top: 10px;
}

.right-header{
    color:orange;
    font-size: 15px;
}

footer {
        background: #15161D;
        color: #B9BABC;
        margin-left: -1%;
        margin-right: -1%; 
        height: 200px; 
        display: flex;
}

.footer {
    padding-left: 30%;
    margin-top: -2%;
}

.footer .footer-title {
    /* padding-top: 10px; */
    color: #FFF;
    text-transform: uppercase;
    font-size: 18px;
    margin: 0px 0px 10px;
}

.footer-links li+li {
    margin-top: 10px;
}

.footer-links li a {
    color: #B9BABC;
}

.footer-links li a:hover {
    color: #D10024;
}
</style>
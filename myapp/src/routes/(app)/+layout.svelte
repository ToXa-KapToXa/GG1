<script>
	
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
                            <div class="dropdown">
                                <a href="/" class="dropdown-toggle" data-toggle="dropdown" aria-expanded="true">
                                    <a href="/bucket" class="btn btn-entrance"><i class="fa fa-shopping-cart"></i>
                                        <span>Корзина</span>
                                        </a>
                                        <!--<div class="qty">0</div>-->
                                </a>
                                <div class="cart-dropdown">
                                    <div class="cart-list">
                                        <!--<div class="product-widget" th:each="detail : ${bucket.bucketDetails}">
                                            <div class="product-img">
                                                <img th:src="${detail.image_url}" alt="">
                                            </div>
                                            <div class="product-body">
                                                <h3 class="product-name"><a href="#" th:text="${detail.title}">YAMAHA F310</a></h3>
                                                <h4 class="product-price" th:text="${detail.price}">₽13.500</h4>
                                                <span class="qty"><span th:text="${detail.amount}"></span>x</span>
                                            </div>-->
                                    </div>
    
                                    <div class="cart-summary">
                                        <div class="itogo"><h5>ИТОГО:</h5></div>
                                        <div class="fullprice"></div>
                                    </div>
    
                                    <div class="cart-btns">
                                        <a href="/">Оплатить  <i class="fa fa-arrow-circle-right"></i></a>
                                    </div>
                                </div>
                            </div>
                            <!-- /КОРЗИНА -->
    
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
    
                        <!-- МЕНЮ -->
                            <div class="menu-toggle">
                                <a href="/">
                                    <i class="fa fa-bars"></i>
                                    <span>Меню</span>
                                </a>
                            </div>
                            <!-- /МЕНЮ -->
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
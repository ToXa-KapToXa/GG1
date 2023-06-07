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
                                <img src="./logo.png" alt="">
                            </a>
                        </div>
                    </div>
                    <!-- /ЛОГО -->

                    <div class="col-md-6">
                    </div>

                    <div class="col-md-3 clearfix">
                        <div class="header-ctn">
    
                            <div class="dropdown">
                                <a href="/main" class="header-a-right">
                                    <span class="right-header">Главная</span>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- РЯД -->
            </div>
            <!-- БЛОК -->
        </div>
    </header>
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
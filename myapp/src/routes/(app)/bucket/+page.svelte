<script>
let products = [
        {id: 1, name: "Кресло Людвиг", price: "9 999", category: "Кресло", namefile: "./images/kreslo1.webp", neww: true, old_price: "15 999", sale: "-20%", hit: true},
        {id: 2, name: "Кресло Gap", price: "6 999", category: "Кресло", namefile: "./images/kreslo2.jpg", neww: true, old_price: "", sale: "", hit: false},
        {id: 3, name: "Кресло Агата", price: "5 999", category: "Кресло", namefile: "./images/kreslo3.jpg", neww: false, old_price: "", sale: "", hit: true},
        {id: 4, name: "Кресло Сиеста", price: "13 999", category: "Кресло", namefile: "./images/kreslo4.webp", neww: true, old_price: "", sale: "", hit: false},
        {id: 5, name: "Кресло Гауди", price: "7 999", category: "Кресло", namefile: "./images/kreslo5.jpg", neww: false, old_price: "9 999", sale: "-20%", hit: true},

        // {id: 11, name: "Диван Парма", price: "10 999", category: "Диван", namefile: "./images/divan1.webp", neww: false, old_price: "21 999", sale: "-50%", hit: true},
        // {id: 12, name: "Диван Куба", price: "7 999", category: "Диван", namefile: "./images/divan2.jpg", neww: true, old_price: "", sale: "", hit: false},
        // {id: 13, name: "Диван Дени", price: "16 990", category: "Диван", namefile: "./images/divan3.jpg", neww: false, old_price: "35 999", sale: "-52%", hit: true},
        // {id: 14, name: "Диван Уно", price: "16 999", category: "Диван", namefile: "./images/divan4.jpg", neww: true, old_price: "27 999", sale: "-39%", hit: false},
        // {id: 15, name: "Диван Торонто", price: "14 999", category: "Диван", namefile: "./images/divan5.jpg", neww: false, old_price: "27 999", sale: "-46%", hit: true},

        // {id: 21, name: "Шкаф для одежды Рона", price: "10 599", category: "Шкаф", namefile: "./images/skaf1.jpg", neww: false, old_price: "", sale: "", hit: false},
        // {id: 22, name: "Шкаф Атлант", price: "9 999", category: "Шкаф", namefile: "./images/skaf2.jpg", neww: true, old_price: "", sale: "", hit: true},
        // {id: 23, name: "Шкаф Tiffany", price: "28 599", category: "Шкаф", namefile: "./images/skaf3.webp", neww: false, old_price: "", sale: "", hit: false},
        // {id: 24, name: "Шкаф для одежды Коста", price: "8 999", category: "Шкаф", namefile: "./images/skaf4.jpg", neww: true, old_price: "", sale: "", hit: true},
        // {id: 25, name: "Шкаф SILVA Оливия", price: "17 199", category: "Шкаф", namefile: "./images/skaf5.jpg", neww: false, old_price: "", sale: "", hit: true},

        // {id: 31, name: "Каркас кровати Соренто", price: "5 599", category: "Кровать", namefile: "./images/bed1.webp", neww: false, old_price: "6 999", sale: "-21", hit: true},
        // {id: 32, name: "Каркас кровати Глазго", price: "11 999", category: "Кровать", namefile: "./images/bed2.jpg", neww: false, old_price: "", sale: "", hit: false},
        // {id: 33, name: "Каркас кровати Астра", price: "7 999", category: "Кровать", namefile: "./images/bed3.jpg", neww: true, old_price: "", sale: "", hit: true},
        // {id: 34, name: "Кровать Мета", price: "4 899", category: "Кровать", namefile: "./images/bed4.jpg", neww: false, old_price: "", sale: "", hit: true},
        // {id: 35, name: "Каркас кровати Ирен", price: "2 999", category: "Кровать", namefile: "./images/bed5.jpg", neww: true, old_price: "", sale: "", hit: false},

        // {id: 41, name: "Приставной стол Бьюти", price: "2 799", category: "Стол", namefile: "./images/stol1.webp", neww: true, old_price: "", sale: "", hit: true},
        // {id: 42, name: "Журнальный стол SILVA", price: "3 999", category: "Стол", namefile: "./images/stol2.jpg", neww: true, old_price: "", sale: "", hit: false},
        // {id: 43, name: "Журнальный стол Мартин", price: "5 599", category: "Стол", namefile: "./images/stol3.jpg", neww: false, old_price: "", sale: "", hit: true},
        // {id: 44, name: "Журнальный стол Лофт", price: "1 599", category: "Стол", namefile: "./images/stol4.webp", neww: true, old_price: "", sale: "", hit: false},
        // {id: 45, name: "Журнальный стол Вика", price: "9 999", category: "Стол", namefile: "./images/stol5.webp", neww: false, old_price: "", sale: "", hit: false},
    ]
</script>

<main>
<!-- СЕКЦИЯ -->
<div class="section">
    <!-- БЛОК -->
    <div class="container">
        <!-- РЯД -->
        <div class="row">
            <h2>Ваша корзина</h2>
            {#each products as product}
            <div>
                <div class="product-widget">
                    <div class="product-img">
                        <img src={product.namefile} alt="">
                    </div>
                    <div class="product-body">
                        <h3 class="product-name"><a href="/">{product.name}</a></h3>
                        <h4 class="product-price">₽{product.price}</h4>
                        <span class="qty"><span></span>x</span>
                    </div>
                    <div>
                        <a href="/"><button class="add-to-cart-btn plus">Удалить</button></a>
                    </div>
                </div>
            </div>
            {/each}

           <!-- <table border="1" align="center">
                <tr>
                    <td>Title</td>
                    <td>Amount</td>
                    <td>Price</td>
                    <td>Sum</td>
                    <td></td>
                </tr>
                <tr th:each="detail : ${bucket.bucketDetails}">
                    <td th:text="${detail.title}">Cheese</td>
                    <td th:text="${detail.amount}">2</td>
                    <td th:text="${detail.price}">11.0</td>
                    <td th:text="${detail.sum}">22</td>
                    <td><a href="#">Remove</a></td>
                </tr>
            </table>-->

            <!-- <h3 id="itogoo">Итого: ₽<b th:text="${bucket.sum}">1000</b></h3> -->

        </div>
        <!-- РЯД -->
    </div>
    <!-- БЛОК -->
</div>
<!-- СЕКЦИЯ -->
</main>

<style>

</style>
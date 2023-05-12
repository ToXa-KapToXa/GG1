<script>
    let products = [
        {id: 1, name: "Кресло Людвиг", price: "9 999", category: "Кресло", namefile: "./images/kreslo1.webp", neww: true, old_price: "15 999", sale: "-20%", hit: true},
        {id: 2, name: "Кресло Gap", price: "6 999", category: "Кресло", namefile: "./images/kreslo2.jpg", neww: true, old_price: "", sale: "", hit: false},
        {id: 3, name: "Кресло Агата", price: "5 999", category: "Кресло", namefile: "./images/kreslo3.jpg", neww: false, old_price: "", sale: "", hit: true},
        {id: 4, name: "Кресло Сиеста", price: "13 999", category: "Кресло", namefile: "./images/kreslo4.webp", neww: true, old_price: "", sale: "", hit: false},
        {id: 5, name: "Кресло Гауди", price: "7 999", category: "Кресло", namefile: "./images/kreslo5.jpg", neww: false, old_price: "9 999", sale: "-20%", hit: true},

        {id: 11, name: "Диван Парма", price: "10 999", category: "Диван", namefile: "./images/divan1.webp", neww: false, old_price: "21 999", sale: "-50%", hit: true},
        {id: 12, name: "Диван Куба", price: "7 999", category: "Диван", namefile: "./images/divan2.jpg", neww: true, old_price: "", sale: "", hit: false},
        {id: 13, name: "Диван Дени", price: "16 990", category: "Диван", namefile: "./images/divan3.jpg", neww: false, old_price: "35 999", sale: "-52%", hit: true},
        {id: 14, name: "Диван Уно", price: "16 999", category: "Диван", namefile: "./images/divan4.jpg", neww: true, old_price: "27 999", sale: "-39%", hit: false},
        {id: 15, name: "Диван Торонто", price: "14 999", category: "Диван", namefile: "./images/divan5.jpg", neww: false, old_price: "27 999", sale: "-46%", hit: true},

        {id: 21, name: "Шкаф для одежды Рона", price: "10 599", category: "Шкаф", namefile: "./images/skaf1.jpg", neww: false, old_price: "", sale: "", hit: false},
        {id: 22, name: "Шкаф Атлант", price: "9 999", category: "Шкаф", namefile: "./images/skaf2.jpg", neww: true, old_price: "", sale: "", hit: true},
        {id: 23, name: "Шкаф Tiffany", price: "28 599", category: "Шкаф", namefile: "./images/skaf3.webp", neww: false, old_price: "", sale: "", hit: false},
        {id: 24, name: "Шкаф для одежды Коста", price: "8 999", category: "Шкаф", namefile: "./images/skaf4.jpg", neww: true, old_price: "", sale: "", hit: true},
        {id: 25, name: "Шкаф SILVA Оливия", price: "17 199", category: "Шкаф", namefile: "./images/skaf5.jpg", neww: false, old_price: "", sale: "", hit: true},

        {id: 31, name: "Каркас кровати Соренто", price: "5 599", category: "Кровать", namefile: "./images/bed1.webp", neww: false, old_price: "6 999", sale: "-21", hit: true},
        {id: 32, name: "Каркас кровати Глазго", price: "11 999", category: "Кровать", namefile: "./images/bed2.jpg", neww: false, old_price: "", sale: "", hit: false},
        {id: 33, name: "Каркас кровати Астра", price: "7 999", category: "Кровать", namefile: "./images/bed3.jpg", neww: true, old_price: "", sale: "", hit: true},
        {id: 34, name: "Кровать Мета", price: "4 899", category: "Кровать", namefile: "./images/bed4.jpg", neww: false, old_price: "", sale: "", hit: true},
        {id: 35, name: "Каркас кровати Ирен", price: "2 999", category: "Кровать", namefile: "./images/bed5.jpg", neww: true, old_price: "", sale: "", hit: false},

        {id: 41, name: "Приставной стол Бьюти", price: "2 799", category: "Стол", namefile: "./images/stol1.webp", neww: true, old_price: "", sale: "", hit: true},
        {id: 42, name: "Журнальный стол SILVA", price: "3 999", category: "Стол", namefile: "./images/stol2.jpg", neww: true, old_price: "", sale: "", hit: false},
        {id: 43, name: "Журнальный стол Мартин", price: "5 599", category: "Стол", namefile: "./images/stol3.jpg", neww: false, old_price: "", sale: "", hit: true},
        {id: 44, name: "Журнальный стол Лофт", price: "1 599", category: "Стол", namefile: "./images/stol4.webp", neww: true, old_price: "", sale: "", hit: false},
        {id: 45, name: "Журнальный стол Вика", price: "9 999", category: "Стол", namefile: "./images/stol5.webp", neww: false, old_price: "", sale: "", hit: false},
    ]
</script>

<main>
    <h3>Кресла</h3>
    <div class="product1">
        {#each products as {name, price, namefile, category, neww, old_price, sale, hit}}
        {#if category === "Стол"}
            <div class="product">
                <div class="product-img">
                    <img src={namefile} alt={name}>
                    {#if (neww && sale)}
                    <div class="product-label">
                        <span class="new">НОВИНКА</span>
                        <span class="sale">{sale}</span>
                    </div>
                    {:else if neww}
                    <div class="product-label">
                        <span class="new">НОВИНКА</span>
                    </div>
                    {:else if sale}
                    <div class="product-label">
                        <span class="sale">{sale}</span>
                    </div>
                    {/if}
                </div>
                <div class="product-body">
                    <p class="product-category">{category}</p>
                    <h3 class="product-name"><a href="/">{name}</a></h3>
                    <h4 class="product-price">{price} ₽
                        {#if old_price}
                        <del class="product-old-price">{old_price}</del>
                        {/if}
                    </h4>
                    <div class="product-rating">
                        <i class="fa fa-star"></i>
                        <i class="fa fa-star"></i>
                        <i class="fa fa-star"></i>
                        <i class="fa fa-star"></i>
                    </div>
                </div>
                <div class="add-to-cart">
                    <a href="/"><button class="add-to-cart-btn plus"><img src="./icons/shopping-cart.svg" alt =""/> В корзину</button></a>
                </div>
            </div>
        {/if}
        {/each}
    </div>
</main>

<style>
    main {
    margin-left: 6%;
}

h3 {
    margin-bottom: -5px;
    margin-left: 6%;
}

.product-price {
    padding-top: 7px;
}
</style>
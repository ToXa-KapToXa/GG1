<script>
    import { onMount } from "svelte";
    const url = "https://gg1-back.onrender.com/api/product/category/Chair"
    export let Products = [];

    onMount(async function () {
    const response = await fetch(url);
    const data = await response.json();
    console.log(data);
    Products = data["data"]["product"]
    console.log(Products)
  });
</script>

<main>
    <h3>Кресла</h3>
    <div class="product1">
    {#each Products as product}
        <div class="product">
            <div class="product-img">
                <img src={product.namefile} alt={product.name}>
                {#if (product.new && product.sale)}
                <div class="product-label">
                    <span class="new">НОВИНКА</span>
                    <span class="sale">-{product.sale}%</span>
                </div>
                {:else if product.new}
                <div class="product-label">
                    <span class="new">НОВИНКА</span>
                </div>
                {:else if product.sale}
                <div class="product-label">
                    <span class="sale">-{product.sale}%</span>
                </div>
                {/if}
            </div>
            <div class="product-body">
                <p class="product-category">{product.category}</p>
                <h3 class="product-name"><a href="/">{product.name}</a></h3>
                {#if product.sale}
                <h4 class="product-price">{Math.round(product.price*(1-(product.sale/100)))} ₽
                    <del class="product-old-price">{product.price}</del>
                </h4>
                {:else}
                <h4 class="product-price">{product.price} ₽
                </h4>
                {/if}
            </div>
            <div class="add-to-cart">
                <a href="/"><button class="add-to-cart-btn plus"><img src="./icons/shopping-cart.svg" alt =""/> В корзину</button></a>
            </div>
        </div>
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
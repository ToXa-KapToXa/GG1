<script>

</script>

<main>
<!-- СЕКЦИЯ -->
<div class="section">
    <!-- БЛОК -->
    <div class="container">
        <!-- РЯД -->
        <div class="row">
            <h2>Ваша корзина</h2>
            <!-- <div>

                <div class="product-widget" th:each="detail : ${bucket.bucketDetails}">
                    <div class="product-img">
                        <img th:src="${detail.image_url}" alt="">
                    </div>
                    <div class="product-body">
                        <h3 class="product-name"><a href="#" th:text="${detail.title}">YAMAHA F310</a></h3>
                        <h4 class="product-price" th:text="${detail.price}">₽13.500</h4>
                        <span class="qty"><span th:text="${detail.amount}"></span>x</span>
                    </div>
                    <div>
                        <a href="/"><button class="add-to-cart-btn plus">Удалить</button></a>
                    </div>
                </div>
            </div> -->

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
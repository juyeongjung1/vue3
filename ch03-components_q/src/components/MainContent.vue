<script setup lang="ts">



//【3.2】以下のコードの意味を確認してください。キー名や型名に注目してください。


// 商品配列の型定義
type Product = { 
    id: number; 
    name: string; 
    price: number; 
    category: string 
}

// 親から受け取る配列のpropsを定義
const props = defineProps<{ products: Product[] }>()

//////////////【ここから、3.3の問題】///////////////
// ➀ 以下に、 親へ通知するイベントを定義してください。


// ➁ 以下に、 ボタンが押されたときにemitで親にIDを通知する関数を作成してください。


//////////////【ここまで、3.3の問題】///////////////
</script>

<template>
  <main>
    <div class="card ">
      <div class="card-body">
        <h2 class="mb-3">商品一覧</h2>

        <table class="table table-striped table-hover align-middle">
          <thead class="table-dark">
            <tr>
              <th>商品番号</th>
              <th>商品名</th>
              <th>価格</th>
              <th>カテゴリ</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="p in props.products" :key="p.id">
              <td>{{ p.id }}</td>
              
              <td>
                <!--【3.3 ➂】 以下の商品名をリンク風にして、➁の関数にp.idを入れるように修正してください -->
                <button class="btn btn-link"                  >

                </button>
              </td>
              <td>{{ p.price }} 円</td>
              <td>{{ p.category }}</td>
            </tr>
          </tbody>
        </table>
      </div>
      <h2 class="mb-4">おすすめ商品</h2>
      <div class="row">
        <!-- 【3.4 ➅ 】productCardをimportしてください。-->
        <!-- 【3.4 ➆ 】以下のfor文を確認してください。-->
        <div class="col-md-4 mb-4" v-for="product in products" :key="product.id">
          <!-- 【3.4 ➇】以下にProductCardを配置し、productをv:bindで指定してください-->

        </div>
    </div>
    </div>
  </main>
</template>

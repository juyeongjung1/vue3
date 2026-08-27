<script setup lang="ts">

// 【4.5 ➁】Vueのinjectと、Ref型をインポートしてください。


// 【4.5 ➂】以下の商品配列の型定義している部分を確認してください。
type Product = {
    id: number;
    name: string;
    price: number;
    category: string
}
// 【4.5 ➃】以下の仮配列を、App.vueでprovideされた「products」を受け取るコードに置き換えてください。
// 4.3・4.4では、表の見出しだけを表示するために空の配列を使用します。
const products: Product[] = []

// 【3章の内容】親から受け取るpropsを定義
// const props = defineProps<{ products: Product[] }>()

// 【3章の内容】親へ通知するイベントを定義
// const emit = defineEmits(['select'])

// 【3章の内容】ボタンが押されたときにemitで親にIDを通知
//const selectRow = (id: number) => {
//    emit('select', id)
//}
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
          <!-- 【4.5 ➄】以下がinjectで受け取ったproductsを参照していることを確認してください。-->
                        <tr v-for="p in products" :key="p.id">
                            <td>{{ p.id }}</td>
                            <td>
          <!-- 【4.6 ➁】以下に、詳細画面へ遷移する動的URLを持つRouterLinkを入れてください。-->

                              {{ p.name }}
                            </td>
                            <td>{{ p.price }} 円</td>
                            <td>{{ p.category }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </main>
</template>

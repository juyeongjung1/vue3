<script setup lang="ts">
import { inject } from 'vue'
import type { Ref } from 'vue'

// 商品配列の型定義
type Product = {
  id: number;
  name: string;
  price: number;
  category: string
}
// App.vueでprovideされた「products」を受け取る
const products = inject('products') as Ref<Product[]>

// 【3章の内容】親から受け取るpropsを定義
//const props = defineProps<{ products: Product[] }>()

// 【3章の内容】親へ通知するイベントを定義
//const emit = defineEmits(['select'])

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
            <tr v-for="p in products" :key="p.id">
              <td>{{ p.id }}</td>
              <td>
                <RouterLink :to="`/products/${p.id}`">
                  {{ p.name }}
                </RouterLink>
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

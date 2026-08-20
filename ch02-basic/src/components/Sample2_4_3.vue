<script setup lang="ts">
import { reactive } from 'vue'

// 商品の配列（本来はDBやAPIから取得することを想定）
const products = reactive([
  { id: 1, name: 'ノートパソコン', price: 120000 },
  { id: 2, name: 'マウス', price: 2500 },
  { id: 3, name: 'キーボード', price: 4800 }
])
</script>

<template>
    <h3>商品一覧</h3>

    <!-- v-forで配列の中身を順に表示 -->
    <table class="table table-bordered w-auto">
      <thead class="table-light">
        <tr>
          <th>商品ID</th>
          <th>商品名</th>
          <th>価格</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="p in products" :key="p.id">
          <td>{{ p.id }}</td>
          <td>{{ p.name }}</td>
          <td>{{ p.price }}円</td>
        </tr>
      </tbody>
    </table>
</template>
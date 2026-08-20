<script setup lang="ts">
import { reactive } from 'vue'

// ➀ 配列をreactive関数でリアクティブ化している部分を確認してください
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
        <!--➁ 以下に、products配列内のオブジェクトを順番に出力してください。 -->
        <tr                          >
          <td>     </td>
          <td>     </td>
          <td>   円</td>
        </tr>
      </tbody>
    </table>
</template>
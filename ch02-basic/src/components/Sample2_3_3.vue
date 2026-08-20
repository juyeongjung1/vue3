<script setup lang="ts">
import { reactive, computed } from 'vue' //computedを同時にimport

// reactive関数でオブジェクトをリアクティブ化
const product = reactive({
  id: 1,
  name: 'ノートパソコン',
  price: 50000
})

// computed関数で、priceが変わると自動再計算
// TypeScriptの型注釈として number を指定
const taxIncludedPrice = computed(():number => {
  return Math.floor(product.price * 1.1) // 税込価格を計算（小数点以下切り捨て）
})

const raisePrice = (): void => { // 価格を上げる関数。戻り値型を明示的に指定
  product.price += 1000
}
</script>

<template>
  <h3>商品情報</h3>
  <ul>
    <li>商品番号：{{ product.id }}</li>
    <li>商品名　：{{ product.name }}</li>
    <li>価格(税抜)：{{ product.price }}</li>
    <li>価格(税込)：{{ taxIncludedPrice }}</li>
  </ul>

  <!-- 価格を更新すると、税込価格も自動で再計算 -->
  <button @click="raisePrice">価格 +1000</button>
</template>

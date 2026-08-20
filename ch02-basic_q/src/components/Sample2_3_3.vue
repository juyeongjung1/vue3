<script setup lang="ts">
import { reactive} from 'vue' // ➀　computedもimportしてください

// ➁　reactive関数でオブジェクトをリアクティブ化していることを確認してください
const product = reactive({
  id: 1,
  name: 'ノートパソコン',
  price: 50000
})

// ➂ ここに、computed関数で税込価格を計算する変数を作成してください
// 税込価格は、priceに1.1をかけて小数点以下を切り捨てた値としてください
// TypeScriptの型注釈として number を指定してください
const taxIncludedPrice = ""


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
    <!-- ➃　ここに、算術プロパティを入れてください。-->
    <li>価格(税込)：{{ }}</li>
  </ul>

  <!-- 価格を更新すると、税込価格も自動で再計算 -->
  <button @click="raisePrice">価格 +1000</button>
</template>

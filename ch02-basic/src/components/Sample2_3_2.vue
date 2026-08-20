<script setup lang="ts">
import { reactive } from 'vue' // reactive関数をインポート

// reactive関数で複数プロパティをまとめてリアクティブ化
const product = reactive({　
  id: 1,
  name: 'ノートパソコン',
  price: 50000
})　

const raisePrice = () => {　// 価格を上げる関数
  product.price += 1000　// reactiveで作成した変数は、.value不要で直接アクセスできる
}

const rename = () => {　// 名前を更新する関数
  product.name += ' (New)'; 
}
</script>

<template>
  <h3>商品情報</h3>
  <ul>
    <li>商品番号：{{ product.id }}</li>
    <li>商品名　：{{ product.name }}</li>
    <li>価格　　：{{ product.price }}</li>
  </ul>

  <!-- ボタン操作でオブジェクトの中身を更新 -->
  <button @click="raisePrice">価格 +1000</button>
  <button @click="rename">名前を更新</button>
</template>

<script setup lang="ts">
import { ref } from 'vue' // ref関数をインポート(毎回必須)

const count = ref(0) // ref関数でリアクティブな変数を作成

const increment = () => { // カウントを増やす関数
  count.value++ // refで作成した変数の値を変更する場合は.valueを使う
}
</script>

<template>
  <!-- refで作成した変数の値を参照する場合も.valueは不要 -->
  <p>現在のカウント：{{ count }}</p>  
  <!-- ボタンをクリックしたらincrement関数を実行 -->
  <button @click="increment">増やす</button>
</template>
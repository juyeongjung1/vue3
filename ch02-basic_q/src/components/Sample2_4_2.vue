<script setup lang="ts">
import { ref } from 'vue'

// ➀ 以下のリアクティブ変数を確認してください。（1:東京 / 2:大阪 / 3:名古屋）
const state = ref(1)

// ➁　v-show用のリアクティブ変数を確認してください。(メモの表示・非表示用)
const showMemo = ref(false)

// ➂　「次の会場へ」ボタンをクリックした際の分岐処理を確認してください。
const next = (): void => {
  if (state.value === 1) {
    state.value = 2
  }
  else if (state.value === 2) {
    state.value = 3
  }
  else {
    state.value = 1
  }
}

//➃ 以下の「メモの表示切り替え」ボタンをクリックした際の処理を確認してください。
const toggleMemo = (): void => {
  showMemo.value = !showMemo.value
}
</script>

<template>
  <h3>会場案内</h3>

  <!--➄ 以下のdiv要素に、stateの値が1,2,3の条件を書いてください。-->
  <div        > 東京会場 </div>
  <div        > 大阪会場</div>
  <div        > 名古屋会場</div>

  <button class="btn btn-primary mt-2" @click="next">次の会場</button>

  <hr class="my-3" />

  <button class="btn btn-outline-secondary mb-2" @click="toggleMemo">
    <!--➅ 以下の三項演算子のコードを確認してください。-->
    メモを{{ showMemo ? '隠す' : '表示' }}
  </button>
  
  <!-- ➆ 以下のp要素に、showMemoの値による表示・非表示の切り替えを書いてください。-->
  <p               >メモ：当日は5分前集合</p>
</template>

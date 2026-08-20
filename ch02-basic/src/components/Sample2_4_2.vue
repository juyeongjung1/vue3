<script setup lang="ts">
import { ref } from 'vue'

// 会場の状態（1:東京 / 2:大阪 / 3:名古屋）
const state = ref(1)
  
// v-show用：メモの表示・非表示
const showMemo = ref(false)

// 次の会場へ
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

// メモの表示切り替え
const toggleMemo = (): void => {
  showMemo.value = !showMemo.value
}
</script>

<template>
  <h3>会場案内</h3>

  <!-- v-if / v-else-if / v-else：状態に合わせて表示ブロックを切替 -->
  <div v-if="state === 1">  東京会場 </div>
  <div v-else-if="state === 2"> 大阪会場</div>
  <div v-else> 名古屋会場</div>

  <button class="btn btn-primary mt-2" @click="next">次の会場</button>

  <hr class="my-3" />

  <!-- v-show：要素は残したまま見た目だけ隠す/見せる -->
  <button class="btn btn-outline-secondary mb-2" @click="toggleMemo">
    メモを{{ showMemo ? '隠す' : '表示' }}
  </button>
  <p v-show="showMemo">メモ：当日は5分前集合</p>
</template>

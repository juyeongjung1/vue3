<script setup lang="ts">
import { ref } from 'vue'
import Q2_2 from './components/Q2_2.vue'
import Q2_3_1 from './components/Q2_3_1.vue'
import Q2_3_2 from './components/Q2_3_2.vue'
import Q2_3_3 from './components/Q2_3_3.vue'
import Q2_4_1 from './components/Q2_4_1.vue'
import Q2_4_2 from './components/Q2_4_2.vue'
import Q2_4_3 from './components/Q2_4_3.vue'
import Q2_5 from './components/Q2_5.vue'
import Q2_6 from './components/Q2_6.vue'

const section = ref('setup')
</script>

<template>
  <nav>
   <button @click="section = 'Q2_2'">2-2. Vueコンポーネントの基本</button>
    <button @click="section = 'Q2_3_1'">2-3-1. ref()関数</button>
    <button @click="section = 'Q2_3_2'">2-3-2. reactive()関数</button>
    <button @click="section = 'Q2_3_3'">2-3-3. computed()関数</button>
    <button @click="section = 'Q2_4_1'">2-4-1. v-bind</button>
    <button @click="section = 'Q2_4_2'">2-4-2. v-if</button>
    <button @click="section = 'Q2_4_3'">2-4-3. v-for</button>
    <button @click="section = 'Q2_5'">2-5. イベント処理</button>
    <button @click="section = 'Q2_6'">2-6. フォーム入力</button>
  </nav>

  <div class="content">
    <Q2_2 v-if="section === 'Q2_2'" />
    <Q2_3_1 v-else-if="section === 'Q2_3_1'" />
    <Q2_3_2 v-else-if="section === 'Q2_3_2'" />
    <Q2_3_3 v-else-if="section === 'Q2_3_3'" />
    <Q2_4_1 v-else-if="section === 'Q2_4_1'" />
    <Q2_4_2 v-else-if="section === 'Q2_4_2'" />
    <Q2_4_3 v-else-if="section === 'Q2_4_3'" />
    <Q2_5 v-else-if="section === 'Q2_5'" />
    <Q2_6 v-else-if="section === 'Q2_6'" />
  </div>
</template>

<style scoped>
nav { margin-bottom: 1rem; }
button { margin-right: 0.5rem; }
</style>

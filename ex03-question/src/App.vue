<script setup lang="ts">
import { ref } from 'vue'
import Q3_1 from './components/Q3_1/App_Q3_1.vue'
import Q3_2 from './components/Q3_2/App_Q3_2.vue'
import Q3_3 from './components/Q3_3/App_Q3_3.vue'
import Q3_4 from './components/Q3_4/App_Q3_4.vue'

const section = ref('setup')
</script>

<template>
  <nav>
   <button @click="section = 'Q3_1'">3-1</button>
   <button @click="section = 'Q3_2'">3-2</button>
   <button @click="section = 'Q3_3'">3-3</button>
   <button @click="section = 'Q3_4'">3-4</button>

    
  </nav>

  <div class="content">
    <Q3_1 v-if="section === 'Q3_1'" />
    <Q3_2 v-else-if="section === 'Q3_2'" />
    <Q3_3 v-else-if="section === 'Q3_3'" />
    <Q3_4 v-else-if="section === 'Q3_4'" />
   
  </div>


</template>
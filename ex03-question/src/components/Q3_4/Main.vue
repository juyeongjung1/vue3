<script setup lang="ts">
import EmployeeCard from './EmployeeCard.vue' // インポート

// 型定義（photoUrlを追加）
type Employee = {
  id: number
  name: string
  salary: number
  department: string
  photoUrl: string
}

// 配列として受け取る
const props = defineProps<{ employeeList: Employee[] }>()

// イベントの定義（孫からのイベントをそのまま親へ流す）
const emit = defineEmits(['select'])
const onSelect = (name: string) => {
  emit('select', name)
}
</script>

<template>
  <main class="p-3">
    <div class="container">
      <h2 class="fs-4 mb-3">社員一覧</h2>
      
      <div class="mb-4">
        <slot>
          <p class="text-muted">お知らせはありません。</p>
        </slot>
      </div>

      <div class="row">
        <div class="col-md-4 mb-4" v-for="employee in props.employeeList" :key="employee.id">
          
          <EmployeeCard 
            :employee="employee" 
            @select="onSelect" 
          />
          
        </div>
      </div>

    </div>
  </main>
</template>
<script setup lang="ts">
import { inject } from 'vue'
import type { Ref } from 'vue'
// c. RouterLinkを使用するため、以下の行頭の「//」を外してください。
// import { RouterLink } from 'vue-router'

type Employee = {
  id: number
  name: string
  salary: number
  department: string
}

const employeeList = inject('employeeList') as Ref<Employee[]>
</script>

<template>
  <div class="p-3">
    <h2 class="mb-4">社員一覧</h2>
    <table class="table table-bordered table-hover">
      <thead class="table-secondary">
        <tr>
          <th>社員ID</th>
          <th>氏名</th>
          <th>給与</th>
          <th>部署</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="employee in employeeList" :key="employee.id">
          <td>{{ employee.id }}</td>
          <td>
 <!-- c. 一覧画面のリンク化（EmployeeListView.vue）
➀	テーブル内の「氏名」を表示している部分を <RouterLink> タグで囲みます。
➁	to 属性には、idを含む動的なパスか、または名前付きルートを指定してください。 -->
       
              {{ employee.name }}
          
          </td>
          <td>{{ employee.salary }}円</td>
          <td>{{ employee.department }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

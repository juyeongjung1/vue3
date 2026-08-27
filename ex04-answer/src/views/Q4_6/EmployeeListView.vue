<script setup lang="ts">
// d. ➀ vue から inject をimportしてください。
import { inject } from 'vue'
// d. ➁ vue から Ref をimport typeしてください。
import type { Ref } from 'vue'
import { RouterLink } from 'vue-router'

// d ➂ 社員データの型定義（Employee型）を確認してください。
type Employee = {
  id: number
  name: string
  salary: number
  department: string
}

//d ➃ inject を使用して、親から提供された 'employeeList' を受け取り、
// 変数（例: employeeList）に格納してください。
// ※TypeScriptの場合、as Ref<Employee[]> で型を指定しておくと安全です。
const employeeList = inject('employeeList') as Ref<Employee[]>
</script>

<template>
  <div class="p-3">
    <h2 class="mb-4">社員一覧</h2>

    <!-- ➄ HTMLのテーブルの部分を確認してください。 -->
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
<!-- ➅ テーブルのボディ（tbody）で v-for を使用し、受け取った employeeList をループして各行を表示してください。 -->
        <tr v-for="employee in employeeList" :key="employee.id">
          <td>{{ employee.id }}</td>
          <td>
            <RouterLink :to="`/Q4_6/employees/${employee.id}`">
              {{ employee.name }}
            </RouterLink>
          </td>
          <td>{{ employee.salary }}円</td>
          <td>{{ employee.department }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

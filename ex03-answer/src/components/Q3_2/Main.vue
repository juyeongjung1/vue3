<script setup lang="ts">
//➀ 社員1人分の型 EmployeeList（id, name, salary, department）を定義してください。
type EmployeeList = {
  id: number
  name: string
  salary: number
  department: string
}

//➁ defineProps を使用して、employeeList という名前で EmployeeListの配列 を受け取れるようにしてください。
const props = defineProps<{ employeeList: EmployeeList[] }>()
</script>

<template>
  <main class="p-3">
    <div class="container h-100">
      <h2 class="fs-4">社員一覧</h2>
      <table class="table table-bordered">
        <thead>
          <tr class="table-secondary text-center">
            <th scope="col">社員ID</th>
            <th scope="col">氏名</th>
            <th scope="col">給与</th>
            <th scope="col">部署名</th>
          </tr>
        </thead>
        <tbody>

<!-- ➂ tr タグに v-for を適用し、
 受け取ったリストの中身（社員ID、氏名、給与、部署名）をテーブルに表示してください。 -->
          <tr v-for="employee in props.employeeList" :key="employee.id" class="text-center">
            <td>{{ employee.id }}</td>
            <td>{{ employee.name }}</td>
            <td>{{ employee.salary }}円</td>
            <td>{{ employee.department }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </main>
</template>

<script setup lang="ts">
type EmployeeList = {
  id: number
  name: string
  salary: number
  department: string
}

const props = defineProps<{ employeeList: EmployeeList[] }>()

// ➀ defineEmits を使用して、親へ通知するためのイベント（イベント名: 'select'）を定義してください。
const emit = defineEmits(['select'])

// ➁ 社員が選択された時に実行する関数（例: onSelect）を作成してください。
// この関数内で emit を実行し、引数として受け取った「社員名」を親へ渡します。
const onSelect = (name: string) => {
  emit('select', name)
}
</script>

<template>
  <main class="p-3">
    <div class="container">
      <h2 class="fs-4">社員一覧</h2>
      <table class="table table-bordered">
        <thead>
          <tr class="table-secondary text-center">
            <th scope="col">社員ID</th>
            <th scope="col">氏名</th>
            <th scope="col">給与</th>
            <th scope="col">部署名</th>
            <!--➂ テーブル見出し（thead）に追加された「操作」列を確認してください。 -->
            <th scope="col">操作</th> </tr>
        </thead>
        <tbody>
          <tr v-for="employee in props.employeeList" :key="employee.id" class="text-center">
            <td>{{ employee.id }}</td>
            <td>{{ employee.name }}</td>
            <td>{{ employee.salary }}円</td>
            <td>{{ employee.department }}</td>
            <td>
 <!-- ➃テーブルのデータ行（tbody）に「選択」ボタンを追加し、
  クリック時（@click）に onSelect 関数を社員名を渡しながら呼び出すように記述してください。 -->
              <button class="btn btn-primary btn-sm" @click="onSelect(employee.name)">
                選択
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </main>
</template>
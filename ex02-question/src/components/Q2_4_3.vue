<script setup lang="ts">
import { reactive } from 'vue'

/*
a. 社員リストの定義
•	以下のオブジェクトを含む配列 employeeList を定義しているreactive部分を確認してください。
*/
const employeeList = reactive([
  { id: 101, name: '佐藤一郎', salary: 3500000, department: '営業部' },
  { id: 102, name: '鈴木二郎', salary: 3500000, department: '総務部' },
  { id: 103, name: '高橋三郎', salary: 5000000, department: '開発部' },
  { id: 104, name: '田中四郎', salary: 5500000, department: '営業部' },
  { id: 105, name: '伊藤五郎', salary: 4800000, department: '総務部' }
])
</script>

<template>
  <h1>演習2-4-3</h1>
  <hr>
  <!-- b. テーブルの作成（v-for の使用）
•	template 内の<table>と<thead>のソースコードを確認してください。-->

  <table class="table table-bordered w-auto">
    <thead class = "table-primary">
    <tr>
      <th>ID</th>
      <th>氏名</th>
      <th>年収</th>
      <th>部署</th>
    </tr>
    </thead>
    <tbody>
      <!-- tbody 内の tr タグに v-for を適用し、employeeList の各要素を表示してください。
　　　　　o	重要: :key 属性には必ず一意な id を指定してください。 -->
    <tr                >
      <td>  </td>  <!--id-->
      <td>  </td>  <!--name-->
      <td> 円</td> <!--salary-->
      <td>   </td> <!--department-->
    </tr>
    </tbody>
    </table>
</template>

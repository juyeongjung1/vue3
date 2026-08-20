<script setup lang="ts">
//b. ➀ vue から computed をインポートしてください。
import { reactive, computed } from 'vue'

//a. データ準備
//reactive の社員情報 employee にsalaryを追記している部分を確認してください。
const employee = reactive({
  name: '田中 太郎',
  department: '開発部',
  workLocation: '未設定',
  salary:250000 
})

/*b. 手取り額の算出
➁ 給与の 80% を手取り額として計算する算出プロパティ salaryTaxPlus を定義してください。
o	計算式: employee.salary * 0.8*/

const salaryTaxPlus = computed(() => {
  return employee.salary * 0.8
})

</script>

<template>
  <h1>演習2-3-3</h1>
  <hr>
  <h2>あなたの情報</h2>
  <p>氏名: {{ employee.name }}</p>
  <p>部署: {{ employee.department }}</p>
  <!-- c. 画面表示
   ➀	template に以下の要素を追記してください。
　　　　月給:  
　　　　推定手取り額: -->
  <p>月給:{{ employee.salary }} 円</p>
  <p>推定手取り額：{{ salaryTaxPlus }} 円</p>
  
  <hr>
  <!--➁クリックすると employee.salary が 10000 増える「昇給」ボタンのソースコードを確認してください。-->
  <button @click="employee.salary += 10000">昇給</button>
  
</template>

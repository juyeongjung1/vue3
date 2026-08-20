<script setup lang="ts">
import { reactive } from 'vue'
import Header from './Header.vue'
import Main from './Main.vue'
import SideMenu from './SideMenu.vue'
import Footer from './Footer.vue'

/*a. 親コンポーネントの実装（App_Q3_2.vue）
  ➀ script setup 内で、以下のデータを定義している部分を確認してください。
	o	定数 companyName: 値 'Trainocate inc.'
  o	リアクティブな配列 employeeList: 5名分の社員オブジェクト（id, name, salary, department）
*/

const companyName = 'Trainocate inc.'
const employeeList = reactive([
  { id: 101, name: '佐藤一郎', salary: 3500000, department: '営業部' },
  { id: 102, name: '鈴木二郎', salary: 3500000, department: '総務部' },
  { id: 103, name: '高橋三郎', salary: 5000000, department: '開発部' },
  { id: 104, name: '田中士郎', salary: 5500000, department: '営業部' },
  { id: 105, name: '伊藤五郎', salary: 4800000, department: '総務部' }
])


</script>

<template>
  <Header /> 
  <div class="container">
    <div class="row">
      <div class="col-md-3">
        <SideMenu /> 
      </div>
 <!-- ➁ <Main> タグと <Footer> タグを配置し、
      v-bind（:）を使って定義した変数をそれぞれのコンポーネントに渡してください。 -->
      <div class="col-md-9">
        <Main /> 
      </div>
    </div>
  </div>
  <Footer /> 
</template>
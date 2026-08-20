<script setup lang="ts">
import { ref } from 'vue'
import Header from './components/Header.vue'
//import Main from './components/Main.vue'
import SideMenu from './components/SideMenu.vue'
import Footer from './components/Footer.vue'

//4.3 c. ➀ Vue Router の RouterView コンポーネントをインポートしていることを確認してください。
import { RouterView } from 'vue-router'

//4.5 c. ➀　vue から provide をインポートしてください。
import { provide } from 'vue'

const companyName = 'Trainocate inc.'

// 社員データ(refでリアクティブに管理)
const employeeList = ref([
   { id: 101, name: '佐藤一郎', salary: 3500000, department: '営業部', photoUrl: '/images/101.png' },
  { id: 102, name: '鈴木二郎', salary: 3500000, department: '総務部', photoUrl: '/images/102.png' },
  { id: 103, name: '高橋三郎', salary: 5000000, department: '開発部', photoUrl: '/images/103.png' },
  { id: 104, name: '田中士郎', salary: 5500000, department: '営業部', photoUrl: '/images/104.png' },
  { id: 105, name: '伊藤五郎', salary: 4800000, department: '総務部', photoUrl: '/images/105.png' }
])

// 4.5 c. ➁ 定義済みの employeeList を、キー名 'employeeList' で provide してください。
provide('employeeList', employeeList)

</script>

<template>
  <Header /> 
  <div class="container">
    <div class="row">
      <div class="col-md-3">
        <SideMenu /> 
      </div>
      <div class="col-md-9">
        <!-- ➁ 3章で配置していた <Main ... /> コンポーネント（およびインポート文）を削除またはコメントアウトしてください。-->
        <!-- <Main :employeeList />   -->
       
        <!-- ➂ 代わりに、メインコンテンツが表示されるエリア（col-md-9 の div タグの中）に 
         <RouterView /> タグを配置してください。-->
         <RouterView/>
      </div>
    </div>
  </div>
  <Footer :companyName /> 
</template>
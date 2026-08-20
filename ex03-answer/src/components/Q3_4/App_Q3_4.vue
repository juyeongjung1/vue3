<script setup lang="ts">
import { reactive } from 'vue'
import Header from './Header.vue'
import EmployeeCard from './EmployeeCard.vue'
import SideMenu from './SideMenu.vue'
import Footer from './Footer.vue'

const companyName = 'Trainocate inc.'

// ➀ 社員データに photoUrl を追加している部分を確認してください。
const employeeList = reactive([
  { id: 101, name: '佐藤一郎', salary: 3500000, department: '営業部', photoUrl: '/images/101.png' },
  { id: 102, name: '鈴木二郎', salary: 3500000, department: '総務部', photoUrl: '/images/102.png' },
  { id: 103, name: '高橋三郎', salary: 5000000, department: '開発部', photoUrl: '/images/103.png' },
  { id: 104, name: '田中士郎', salary: 5500000, department: '営業部', photoUrl: '/images/104.png' },
  { id: 105, name: '伊藤五郎', salary: 4800000, department: '総務部', photoUrl: '/images/105.png' }
])

</script>

<template>
  <Header />
  <div class="container">
    <div class="row">
      <div class="col-md-3">
        <SideMenu />
      </div>
      <div class="col-md-9">
        <div class="row">
          <h2 class="mb-4">社員一覧</h2>
 <!-- ➁ v-for を使って <EmployeeCard> コンポーネントを繰り返し表示するように追記してください。
  　　　　　属性名は、employee にしてください。 -->
          <div class="col-md-3 mb-3" v-for="employee in employeeList" :key="employee.id">
            <EmployeeCard :employee="employee" />
          </div>
        </div>
      </div>
    </div>
  </div>
  <Footer :companyName />
</template>
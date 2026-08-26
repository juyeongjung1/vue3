<script setup lang="ts">
import { ref, reactive } from 'vue'
import Header from './Header.vue'
import Main from './Main.vue'
import SideMenu from './SideMenu.vue'
import Footer from './Footer.vue'

const companyName = 'Trainocate inc.'
const employeeList = reactive([
  { id: 101, name: '佐藤一郎', salary: 3500000, department: '営業部' },
  { id: 102, name: '鈴木二郎', salary: 3500000, department: '総務部' },
  { id: 103, name: '高橋三郎', salary: 5000000, department: '開発部' },
  { id: 104, name: '田中士郎', salary: 5500000, department: '営業部' },
  { id: 105, name: '伊藤五郎', salary: 4800000, department: '総務部' }
])
/*b. 親コンポーネントの実装（App_Q3_3.vue）
➀ 選択された社員名を保持するためのリアクティブ変数
（例: selectedEmployeeName）を ref で定義してください（初期値は空文字 ' '）*/


/*➁ 子から通知を受け取った時に実行する関数（例: handleSelect）を作成し、
  引数で受け取った名前をリアクティブ変数に代入してください。*/


</script>

<template>
  <div class="position-relative">
    <Header />
    <!--➃ 画面の右上に、選択された社員名を表示するエリア
      （選択中の社員: ...）を追加してください -->
    <div class="position-absolute top-0 end-0 p-3">
      選択中の社員: <strong>         </strong>
    </div>
  </div>
  <div class="container">
    <div class="row">
      <div class="col-md-3">
        <SideMenu />
      </div>
      <div class="col-md-9">
        
 <!-- ➂ <Main> タグにイベントリスナ（@select="..."）を追加し、作成した関数と紐付けてください。 -->
        <Main :employeeList="employeeList"/>
      </div>
    </div>
  </div>
  <Footer :companyName />
</template>

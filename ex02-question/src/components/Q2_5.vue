<script setup lang="ts">
import { ref, reactive } from 'vue'

// a. データの準備
// 選択された社員情報を表示するための変数 selectedInfo（初期値 ''）を ref で定義してください。


// employeeList は演習2.4.3と同様のデータを使います。
const employeeList = reactive([
  { id: 101, name: '佐藤一郎', salary: 3500000, department: '営業部' },
  { id: 102, name: '鈴木二郎', salary: 3500000, department: '総務部' },
  { id: 103, name: '高橋三郎', salary: 5000000, department: '開発部' },
  { id: 104, name: '田中士郎', salary: 5500000, department: '営業部' },
  { id: 105, name: '伊藤五郎', salary: 4800000, department: '総務部' }
])

/*b. 選択メソッドの実装（引数あり）
 selectEmployee(name) 関数を作成してください。引数として「氏名」受け取ります。 
 関数内で、selectedInfo.value に 選択した社員：${name}　という文字列を代入してください。
 ※文字列と変数を並べる時は、バッククォート(``)　で囲って、 `社員 ${変数名}`　の書き方で埋め込めます。*/



</script>

<template>
  <h1>演習2-5</h1>

  <!-- d. 結果の表示
   テーブルの上の <p> タグにselectedInfo の内容を表示してください。 -->
  <p class="fw-bold text-primary">        </p>
  
<!-- c. テーブルへのボタン追加
   thead に「操作」列を追加してください。
   tbody のtrに「選択」ボタンを追加し、@click イベントを設定してください。 -->

  <table class="table table-bordered w-auto">
    <thead class="table-dark">
      <tr>
        <th>ID</th>
        <th>氏名</th>
        <th>年収</th>
        <th>操作</th>
      </tr>
    </thead>
    <tbody>
     
      <tr v-for="emp in employeeList" :key="emp.id">
        <td>{{ emp.id }}</td>
        <td>{{ emp.name }}</td> 
        <td>{{ emp.salary }} 円</td>
        <td>
          <!-- ボタンにクリックイベントを付与し、氏名の引数付きでselectEmployeeメソッドを呼び出してください -->
          <button class="btn btn-outline-primary btn-sm" 
                                  > <!--　←ここにクリックイベントを付与-->
            選択
          </button>
        </td>
      </tr>
    </tbody>
  </table>
</template>

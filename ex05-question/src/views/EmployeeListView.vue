<script setup lang="ts">
import { ref, onMounted } from 'vue'
// 5.1 a. Axios のインポート
// ➀ script setup 内で、axios をインポートしてください。

// import axios from 'axios'
import { RouterLink } from 'vue-router'

// 社員の型定義
type Employee = {
  id: number
  password: string
  name: string
  salary: number
  location_name: string
}

const employees = ref<Employee[]>([])
const loading = ref(false) 
const error = ref<string | null>(null)
// 5.1 b. 全件取得関数の実装 (fetchEmployees)
const fetchEmployees = async () => {
  // fetchEmployees 関数を定義し、axios.get を使用して全社員情報を取得してください。
  // 利用 API: 1.B 全件取得 API (GET)
  // URL: http://localhost:3000/api/employees/
}

onMounted(() => {
  // 5.1 c. マウント時の処理
  // 画面初期表示時 (onMounted) に fetchEmployees 関数を実行してください。
  
})

// 5.1 d. 検索用変数の定義
// keyword を保持する ref 変数を定義してください（初期値は空文字）。


// 5.1 e. 検索機能の実装
// searchEmployees 関数を定義し、axios.get を使用して検索結果を取得してください。
// 利用 API: 1.A 検索 API (GET)
// URL: http://localhost:3000/api/employees/search?keyword=...
const searchEmployees = async () => {

}
</script>

<template>
  <div class="container mt-4">
    <h2>人事管理システム</h2>
    
    <!-- 検索フォームと新規登録ボタン -->
    <div class="d-flex justify-content-between mb-3">
      <div class="input-group w-50">
        <!-- 5.1 f. 双方向バインディング -->
        <!-- input タグと keyword 変数を双方向データバインディングしてください。 -->
        <input type="text" class="form-control" placeholder="氏名で検索">
        <button class="btn btn-primary" @click="searchEmployees">検索</button>
      </div>
      <RouterLink to="/employees/new" class="btn btn-success">新規登録</RouterLink>
    </div>

    <!-- ローディング・エラー表示 -->
    <div v-if="loading">読み込み中...</div>
    <div v-else-if="error" class="text-danger">{{ error }}</div>

    <!-- 社員一覧テーブル -->
    <table v-else class="table table-striped">
      <thead>
        <tr>
          <th>ID</th>
          <th>氏名</th>
          <th>給与</th>
          <th>勤務地</th>
        </tr>
      </thead>
      <tbody>
        <!-- 5.1 g. リストレンダリング -->
        <!-- v-for を使用して employees の内容を繰り返し表示してください。 -->
        <tr                          > <!--v-forを付与する-->
          <td>    </td> <!--emp.id-->
          <td>        <!--emp.name-->
            
            <!-- 5.1 h. 詳細リンク -->
            <!-- RouterLink を使用して、社員詳細画面（/employees/ID）へのリンクを作成してください。 -->
            
          </td>
          <td>    円</td> <!--emp.salary-->
          <td>     </td> <!--emp.location_name-->
        </tr>
      </tbody>
    </table>
  </div>
</template>

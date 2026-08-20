<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRoute, useRouter, RouterLink } from 'vue-router'
// 5.2 a. Axios のインポート
// script setup 内で、axios をインポートしてください。
// import axios from 'axios'

const route = useRoute()
const router = useRouter()

const id = Number(route.params.id)

// 型定義
type Employee = {
  id: number
  password: string
  name: string
  salary: number
  location_name: string
  image_path: string
}

const employee = ref<Employee | null>(null)

// 詳細取得
const fetchDetail = async () => {
  try {
    // 5.2 b. 詳細取得
    // axios.get を使用して、特定の社員情報を取得してください。
    // 利用 API: 2. 社員詳細取得 API (GET)
    // URL: http://localhost:3000/api/employees/ID/
  } catch (err) {
    alert('データ取得に失敗しました')
  }
}

// 削除処理
const deleteEmployee = async () => {
  if(!confirm('本当にこの社員データを削除してもよろしいですか？')) return
  // 5.2 c. 削除機能
  // ➀ axios.delete を使用して、特定の社員データを削除してください。
  // 利用 API: 5. 社員削除 API (DELETE)
  // URL: http://localhost:3000/api/employees/ID/
  // ➁ 削除完了後、一覧画面にリダイレクトさせるロジックも検討してください。
}

onMounted(() => {
  fetchDetail()
})
</script>

<template>
  <div class="container mt-4" v-if="employee">
    <h2>社員詳細</h2>
    <div class="card p-3">
      <!-- 画像表示エリア -->
      <!-- 5.2 d. 画像表示制御 -->
      <!-- image_path がある場合のみ <img> タグを表示してください。 -->
      <div v-if="employee.image_path" class="mb-3 text-center">
        <!-- 5.2 e. 画像パスのバインド -->
        <!-- src 属性に image_path をバインドしてください。 -->
        <img alt="社員写真" class="img-thumbnail" style="max-width: 200px;">
      </div>
      <div v-else class="mb-3 text-center text-muted">
        (写真なし)
      </div>

      <p><strong>ID:</strong> {{ employee.id }}</p>
      <p><strong>氏名:</strong> {{ employee.name }}</p>
      <p><strong>給与:</strong> {{ employee.salary }} 円</p>
      <p><strong>勤務地:</strong> {{ employee.location_name }}</p>
      <p><strong>パスワード:</strong> {{ employee.password }}</p>
      
      <div class="mt-3">
        <RouterLink to="/employees" class="btn btn-secondary me-2">戻る</RouterLink>
        <!-- 5.2 f. 編集リンク -->
        <!-- 編集画面（/employees/edit/ID）への RouterLink を作成してください。 -->
        <RouterLink to="/employees" class="btn btn-primary me-2">編集</RouterLink>
        <button class="btn btn-danger" @click="deleteEmployee">削除</button>
      </div>
    </div>
  </div>
  <div v-else class="container mt-4">
    <p>読み込み中、またはデータが見つかりません。</p>
    <RouterLink to="/employees" class="btn btn-secondary">戻る</RouterLink>
  </div>
</template>

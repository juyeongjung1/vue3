<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
// import axios from 'axios'

const route = useRoute()
const router = useRouter()
const id = Number(route.params.id)

const name = ref('')
const password = ref('')
const salary = ref<number | null>(null)
const location_name = ref('')
const image_path = ref('')

// 既存データの取得
const fetchEmployee = async () => {
  try {
    // 5.3 a. axios.get を使用してデータを取得し、各 ref 変数に代入してください。
    // URL: http://localhost:3000/api/employees/ID/ (GET 2. 社員詳細取得 API)
  } catch (err) {
    alert('データ取得エラー')
  }
}

// 更新処理
const updateEmployee = async () => {
// 5.3 b. 更新処理
// axios.put を使用してデータを更新してください。
// 利用 API: 4. 社員更新 API (PUT)
// URL: http://localhost:3000/api/employees/ID/
// 送信データ: name, password, salary, location_name, image_path
}

onMounted(() => {
  fetchEmployee()
})
</script>

<template>
  <div class="container mt-4">
    <h2>社員情報編集</h2>
    <!-- 5.3 c. フォーム送信 -->
    <!-- フォーム送信時（submit）に updateEmployee を実行するようにしてください。 -->
    <form @submit.prevent="">
      <div class="mb-3">
        <label>氏名</label>
        <!-- 5.3 d. バインディング -->
        <!-- 各 input タグに適切な v-model を設定してください。 -->
        <input type="text" class="form-control" v-model="name">
      </div>
      <div class="mb-3">
        <label>パスワード</label>
        <input type="text" class="form-control" v-model="password">
      </div>
      <div class="mb-3">
        <label>給与</label>
        <input type="number" class="form-control" v-model="salary">
      </div>
      <div class="mb-3">
        <label>勤務地</label>
        <input type="text" class="form-control" v-model="location_name">
      </div>
      
      <!--5.3 c　buttonのtypeをsubmitにしてください。-->
      <button class="btn btn-primary">保存</button>
    </form>
  </div>
</template>

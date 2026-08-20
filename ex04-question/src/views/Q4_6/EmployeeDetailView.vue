<script setup lang="ts">
import { inject, computed } from 'vue'
import type { Ref } from 'vue'
// d.　➀ useRoute（vue-router）をインポートしてください。

// 型定義
type Employee = {
  id: number
  name: string
  salary: number
  department: string
  photoUrl: string
}

//d. ➁ ここに、useRoute() を使って、現在のルート情報を取得してください。


//d. ➂ ここに、URLパラメータから ID を取得し、変数「id」に代入してください。
// ※文字列として取得されるため Number() で数値変換が必要です。
const id = 0; //0はダミーです。適宜書き換えてください。

// データを受け取る
const employeeList = inject('employeeList') as Ref<Employee[]>

// IDに一致する社員を検索（リアクティブにするためcomputedを使用）
const employee = computed(() => {
  return employeeList.value.find(emp => emp.id === id)
})
</script>

<template>
  <div class="p-3">
    <h2 class="mb-4">社員詳細</h2>

    <div v-if="employee" class="card" style="max-width: 800px;">
      <div class="row g-0 align-items-center">
        <div class="col-md-5 text-center bg-light">
          <img 
            :src="employee.photoUrl" 
            class="img-fluid rounded-start p-3" 
            style="max-height: 250px; object-fit: contain;"
            alt="顔写真"
          >
        </div>

        <div class="col-md-7">
          <div class="card-body">
            <h3 class="card-title mb-3 fw-bold border-bottom pb-2">
              {{ employee.name }}
            </h3>
            
            <div class="card-text fs-5 mb-4">
              <div class="mb-2">
                <span class="badge bg-secondary me-2">ID: {{ employee.id }}</span>
              </div>
              <div class="mb-1">
                <strong class="me-3">部署:</strong> {{ employee.department }}
              </div>
              <div>
                <strong class="me-3">給与:</strong> {{ employee.salary.toLocaleString() }} 円
              </div>
            </div>

            <div class="text-end">
              <RouterLink to="/Q4_6/employees" class="btn btn-outline-secondary">
                一覧に戻る
              </RouterLink>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div v-else class="alert alert-danger">
      該当する社員データが見つかりません。
    </div>
  </div>
</template>
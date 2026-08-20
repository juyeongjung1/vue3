<script setup lang="ts">
// ➀ 社員1名分の型定義（Employee）を行っていますので、確認してください。
type Employee = {
    id: number
    name: string
    salary: number
    department: string
    photoUrl: string // 画像URLが追加されました
}

// ➁ 親から employee という名前でデータを受け取るように defineProps を記述してください。


</script>

<template>
    <div class="card h-100 text-center shadow-sm">
        <div class="card-body">
 <!-- ➂ 以下の要素を配置してください。 -->
  <!-- 以下の顔写真（imgタグ）：src属性に props.employee.photoUrl をバインド -->
            <img                      class="mb-3 border" width="100" height="120" alt="顔写真">
　　　　　　　<!-- 以下に、propsからの社員名を表示 -->
            <h5 class="card-title fw-bold">                   </h5> 
            <!-- 以下に、propsからの部署名を表示 -->
            <p class="card-text text-secondary mb-3">           </p>

            <!-- 以下の「詳細を見る」ボタンは見た目だけでOK -->
            <button class="btn btn-outline-primary btn-sm">
                詳細を見る 
            </button>
        </div>
        <div class="card-footer small">
            <!-- 以下にpropsからの社員IDを表示 -->
            社員ID: 
        </div>
    </div>
</template>
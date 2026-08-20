<script setup lang="ts">
  // 商品単体の型定義
  type Product = {
    id: number;
    name: string;
    price: number;
    category: string;
  }

  // 【3.4 ➀】親から送信される「商品1件」を受け取ってください(型はProduct)
  const props = ''
</script>

<template>
  <div class="card h-100 text-center">
    <div class="card-header">       </div> <!-- 【3.4 ➁】ここにカテゴリを表示してください -->
    <div class="card-body">
      <h5 class="card-title">       </h5> <!-- 【3.4 ➂】ここに商品名を表示してください -->
      <p class="card-text text-primary fs-4">     円</p> <!-- 【3.4 ➃】ここに価格を表示してください -->
      <button class="btn btn-primary">詳細を見る</button><!--今は形だけ実装-->
    </div>
    <div class="card-footer text-muted">ID:        </div> <!-- 【3.4 ➄】ここにIDを表示してください -->
  </div>
</template>
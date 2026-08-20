<script setup lang="ts">
  // 商品単体の型定義
  type Product = {
    id: number;
    name: string;
    price: number;
    category: string;
  }

  // 親から「商品1件」を受け取る定義
  const props = defineProps<{ product: Product }>();
</script>

<template>
  <div class="card h-100 text-center">
    <div class="card-header">{{ props.product.category }}</div>
    <div class="card-body">
      <h5 class="card-title">{{ props.product.name }}</h5>
      <p class="card-text text-primary fs-4">{{ props.product.price }}円</p>
      <button class="btn btn-primary">詳細を見る</button><!--今は形だけ実装-->
    </div>
    <div class="card-footer text-muted">ID: {{ props.product.id }}</div>
  </div>
</template>
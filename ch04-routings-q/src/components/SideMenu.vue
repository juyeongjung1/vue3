<script setup lang="ts">
</script>

<template>
  <!--【4.4 ➀】 以下のa hrefの部分を、ルーティングによる画面切り替えリンクへ修正してください-->
  <div class="list-group">
    <a href="/"              class="list-group-item list-group-item-action" exact-active-class="active">ダッシュボード</a>
    <a href="/products"      class="list-group-item list-group-item-action" exact-active-class="active">商品一覧</a>
    <a href="/products/new"  class="list-group-item list-group-item-action" exact-active-class="active">新規登録</a>
  <!--【4.4 ➁】 Bootstrapのclassを除外することで、どんな変化があるのか確認してください。-->
  </div>
</template>

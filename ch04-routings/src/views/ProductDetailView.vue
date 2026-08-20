<script setup lang="ts">
import { useRoute } from 'vue-router'

// 現在のURLから、:id の部分を取得
const route = useRoute()
const id = Number(route.params.id)

// 本来は、APIへidを渡してデータを取得する処理が続きます
</script>

<template>
    <h2 class="mb-3">商品詳細</h2>
    <p>商品ID {{ id }} の詳細ページです。</p>

    <!-- 本来は、APIから取得した詳細データを表示するコードが入ります -->
</template>

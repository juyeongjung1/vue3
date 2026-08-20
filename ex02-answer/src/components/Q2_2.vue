<script setup lang="ts">
//a. タイトル変数の定義
// script setup 内で、定数 systemName を定義し、値 '社員管理システム' を代入してください。
const systemName = '社員管理システム'
</script>

<template>
  <h1>演習2-2</h1>
  <hr>
  <!-- b. 画面への表示
template 内で、マスタッシュ構文 {{ }} を使って systemName を h2 タグで表示してください-->
  <h2>{{ systemName }}</h2>
</template>

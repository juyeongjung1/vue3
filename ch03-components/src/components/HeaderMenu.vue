<script setup lang="ts">
//TypeScriptを使う場合、以下のように型の定義が必要
type HeaderData = {
  title: string
  user: string
}

// 親から受け取るpropsの定義
const props = defineProps<HeaderData>()
</script>

<template>
    <header class="bg-dark text-white p-3">
        <div class="row">
            <div class="col-md-6">
                <h1 class="h5 m-0">{{ props.title }}</h1>
            </div>
            <div class="col-md-6 text-end">
                <span class="small">ようこそ、{{ props.user }}さん</span>
            </div>
        </div>
    </header>
</template>

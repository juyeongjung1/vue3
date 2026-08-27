<script setup lang="ts">
// RouterLinkを使用するため、以下の行頭の「//」を外してください。
// import { RouterLink } from 'vue-router'
</script>

<template>
    <!-- a. RouterLink への置き換え -->
    <div class="list-group">
        <h2 class="fs-5 border-bottom pb-2 mb-3">メニュー</h2>

        <!-- ➀ <a> タグなどで書かれているメニュー項目を、<RouterLink> タグに変更してください。 -->
        <!-- ➁to 属性には、以下のパスを指定します。
	　　ダッシュボード: to="/Q4_4"
　　　　社員一覧: to="/Q4_4/employees" -->
        <!-- ➂ Bootstrapのクラス（list-group-item 等）はそのまま維持してください。 -->

        <a href="#" class="list-group-item list-group-item-action">
            ダッシュボード</a>

        <a href="#" class="list-group-item list-group-item-action">
            社員一覧</a>

        <!-- ➃	クリックされたメニューをハイライト表示するために、
     <RouterLink> に exact-active-class="active" 属性を追加してください。 -->
    </div>

</template>

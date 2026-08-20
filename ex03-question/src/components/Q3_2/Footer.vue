<script setup lang="ts">

//➀ script setup 内で、受け取るデータの型 FooterProps（companyName: 文字列）を定義してください。

//➁ defineProps を使用して、定義した型の Props を受け取れるようにしてください。

</script>

<template>
  <footer class="bg-secondary-subtle p-3 text-center">
    
<!-- ➂ 以下に、受け取った companyName を使ってコピーライトの会社名部分を表示してください。 --> 
    <p class="mb-0 fst-italic">                  All Rights Reserved</p>
  </footer>
</template>

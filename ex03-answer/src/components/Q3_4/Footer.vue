<script setup lang="ts">

//➀ script setup 内で、受け取るデータの型 FooterProps（companyName: 文字列）を定義してください。
type FooterProps = {
  companyName: string
}
//➁ defineProps を使用して、定義した型の Props を受け取れるようにしてください。
const props = defineProps<FooterProps>()
</script>

<template>
  <footer class="bg-secondary-subtle p-3 text-center">
    
<!-- ➂ template 内で、受け取った companyName を使ってコピーライトの会社名部分を表示してください。 --> 
    <p class="mb-0 fst-italic">{{ props.companyName }} All Rights Reserved</p>
  </footer>
</template>

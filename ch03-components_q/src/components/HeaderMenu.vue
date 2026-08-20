<script setup lang="ts">



type HeaderData = {

  //【3.2 ➄】　ここに、親(App.vue)から渡されたデータの型を定義して追加してください。

}

//【3.2 ➅】　親から受け取るpropsの定義を追加してください。型名は➄で定義したHeaderDataを使います。

</script>

<template>
    <header class="bg-dark text-white p-3">
        <div class="row">
            <div class="col-md-6"> <!--【3.2 ➆】以下の{{  }}の中に、ヘッダー名を入れてください }} -->
                <h1 class="h5 m-0">{{        }}</h1>
            </div>
            <div class="col-md-6 text-end">　<!--【3.2 ➇】以下の{{  }}の中に、ユーザー名を入れてください }} -->
                <span class="small">ようこそ、{{      }}さん</span>　
            </div>
        </div>
    </header>
</template>

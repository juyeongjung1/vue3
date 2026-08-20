import { createApp } from 'vue'
import App from './App.vue'

// 追加：BootstrapVueNext のプラグイン（必須）
import { createBootstrap } from 'bootstrap-vue-next/plugins/createBootstrap'

// 追加：必要なCSS
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue-next/dist/bootstrap-vue-next.css'

createApp(App)
    .use(createBootstrap()) // 改行し、追加
    .mount('#app')


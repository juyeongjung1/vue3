import { createApp } from 'vue'
import App from './App.vue'

import 'bootstrap/dist/css/bootstrap.css'
import router from './router' // 追加：ルーターのインポート

createApp(App)
    .use(router) // 追加：ルーターをアプリに登録
     .mount('#app')

// Vue Router の機能をインポート
import { createRouter, createWebHistory } from 'vue-router'

// 各ビューコンポーネントをインポート
import HomeView from '../views/HomeView.vue'
import NewProductView from '../views/NewProductView.vue'
import ProductDetailView from '../views/ProductDetailView.vue'
//【4.3 ➀】　ここにProductListViewをインポートしてください。


// ルート（URLとコンポーネントの対応表）を定義
const routes = [
  { path: '/', name: 'home', component: HomeView },
  { path: '/products/new', name: 'new-product', component: NewProductView },
  //【4.3 ➁】以下に /productsパスのルート情報を追加してください。


  //【4.6 ➀】以下のルート情報を確認してください。(:idによる動的ルーティング)
  { path: '/products/:id', name: 'product-detail', component: ProductDetailView },
]

// ルーターを作成
const router = createRouter({
  // ブラウザの履歴管理を有効に設定
  history: createWebHistory(),
  routes                        // 上で定義したルート情報を登録
})

// 他のファイル（main.tsなど）で使えるようにエクスポート
export default router

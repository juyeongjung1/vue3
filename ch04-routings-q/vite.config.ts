import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vite.dev/config/
export default defineConfig({
  //base: '/vueapp/',  // ← 本番配置先に合わせる
  plugins: [vue()]
})

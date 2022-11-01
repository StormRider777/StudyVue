import Vue from 'vue'
//修改插值 标签 main.js 引用 import Vue from "vue/dist/vue.js
// 插值标签  {{  以后由 v-text 代替,django项目 冲突,在VUE CLI 中 delimiters 无效
import App from './App.vue'

Vue.config.productionTip = false
import vrouter from "vue-router"
Vue.use(vrouter)
import router from "./router/index"

new Vue({
  el:'#app',
  render:(h) => h(App),
  router
})

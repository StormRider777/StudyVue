import Vue from 'vue'
//修改插值 标签 main.js 引用 import Vue from "vue/dist/vue.js
// 插值标签  {{  以后由 v-text 代替,django项目 冲突,在VUE CLI 中 delimiters 无效
import App from './App.vue'
Vue.config.productionTip = false

import "vx-easyui/dist/themes/material/easyui.css"
import "vx-easyui/dist/themes/icon.css"
import "vx-easyui/dist/themes/vue.css"
import local from "vx-easyui/dist/locale/easyui-lang-zh_CN"
import Easyui from "vx-easyui"

Vue.use(Easyui)


import vrouter from "vue-router"
Vue.use(vrouter)

new Vue({
  el:'#app',
  render:(h) => h(App),
})

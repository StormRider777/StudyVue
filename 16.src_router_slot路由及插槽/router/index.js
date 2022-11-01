import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'

import App from '../App'
import About from '../pages/About'
import WorkHome from "../pages/WorkPages/WorkHome"


export default new Router({
  mode:'hash',
  routes: [
    {
      path: '/about',
      name: 'about',
      component: About
    },
    {
      path: '/ywgl',
      name: 'ywgl',
      component: WorkHome
    }
  ],
})
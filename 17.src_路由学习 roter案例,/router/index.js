import Router from "vue-router"

import About from "../pages/About"
import Work from "../pages/Work"
import News from "../pages/News"
import Messages from "../pages/Messages"
import Detial from "../pages/Detail"
import test from "../pages/test"

const router = new Router({
    routes:[
        {
            path:'/about',
            components: {work:About},
            meta:{title:'关于'},
            beforeEnter(to,from,next){
                console.log(to.path,to.meta.title,'独享路由守卫,进入前')
                next()
            },
            /*只有前置,没有后卫
            afterEnter(to,from){
                console.log(to.path,to.meta.title,'独享路由守卫,进入后')
            }
            */
        },
        {
            path:'/test',
            name:'test',
            components:{work:()=>import("../pages/test.vue")},
            meta:{title:'登录',isauth:false}
        },
        {
            path:'/work',
            components:{work:Work},
            meta:{title:'工作'},
            children:[
                {
                    path:'news',
                    components:{detailview:News},
                    children:[
                        {
                            name:'xinwen',
                            path: 'detail',
                            component: Detial,
                            props(route){
                                return{id:route.query.id,title:route.query.title,cap:route.query.cap}
                            },
                            meta:{title:'新闻列表'},
                        }
                    ],
                    meta:{isauth:false,title:'新闻'},

                },
                {
                    path:'messages',
                    components:{detailview:Messages},
                    children:[
                        {
                            name:'xiaoxi',
                            path:'detail',
                            component:Detial,
                            props(route){
                                return{id:route.query.id,title:route.query.title,cap:route.query.cap}
                            },
                        }

                    ],
                    meta:{
                        isauth:false,
                        title:'信息'
                    },
                },
            ]
        },

    ]
})

router.beforeEach((to,from,next)=>{
    //console.log(to.meta)
    // var l=JSON.parse(localStorage.getItem('logininfo'))
    // console.log(l)
    // if (l){
    //     if (l.hasOwnProperty('islogin')){
    //         if (l.islogin){
    //             to.meta.islogin=l.islogin
    //             next()
    //         }else{
    //             next('/test')
    //         }
    //     }else{
    //         next('/test')
    //     }
    // }else{
    //     console.log('s')
    //     next('/test')
    // }
    next()
})
router.afterEach((to,from)=>{
    //console.log('后置路由')
    document.title=to.meta.title
})


export default router
<template>
    <div>
        <span v-text="n"></span>
        <ul>
            <li v-for="m in news" :key="m.id">
                <!--地址拼接 query查询
                <router-link :to="`/work/news/detail?cap=News&id=${n.id}&title=${n.title}`" v-text="n.title"></router-link>
                --->
                <!--对象写法-
                1.route.js 中 path 占位  /work/message/:id/:title
                2.:to="{name:'消息',params:{id:m.id,title:m.title}}" 不能用path
                3.子组件中 引用  $route.$params.id
                -->
                <router-link :to="{
                    name:'xinwen',
                    query:{
                        cap:'News',
                        id:m.id,
                        title:m.title
                    }
                    }"
                    v-text="m.title">

                </router-link>
                <input type="text" style="height: 30px">

            </li>
        </ul>
        <div>
            <router-view></router-view>
        </div>
    </div>

</template>

<script>
    export default {
        name: "News",
        data(){
            return{
                n:0,
                ntimer:'',
                news:[
                    {id:1,title:'新闻头条'},
                    {id:2,title:'地方热点'},
                    {id:3,title:'吃瓜群众'},
                    {id:4,title:'疫情通报'},
                ]
            }
        },
        activated(){  //路由激活时调用
            this.ntimer=setInterval(()=>{
                this.n++
            },100)
        },
        deactivated(){ //路由失活调用
            clearInterval(this.ntimer)
        },
        beforeRouteEnter(to,from,next){
            console.log('通过路由规则,进入组件调用:',to.path)
            next()
        },
        beforeRouteLeave(to,from,next){
            console.log('通过路由规则,离开组件调用:',to.path)
            next()
        }
    }
</script>

<style scoped>
ul{
    list-style-type: none;
    padding: 0;
    width: 100%;
}
li{
    height: 35px;
    font-size: 18px;
    display: block;
    width: 100%;
    line-height: 40px;
    padding-left: 10px;
}
    li:hover{
        background: skyblue;
        color: red;
    }
    a{
        text-decoration: none;
    }
</style>
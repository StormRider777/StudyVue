<template>
    <div>
        <ul>
            <li v-for="m in messages" :key="m.id">
                <router-link
                        v-text="m.title"
                        :to="{
                            name:'xiaoxi',
                            query:{
                                cap:'消息',
                                id:m.id,
                                title:m.title,
                            }
                        }">

                </router-link>
            </li>
            <div>
                <router-view></router-view>
            </div>
        </ul>
    </div>
</template>

<script>
    export default {
        name: "Messages",
        data(){
            return{
                messages:[
                    {id:1,title:'休假通知'},
                    {id:2,title:'公告文件'},
                    {id:3,title:'小道消息'},
                    {id:4,title:'通报'},
                    {id:5,title:'停产公告'},
                ]
            }
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
</style>
<template>
    <div>
        <div style="display: flex;justify-content: space-evenly;margin: 10px">
            <span><router-link to="/work/news">新闻</router-link></span>
            <span><router-link to="/work/messages">消息</router-link></span>
        </div>
        <hr>
        <div>
            <!--组件名  缓存  :include="['','']"  列表 如果没有 在体内的全部缓存-->
            <keep-alive >
               <router-view name="detailview"></router-view>
            </keep-alive>

        </div>
    </div>
</template>

<script>
    export default {
        name: "Work",
        components:{
        }
    }
</script>

<style scoped>
    span{
        display: block;
        background: lightgreen;
        width: 100px;
        height: 30px;
        line-height: 30px;
        text-align: center;
        border: 1px solid grey;
        border-radius: 5px;
    }
    span:hover{
        background: skyblue;
        color:red;
    }
    a{
        text-decoration: none;
    }
    a:visited{
        color: black;
    }
    a:hover{
        color: yellow;
    }

</style>
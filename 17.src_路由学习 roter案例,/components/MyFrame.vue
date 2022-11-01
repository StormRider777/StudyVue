<template>
    <div class="mainpage">
        <div class="banner">
            <Banner>
                <template>
                    <img src="../assets/logo.jpeg"  style="width: 30px;height: 30px;border-radius: 15px" alt="">
                </template>
            </Banner>
        </div>
        <div class="content">
            <div class="navmenu">
                <Navmenu></Navmenu>
            </div>
            <div class="workarea">
                <div class="workarea-work">
                    <keep-alive>
                        <router-view name="work"></router-view>
                    </keep-alive>

                </div>
                <div  class="workarea-msg">
                    <span v-text="curpath"></span>
                </div>
            </div>
        </div>

    </div>
</template>

<script>
    import Banner from "../components/Banner"
    import Navmenu from "../pages/NavMenu"
    export default {
        name: "MyFrame",
        components:{
            Banner,Navmenu
        },
        computed:{
            curpath(){
                return '当前路径:'+this.$route.fullPath
            }
        }
    }
</script>

<style scoped>
    .content{
        display: flex;
        justify-content: flex-start;
        width: 100%;
        height: 90%;
        padding: 0;
        overflow: hidden;
    }
    .navmenu{
        width: 100px;
        height: 100%;
        background: #1a1e21;
        border: 1px solid silver;
    }
    .workarea{
        width: 100%;
        height: 100%;
        background: seashell;
        border: 1px solid blue;
    }
    .workarea-work{
        width: 100%;
        height: 400px;
        overflow: auto;
    }
    .workarea-msg{
        max-width: 400px;
        height: 40px;
        line-height: 40px;
        display: inline-block;
        overflow: hidden;
        text-overflow:ellipsis;
    }

    .mainpage{
        width: 500px;
        height: 500px;
        border: 1px solid grey;
        border-radius: 5px;
        margin: 20px auto;
    }
    .banner{
        width: 100%;
        height: 50px;
        color: white;
        font-size: 20px;
        line-height: 50px;
        background: #122b40;
        padding-left: 10px;
    }
</style>
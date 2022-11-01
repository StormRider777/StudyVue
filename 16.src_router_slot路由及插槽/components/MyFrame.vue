<template>
    <div class="mainpage">
        <div class="banner">
            <Banner>
                <template>
                    <img src="../assets/logo.jpeg"  style="width: 30px;height: 30px;border-radius: 15px" alt="">
                </template>
            </Banner>
        </div>
    </div>
</template>

<script>
    import Banner from "../components/Banner"
    export default {
        name: "MyFrame",
        components:{
            Banner,
        }
    }
</script>

<style scoped>
    .mainpage{
        width: 500px;
        height: 500px;
        border: 1px solid grey;
        border-radius: 5px;
    }
    .banner{
        width: 100%;
        height: 50px;
        color: white;
        font-size: 20px;
        line-height: 20px;
        background: #122b40;
        padding-left: 10px;
    }
</style>
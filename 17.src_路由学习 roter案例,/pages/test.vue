<template>
    <div>

        <span v-text="myrandom" style="color: red;font-size: 30px"></span>
        <span>登录名:<input type="text" v-model="loginuser"></span>
        <span><button @click="login()">登录</button></span>
        <span><button @click="logout()">退出登录</button></span>

    </div>
</template>

<script>
    import {nanoid} from "nanoid"
    export default {
        name: "test",
        data(){
            return{myrandom:nanoid(),loginuser:'',islogin:''}
        },
        methods:{
            login(){
                localStorage.setItem('logininfo',JSON.stringify({user:this.loginuser,islogin:true}))
            },
            logout(){
                localStorage.clear()
            }
        }
    }
</script>

<style scoped>

</style>
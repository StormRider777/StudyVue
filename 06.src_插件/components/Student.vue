<template>
    <div>
        <h3 class="zt">名字:{{ name }}</h3>
        <h3>年龄:{{ age }}</h3>
        <h3>电话:{{tel}}</h3>
        <input type="text" v-fbind="tel"><br><br>
        <button @click="editdata()">修改名字</button>
    </div>
</template>

<script>
    export default {
        //delimiters:['{[',']}'],//不起作用
        name: "Student",
        data(){
           return{
               name:'欧阳飞狐',
               age:45,
               tel:'132015500',
           }
        },
        mixins:[hunhe]
    }
</script>

<style scoped>
    .zt{
        color:blue
    }
</style>
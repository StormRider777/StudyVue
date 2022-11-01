<template>
    <div>
        <h3 class="zt">名字:{{ name | myslice }}</h3>
        <h3>人数:{{ total }}</h3>
        <h3>电话:{{tel}}</h3>
        <button @click="hello()">修改名字</button>
    </div>
</template>

<script>
    export default {
        //delimiters:['{[',']}'],//不起作用
        name: "School",
        data(){
           return{
               name:'肥城一中高中三年级',
               total:2000,
               tel:'3303168',
           }
        },
    }
</script>

<style scoped>
    .zt{
        color:blue
    }
</style>
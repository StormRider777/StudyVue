<template>
    <div>

        <h4 class="zt">名称:{{name }}</h4> <br><br>
        <h4>地址:{{ address }}</h4> <br><br>
        <h4>人数:{{total}}</h4> <br><br>
        <button @click="add()">点击人数+1</button>
    </div>
</template>

<script>
    export default {
        //delimiters:['{[',']}'],//不起作用
        name: "School",
        data(){
           return{
            name:'石横镇中心小学',
            address:'肥城市石横镇左丘明路',
            total:1500
           }
        },
        methods:{
            add(){return this.total++}
        }
    }
</script>

<style scoped>
    .zt{
        color:blue
    }
</style>
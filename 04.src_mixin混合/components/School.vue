<template>
    <div>
        <h3 class="zt">名字:{{ name }}</h3>
        <h3>人数:{{ total }}</h3>
        <h3>电话:{{tel}}</h3>
        <button @click="editdata()">修改名字</button>
    </div>
</template>

<script>
    import{ hunhe} from './hunhe'
    export default {
        //delimiters:['{[',']}'],//不起作用
        name: "School",
        data(){
           return{
               name:'肥城一中',
               total:2000,
               tel:'3303168',
           }
        },
        mixins:[hunhe],
    }
</script>

<style scoped>
    .zt{
        color:blue
    }
</style>
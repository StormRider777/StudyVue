<template>
    <div>

        <h3 class="zt">姓名:{{ name }}</h3>
        <h3>年龄:{{ myAge }}</h3>
        <h3>电话:{{tel}}</h3>
        <button @click="add()">点击年龄+1</button>
    </div>
</template>

<script>
    export default {
        //delimiters:['{[',']}'],//不起作用
        name: "Student",
        data(){
           return{
            myAge:this.age,
           }
        },
        methods:{
            add(){return this.myAge++}
        },
        props:{
          name:{
              type:String,
              required:true
          },
          age:{
              type:Number,
              default:100
          },
          tel:{
              type:String,
              required: false
          }
        }
    }
</script>

<style scoped>
    .zt{
        color:blue
    }
</style>
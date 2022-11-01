<template>
    <div style="background: darkseagreen">
        <hr>
        <span v-text="cap" style="color: red"></span>:
        <button @click="goabout('Home')">回到关于页面</button>
        <hr>
        <ul style="list-style-type: none;padding: 5px;margin: 15px">
            <li>编号: <span v-text="id" style="color: blue"></span></li>
            <li>标题: <span v-text="title" style="color: blue"></span></li>
        </ul>
    </div>
</template>

<script>
    export default {
        name: "Detail",
        mounted(){
            //console.log(this.$route)
        },
        props:['id','cap','title'],
        methods:{
            goabout(c){
                alert('跳转到:'+c)
                this.$router.replace({
                    path:'/about'
                })
            }
        }

        /*
        * porps 接受参数
        * props(route){
        * return{id:route.query.id,title:route.query.title,cap:route.query.cap}
        * }
        * */
    }
</script>

<style scoped>
li{
    height: 30px;
}

</style>
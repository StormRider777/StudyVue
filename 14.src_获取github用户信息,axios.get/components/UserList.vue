<template>
    <div>
        <div class="container"
             style="width: 80%;height: 80%;
                max-height:60%;;min-width: 600px;
                margin: 5px auto;
                background:whitesmoke;border: 1px solid lightgrey;border-radius: 5px;
                font-size: 18px;overflow-y: auto;min-height: 500px">

            <div class="card"  v-for="user in info.users" :key="user.login"
                 style="width:100px;height: 150px;overflow: hidden;
                        text-overflow: ellipsis;float: left;margin-left: 5px;margin-top: 5px;border-radius: 5px;border: 1px solid lightgrey">
                <a :href="user.html_url"><img class="card-img-top"
                     :src="user.avatar_url" alt="Card image" style="width:100%">
                </a>
                <div class="card-body" style="text-align: center">
                    <p v-text="user.login" style="font-size: 12px"></p>
                    <!---p class="card-text" style="font-size: 12px">
                        Some example text some example text. John Doe is an architect and engineer
                    </p--->
                </div>
            </div>
            <div v-show="info.isfirst"> <h2> 欢迎使用Github用户信息查询</h2></div>
            <div v-show="info.isloading"> <h2>正在查询中....</h2></div>
            <div v-show="info.errormsg" v-text="info.errormsg"></div>


        </div>
    </div>
</template>

<script>
    export default {
        name: "UserList",
        data(){
            return{
                info:{
                    isfirst:true,
                    isloading:false,
                    errormsg:'',
                    users:[]
                }
            }
        },
        mounted() {
            this.$bus.$on('getusers',(obj)=>{
                this.info={...this.info,...obj}

            })
        }
    }
</script>

<style scoped>

</style>
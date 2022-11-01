<template>
    <div>
        <div class="container" style="width: 80%;height: 120px;margin: 10px auto;
        background:whitesmoke;border: 1px solid lightgrey;border-radius: 5px;
        font-size: 18px;overflow: hidden;min-width: 600px">
            <div>
                <h4>查询GitHub上的用户信息</h4>
                <hr>
                <div>
                    <tr>
                        <td width="80px">请输入:</td>
                        <td width="400px">
                            <input class='form-control' type="text" style="width: 100%;height: 30px;"  v-model="kw">
                        </td>
                        <td>
                            <button class="btn btn-success" style="width:100px;height: 32px" @click="getuser">
                            查询</button>
                        </td>
                    </tr>

                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from "axios"
    export default {
        name: "Search",
        data(){
            return{
                kw:'rose',
            }
        },
        methods:{
            getuser(){
                var res={isfirst:false,isloading: true,errormsg:'',users:[]}
                this.$bus.$emit("getusers",res)

                axios.get(`https://api.github.com/search/users?q=${this.kw}`)
                .then(response => {
                    var res={isfirst:false,isloading: false,errormsg:'',users:response.data.items}
                    this.$bus.$emit("getusers",res)
                })
                .catch(function (error) { // 请求失败处理
                    var res={isfirst:false,isloading: false,errormsg:error.message,users:[]}
                    this.$bus.$emit("getusers",res)
                })
            }
        }

    }
</script>

<style scoped>
    td{
        padding-left: 8px;
    }
</style>
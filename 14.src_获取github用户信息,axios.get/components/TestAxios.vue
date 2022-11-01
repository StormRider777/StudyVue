<template>

    <div>
        <div class="parentdiv">
            <pre>

                import axios from 'axios'
                axios.defaults.baseURL = 'https://api.apiopen.top'
                Vue.prototype.$axios = axios
                this.$axios({
                      method: 'get',
                      url: 'https://api.apiopen.top/getJoke',
                      params:{
                        page:1,
                        count:2,
                        type:'video'
                      }
                    })
                .then(res=>{
                      this.result = res.data.message
                    })
                .catch(error=>{
                        if (error.response) {
                            // 请求已发出，且服务器的响应状态码超出了 2xx 范围
                            console.log(error.response.data);
                            console.log(error.response.status);
                            console.log(error.response.headers);
                        } else if (error.request) {
                            // 请求已发出，但没有接收到任何响应
                            // 在浏览器中，error.request 是 XMLHttpRequest 实例
                            // 在 node.js 中，error.request 是 http.ClientRequest 实例
                            console.log(error.request);
                        } else {
                            // 引发请求错误的错误信息
                            console.log('Error', error.message);
                        }
                        console.log(error.config);


                    axios({
                      method: 'post',
                      url: '/user/12345',
                      data: {       //注意这里，get参数使用params，post参数使用data
                        firstName: 'Fred',
                        lastName: 'Flintstone'
                      }
                    })


                axios.defaults.baseURL = 'http://api.example.com';
                axios.defaults.headers.common['Authorization'] = AUTH_TOKEN;
                axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';

                function getUserAccount() {

                    return axios.get(‘/user/12345’);

                }

                function getUserPermissions() {

                    return axios.get(‘/user/12345/permissions’);

                }

                axios.all([getUserAccount(), getUserPermissions()])

                    .then(axios.spread(function (acct, perms) {

                        // Both requests are now complete

                }));

                axios({
                　　url: '接口地址',
                　　method: 'get/post',
                　　responseType: 'json', // 默认格式
                　　data: {
                　　　　"参数名" : "参数值"
                　　}
                }).then(function (response) {
                　　console.log(response);
                }).catch(function (error) {
                　　console.log(error);
                }）

                $.ajax({
                　　url: '接口地址',
                　　type: 'get/post',
                　　dataType: 'json',
                　　data: {
                　　　　"参数名" : "参数值"
                　　},
                　　success: function (response) {
                　　　　console.log(response)；
                　　}
                })

            </pre>


        </div>
    </div>
</template>

<script>

    export default {
        name: "TestAxios",

    }
</script>

<style scoped>
    .parentdiv{
        width: 400px;
        height:400px;
        border: 2px solid blue;
        display: grid;align-items: center;justify-content: center;
        /*align-items: center;
place-content: center;
         align-content:center;justify-items: center;align-content: center;*/



    }
    .childdiv{
        width: 50px;
        height: 50px;

        margin-left: 2px;
        margin-top: 2px;
        background: red;
    }

</style>
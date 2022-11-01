<template>
    <div>
        <div>
            <pre>
                sessionstorage  与localstorage 用法一样
                sessionstorage ,只用于当前浏览器,关闭浏览器消失
                localstorage  ,本地存储,除非自行操作清除,或重置浏览器,清理浏览器缓存,才清除.
                ===========================
                methods:{
                    savedata(){
                        localStorage.setItem('dwmc',this.dwmc)
                        localStorage.setItem('person',JSON.stringify(this.preson))
                    },
                    readdata(){
                        var s1=localStorage.getItem('dwmc')
                        console.log(s1)
                        var s2=localStorage.getItem('person')
                        console.log(JSON.parse(s2))
                        var e=document.getElementById("content_data")
                        e.innerHTML=s1+'  '+s2
                    },
                    delone(){
                        localStorage.removeItem('dwmc')
                        this.readdata()

                    },
                    clearall(){
                        localStorage.clear()
                    }
                }
            </pre>
        </div>
        单位名称: <input type="text" v-model="dwmc"><br><br>
        姓名: <input type="text" v-model="preson.name"> <br><br>
        证件号码: <input type="text" v-model="preson.cardid"><br><br>
        年龄: <input type="text" v-model="preson.age"><br><br>
        <button @click="savedata">保存</button>
        <button @click="readdata">读取</button><br><br>
        <button @click="delone">删除一个</button>
        <button @click="clearall">清除</button>
        <div id="content_data"></div>
    </div>

</template>

<script>
    import {nanoid} from "nanoid"
    export default {
        name: "local_session_storage",
        data(){
            return{
                dwmc:nanoid(),
                preson:{
                    name:nanoid(),
                    cardid:nanoid(),
                    age:Math.random()*100
                },
            }
        },
        methods:{
            savedata(){
                localStorage.setItem('dwmc',this.dwmc)
                localStorage.setItem('person',JSON.stringify(this.preson))
            },
            readdata(){
                var s1=localStorage.getItem('dwmc')
                console.log(s1)
                var s2=localStorage.getItem('person')
                console.log(JSON.parse(s2))
                var e=document.getElementById("content_data")
                e.innerHTML=s1+'<br>'+s2
            },
            delone(){
                localStorage.removeItem('dwmc')
                this.readdata()

            },
            clearall(){
                localStorage.clear()
            }
        }

    }
</script>

<style scoped>

</style>
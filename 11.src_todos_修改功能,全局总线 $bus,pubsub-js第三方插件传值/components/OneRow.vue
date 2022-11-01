<template>
    <tr>
        <td style="width: 10px">
            <input type="checkbox" :checked="todo.done" @change="todo.done=!todo.done" >
        </td>
        <td>
            <span>
                <input type="text"
                       v-show="todo.isedit"
                       id="textbox"
                       @blur="saverow($event,todo)"
                       :value="todo.todo"
                       ref="getfocus"
                       >
                <!---可以用 v-model 但是,功能收到很多局限,不然用,根据输入数据取更新data--->
            </span>
            <span v-text="todo.todo" v-show="!todo.isedit"></span>
        </td>
        <td style="width: 120px">
            <button id="delebtn" @click="delerow(todo.id)"> 删除</button>
            <button id="editbtn" @click="editrow(todo)" v-show="!todo.isedit"> 修改</button>
        </td>
    </tr>
</template>

<script>
    export default {
        name: "OneRow",
        props:['todo'],
        mounted(){

        },
        methods:{
            delerow(mid){
                //this.deleteone(mid)
                //向bus定位点 发送 数值 mid
                this.$bus.$emit("deleteone",mid)
            },
            editrow(row){
                if (!row.hasOwnProperty('isedit')){
                    this.$set(row,'isedit',true)
                }else{
                    row.isedit=true
                }
                //进入编辑状态 获取焦点
                this.$nextTick(function () {
                    this.$refs.getfocus.focus()
                })

            },
            saverow(e,row){
                row.isedit=false
                //此处虽然能够修改,但是不推荐,因为,todo是props传过来的,但变量是允许修改,因为是对象,
                //正确推荐的方法是用 this.$bus.$emit('updatedata',e.target.value)
                if (e.target.value.trim()){
                    row.todo=e.target.value.trim()
                }

                //this.$bus.$emit('updaterow',e.target.value)
            }
        }
    }
</script>

<style scoped>
    tr:hover{
        background: skyblue;
        color: red;
        border-radius: 5px;
        box-shadow: 0px 0px 2px 2px grey;
        font-weight: bold;
    }
    tr:hover #delebtn,tr:hover #editbtn{
        display:inline-block;
    }

    #delebtn{

        height: 35px;
        width: 55px;
        display: none;

    }
    #editbtn{
        height: 35px;
        width: 55px;
        display: none;
        margin-left: 5px;
    }
    #textbox{
        width: 90%;
        height: 28px;
        border-radius: 2px;
    }
    #textbox{
        box-shadow: 0px 0px 2px 2px darkgray;
    }
</style>
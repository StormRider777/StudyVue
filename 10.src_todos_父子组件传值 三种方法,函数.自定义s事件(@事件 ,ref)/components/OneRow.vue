<template>
    <tr>
        <td style="width: 10px">
            <input type="checkbox" :checked="todo.done" @change="todo.done=!todo.done">
        </td>
        <td>
            {{todo.todo}}
        </td>
        <td style="width: 60px">
            <button id="delebtn" @click="delerow(todo.id)"> 删除</button>
        </td>
    </tr>
</template>

<script>
    export default {
        name: "OneRow",
        props:['todo','deleteone'],
        methods:{
            delerow(mid){
                this.deleteone(mid)
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
    }
    tr:hover #delebtn{
        display: block;
    }
    #rowinfo{
        width:50%
    }
    #delebtn{
        height: 35px;
        width: 60px;
        display: none;
        margin: 0 auto;
    }
</style>
<template>
    <div>
        <table id="datalist" cellpadding="1" cellspacing="1">
            <!---thead>
                <tr><td style="width: 10px"></td><td width="98%">事项</td><td></td></tr>
            </thead--->
            <tbody>
                <OneRow v-for="todo in todos" :key="todo.id" :todo="todo"></OneRow>
            </tbody>
        </table>
    </div>
</template>

<script>
    import OneRow from "./OneRow"
    export default {
        name: "AllList",
        components:{
            OneRow,
        },
        props:['todos'],
        mounted() {
            //console.log('s:',this.deleteone())
        }

    }

</script>

<style scoped>
    thead{
        background: lightgrey;

    }
    tr{
        height: 35px;

    }
    td{
        border-radius: 5px;
    }
    #datalist{
        width: 100%;
        margin: 5px auto;
    }
</style>
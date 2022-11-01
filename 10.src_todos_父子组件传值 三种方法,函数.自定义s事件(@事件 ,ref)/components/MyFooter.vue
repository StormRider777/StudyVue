<template>
    <div v-show="totalrows>0">
        <span id='selectall'><input type="checkbox" v-model="tmpcheckall" @change="checkallrow(tmpcheckall)">已选 {{selectrows}} /总 {{totalrows}} 个</span>
        <button id="deleallbtn" @click="DelSelected()" :disabled="!selectrows>0">删除所选</button>
    </div>
</template>

<script>
    export default {
        name: "MyFooter",
        data(){
            return{
                tmpcheckall:false
            }
        },
        props:['selectrows','totalrows',"checkallrow","delselected"],
        methods:{
           DelSelected(){
               this.$emit("delselected")
           }
        }
    }

</script>

<style scoped>
    #selectall{
        margin-left: 5px;
        margin-top: 5px;
    }
    #deleallbtn{
        width: 120px;
        height: 35px;
        margin-left: 20px;

    }
</style>
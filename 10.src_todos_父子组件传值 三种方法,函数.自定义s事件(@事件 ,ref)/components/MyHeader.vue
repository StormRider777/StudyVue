<template>
    <div id="info_input_div">
        <input type="text" id="info_input" @keydown.enter="addrow" v-model.trim="tmpdata">
    </div>
</template>

<script>
    export default {
        name: "MyHeader",
        //props:['inputrow'],
        data(){
          return{tmpdata:''}
        },
        methods:{
            addrow(){
                if (this.tmpdata){
                    //this.inputrow(this.tmpdata)
                    this.$emit('inputrow',this.tmpdata)
                    this.tmpdata=""
                }else{

                }

            }
        }
    }
</script>

<style scoped>
    #info_input_div {
        width: 100%;
        margin: 5px auto;
        height: 35px;
        line-height: 35px;
        border-radius: 5px;

    }
    #info_input{
        border-radius: 5px;
        width: 98%;
        height: 30px;
        font-size: 25px;
    }
    #info_input:hover{
        box-shadow: 0px 0px 2px 2px lightskyblue;
    }
</style>
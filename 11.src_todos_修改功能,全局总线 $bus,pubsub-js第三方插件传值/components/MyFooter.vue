<template>
    <div v-show="totalrows>0">
        <span id='selectall'>
            <input type="checkbox"
                   :checked="totalrows===selectrows"
                   @change="ischeck()">
            已选 <span v-text="selectrows"></span>
            /总 <span v-text="totalrows"></span>个
        </span>
        <button id="deleallbtn" @click="DelSelected()" :disabled="!selectrows>0">删除所选</button>
    </div>
</template>

<script>
    export default {
        name: "MyFooter",

        props:['selectrows','totalrows'], //,"checkallrow","delselected"],使用自定义事件 @ 、ref 不用props
        data(){
          return{
              tmpcheck:false
          }
        },
        methods:{
           DelSelected(){
               this.$emit("delselected")  //发射到父组件的定位点.  @自定义事件---->方法
           },
           ischeck(){
               if (this.selectrows===this.totalrows){
                   this.tmpcheck=true
               }else{
                   this.tmpcheck=false
               }
               this.tmpcheck=!this.tmpcheck
               this.$emit("ischeckallrow",this.tmpcheck) //发射到父组件的定位点 ref---> 自定义事件
           },
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
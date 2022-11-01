<template>
  <div id="app">
    <div  id="maindiv">
      <div style="margin: 0px auto;width:50px;height: 50px;" >
          <img alt="Vue logo" src="./assets/logo.jpeg" style="width: 80%;height: 80%;border-radius: 50px">
      </div>
      <!--span v-text="msg"></span-->
      <div>
        <!--绑定函数的方法接受子组件传递来的数据-->
        <MyHeader :inputrow="addrow"></MyHeader>
        <hr>
        <div style="width: 100%;max-height: 300px;overflow-y: auto" id="datalistdiv">
        <!--使用全局事件总线,传递和接受参数.-->
        <AllList :todos="todos"></AllList>
        </div>
        <hr>
        <!--使用自定义事件 @事件名 、 ref=“事件名”--->
        <MyFooter :selectrows="selectrows" :totalrows="totalrows"
                  @delselected="deleteselectd"
                  ref="checkallrow"></MyFooter>

      </div>

      <hr>
      <span style="font-weight: bold"> <a href="javascript:void(0)" @click="displayhelpcode()">显示代码说明</a></span>
      <div v-text="scode" id="help" v-show="helpshow"
           style="overflow-y: scroll;max-height: 250px;width: 100%" >

      </div>
    </div>

  </div>
</template>

<script>
import AllList from "./components/AllList"
import MyHeader from "./components/MyHeader"
import MyFooter from "./components/MyFooter"
import {nanoid} from "nanoid"

export default {
  delimiters:["^^","^^"],
  name: 'App',
  components: {
    MyHeader,
    MyFooter,
    AllList,
  },
  data(){
    return{
      msg:'{[ 修改插值 标签 main.js 引用 import Vue from "vue/dist/vue.js" ',
      helpshow:false,
      todos:JSON.parse(localStorage.getItem('todos'))?JSON.parse(localStorage.getItem('todos')):[],
      scode:`<pre>
         ========================
         几个知识点
         ========================
            1.元素事件 参数 $event 例如:@click="func($event)"
            2.进入编辑状态,让当前编辑框获取焦点
              <input ref="getfocus"/>

                this.$nextTick(function () {
                    this.$refs.getfocus.focus()
                })
          =============================
          组件间传递数值==>全局事件总线
          =============================
          1.在main.js中设置启用全局事件总线
              new Vue({
                el:'#app',
                render: h => h(App),
                beforeCreate(){
                    Vue.prototype.$bus = this //安装全局事件总线，$bus就是当前应用的vm
                }
            })
            2.接受数值的组件引用总线设置接受定位点.
                mounted(){
                  // 绑定自定义事件
                  this.$bus.$on('自定义事件名', (接收参数)=>{
                    console.log('我是B组件，收到了数据', 接收参数);
                  })
                发出数据的组件定义.向总线发送事件,有总线getter setter进行自动更新
                 methods:{
                  // 触发事件,事件名不能重复
                  send(){
                    this.$bus.$emit('自定义事件名', 传递参数);
                  }
             3.销毁组件前,销毁总线接收点
                beforeDestroy() {
                  this.$bus.$off('自定义事件名')

          ===============================
          组件间传递数值===>消息订阅传递数据
          ===============================
          1.npm install pubsub-js
          2.import pubsub from 'pubsub-js'
          3.获取数据的 组件 ,设定 接收点()
              在data.methods 中设置一个 函数 myresdata(_,value){} _
              this.pubid=pubsub.subscribe('myrecive',this.myresdata)
          4.发送值的组件
              import pubsub from 'pubsub-js'
              需要传值的事件中 :
              pubsub.publish('myrecive',a,b,c)

          5.vue.beforeDestroy(){pubsub.unsubscribe(this.pubid)} 销毁消息
          ===================================
          组件间传递数值=====> 三种,函数法,自定义事件法,(分两种.ref  @自定义事件)
         =====================================
        一、通过父组件给子组件传递函数类型的props实现
        父组件：
        <Child :getChildInfo="getChildInfo"></Child>
        子组件：
        <btn @click="sendChildInfo"></btn>
        props: ['getChildInfo']
        sendChildInfo() {
            this.getChildInfo(数据);
        }

        二、通过父组件给子组件绑定自定义事件实现
        第一种方式：
        父组件：
        <child @haha="test"></child>

        子组件：
        <btn @click="send"></btn>

        send() {
            this.$emit('haha');
        }

        第二种方式：
        父组件：
        <child ref="xxx"></child>

        mounted() {
            this.$refs.xxx.$on('haha', this.test);
        }
        子组件：
        <btn @click="send"></btn>

        send() {
            this.$emit('haha');
        }
        注意：
        若想让自定义事件只能触发一次，可以使用once修饰符，或者$once方法。
        组件上也可以绑定原生DOM事件，需要使用native修饰符
        <Child @click.native="xxx"></Child>
        通过this.$refs.xxx.$on('haha', 回调)绑定自定义事件时，回调要么配置在methods中，要么用箭头函数，否则this的指向会出问题。
      </pre>`,

    }
  },
  computed:{
    totalrows:function () {
      return this.todos.length
    },
    selectrows:function () {
      var rs=this.todos.filter(r=>{return r.done})
      return rs.length
    }
  },
  methods:{
    deleteone(mid){
      this.todos=this.todos.filter((r)=>{return r.id!=mid})
    },
    addrow(v){
      this.todos.unshift({id:nanoid(),todo:v,done:false})
    },
    checkallrow(ischecked){
      this.todos.forEach(r=>{
        return r.done=ischecked
      })
    },
    deleteselectd(){
      this.todos=this.todos.filter((r)=>{return !r.done})
    },
    displayhelpcode(){
      this.helpshow=!this.helpshow
      var e=document.getElementById("datalistdiv")
      var he=document.getElementById("help")
      if (this.helpshow){
        e.style.maxHeight='150px'
        he.style.maxHeight='600px'

      }else{
        e.style.maxHeight='550px'
        he.style.maxHeight='250px'
      }
    },
  },
  mounted:function () {
    //ref 设置定位点,子组件发射过来,位置
    this.$refs.checkallrow.$on('ischeckallrow',this.checkallrow)

    //全局总线设置接受数据 定位点,绑定到deleteon函数处理
    this.$bus.$on('deleteone',this.deleteone)

  },
  watch:{
    todos:{
      deep:true,
      handler:function(nv,ov){
        localStorage.setItem('todos',JSON.stringify(nv))
      },
    },
    helpshow(nv,ov){
        //console.log('显示代码标志修改了',nv)
    }
  },
  beforeDestroy() {
    this.$bus.$off("deleteone")
  }
}
</script>

<style>
  #maindiv{
    width:500px;
    max-height: 750px;
    min-height: 400px;
    box-shadow: 0px 0px 2px 2px grey;
    border: 1px solid gray;
    margin: 5px auto;
    padding: 10px;
    /*overflow-y: scroll;*/
    border-radius: 5px;
    overflow-y: auto;
  }
  #help{
    white-space: pre-wrap;
    width:400px;
    margin: 10px auto;
  }
  a{
    color: black;
    text-decoration: none;
    float: right;
  }
  a:hover{
    display:ruby;
    color:yellow;
    background: grey;
  }
  a:visited{
    color:black;
  }
</style>

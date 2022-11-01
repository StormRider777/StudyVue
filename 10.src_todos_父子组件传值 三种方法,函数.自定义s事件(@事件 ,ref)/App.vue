<template>
  <div id="app">
    <div  id="maindiv">
      <div style="margin: 0px auto;width:100px;height: 100px;" >
          <img alt="Vue logo" src="./assets/logo.jpeg" style="width: 100%;height: 100%;border-radius: 50px">
      </div>
      <div>
        <MyHeader @inputrow="addrow"></MyHeader>
        <hr>
        <AllList :todos="todos" :deleteone="deleteone"></AllList>
        <hr>
        <MyFooter :selectrows="selectrows" :totalrows="totalrows" @delselected="deleteselectd" :checkallrow="checkallrow"></MyFooter>

      </div>

      <hr>
      <div v-text="scode" id="help" >

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
  name: 'App',
  components: {
    MyHeader,
    MyFooter,
    AllList,
  },
  data(){
    return{
      todos:JSON.parse(localStorage.getItem('todos'))?JSON.parse(localStorage.getItem('todos')):[],
      scode:`<pre>
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
    }

  },
  watch:{
    todos:{
      deep:true,
      handler:function(nv,ov){
        localStorage.setItem('todos',JSON.stringify(nv))
      }
    }
  },

}
</script>

<style>
  #maindiv{
    width:500px;
    max-height: 700px;
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
</style>

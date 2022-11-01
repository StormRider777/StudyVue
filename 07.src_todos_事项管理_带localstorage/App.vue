<template>
  <div id="app">
    <div  id="maindiv">
      <div style="margin: 0px auto;width:100px;height: 100px;" >
          <img alt="Vue logo" src="./assets/logo.jpeg" style="width: 100%;height: 100%;border-radius: 50px">
      </div>
      <div>
        <MyHeader :inputrow="addrow"></MyHeader>
        <hr>
        <AllList :todos="todos" :deleteone="deleteone"></AllList>
        <hr>
        <MyFooter :selectrows="selectrows" :totalrows="totalrows" :delselected="deleteselectd" :checkallrow="checkallrow"></MyFooter>

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
      todos:JSON.parse(localStorage.getItem('todos'))?JSON.parse(localStorage.getItem('todos')):[]
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
</style>

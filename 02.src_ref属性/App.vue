<template>
  <div id="app">

    <img alt="Vue logo" src="./assets/logo.jpeg"
         style="width:100px;height: 100px;border-radius: 50px">
    <h2 ref="title">学习Vue</h2>
    <h2 ref="hy" v-text="msg" style="color:red">学习Vue</h2>
    <button @click="outref">console输出ref属性</button>
    <br>
    <School ref="sch" id="sch"></School>

  </div>
</template>

<script>
import School from "./components/School"
export default {
  name: 'App',
  components: {
    School:School,
  },
  data(){
    return{
      msg:'中国共产党第二十次代表大会'
    }
  },
  methods:{
    outref:function () {
      console.log('title',this.$refs.title)
      console.log('hy',this.$refs.hy)
      console.log('sch--ref方法',this.$refs.sch)
      console.log('sch--DOM方法',document.getElementById('sch'))
      console.log('$refs',this.$refs)

    }
  }
}
</script>

<style>

</style>

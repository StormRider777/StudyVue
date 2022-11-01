<template>
  <div id="app">
  <MyFrame></MyFrame>
  </div>
</template>

<script>
  import MyFrame from "./components/MyFrame"
  export default {
    name: 'App',
    components: {
      MyFrame,
    },
    computed:{

    },
    methods:{

    },
    beforeCreate(){

    },
    mounted(){
      //this.$router.islogin=false
    }
  }
</script>

<style>

</style>

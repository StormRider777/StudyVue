<template>
  <div id="app">

  </div>
</template>

<script>

  export default {
    name: 'App',
    components: {

    },
    computed:{

    },
    methods:{

    },
    beforeCreate(){

    },
    mounted(){
    }
  }
</script>

<style>
  #mainpage{
    width: 100%;
    min-height: 100vh;
    min-width: 800px;
    min-height: 550px;
  }
  #headarea{
    width: 100%;
    height: 8vh;
    min-height: 50px;
    max-height: 60px;
    line-height: 8vh;
    background: #122b40;
    color:white;
    display:grid;
    align-items: center;

  }
  #centarea{
    width: 100%;
    height: 85vh;
    min-height: 460px;
    display: flex;
  }
  #myfootarea{
    width: 100%;
    height: 15vh;
    background: #8c8c8c;
    color: ghostwhite;
    font-size: 18px;
    min-height: 50px;
    max-height: 50px;
    display: flex;
    justify-content: center;
    align-items: center;
  }
</style>

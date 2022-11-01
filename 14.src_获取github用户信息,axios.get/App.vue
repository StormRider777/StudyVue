<template>
  <div id="app">
    <div  id="maindiv">
      <div style="margin: 0px auto;width:50px;height: 50px;" >
          <img alt="Vue logo" src="./assets/logo.jpeg" style="width: 80%;height: 80%;border-radius: 50px">
      </div>
    </div>
    <div style="margin:0px auto;width: 500px;height: 500px">
      <TestAxios></TestAxios>
    </div>

    <div>
      <Search></Search>
      <UserList></UserList>
    </div>
      <!--span v-text="msg"></span-->
  </div>
</template>

<script>
import Search from "./components/Search"
import UserList from "./components/UserList"
import TestAxios from "./components/TestAxios"
export default {
  name: 'App',
  components: {
    Search,UserList,TestAxios
  },
}

</script>

<style>

</style>

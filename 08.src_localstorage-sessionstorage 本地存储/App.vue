<template>
  <div id="app">
    <div style="margin: 0px auto;width:100px;height: 100px;" >
      <img alt="Vue logo" src="./assets/logo.jpeg" style="width: 100%;height: 100%;border-radius: 50px">
    </div>
    <Stor></Stor>
  </div>
</template>

<script>

import local_session_storage from "./components/local_session_storage"

export default {
  name: 'App',
  components: {
     Stor:local_session_storage
  },

}
</script>

<style>

</style>

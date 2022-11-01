<template>
  <div id="app">
    <Test/>
  </div>
</template>

<script>

import {nanoid} from "nanoid"
import Test from "./components/Test"

export default {
  name: 'App',
  components:{
    Test
  }
}
</script>

<style>

</style>

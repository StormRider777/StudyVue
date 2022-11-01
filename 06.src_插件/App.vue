<template>
  <div id="app">

    <img alt="Vue logo" src="./assets/logo.jpeg"
         style="width:100px;height: 100px;border-radius: 50px">
    <School></School>
    <hr>
    <Student></Student>
  </div>
</template>

<script>

import Student from "./components/Student"
import School from './components/School'

export default {
  name: 'App',
  components: {
    Student:Student,
    School:School,
  },
}
</script>

<style>

</style>

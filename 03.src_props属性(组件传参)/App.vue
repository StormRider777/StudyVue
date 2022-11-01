<template>
  <div id="app">

    <img alt="Vue logo" src="./assets/logo.jpeg"
         style="width:100px;height: 100px;border-radius: 50px">
    <Student name="隔壁老王" tel="15689745001" :age="48"></Student>
    <hr>
    <Student name="西门吹雪" tel="8597001" :age="35"></Student>
  </div>
</template>

<script>
import Student from "./components/Student"
export default {
  name: 'App',
  components: {
    Student:Student,
  },
}
</script>

<style>

</style>

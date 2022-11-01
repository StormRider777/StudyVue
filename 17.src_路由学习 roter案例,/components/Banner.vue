<template>
    <div>
        <slot></slot>
        这是Router练习系统 1.0
        <button @click="goback()">后退</button>
        <button @click="goforward()">前进</button>
    </div>
</template>

<script>
    export default {
        name: "Banner",
        methods:{
            goback(){
                this.$router.back()
            },
            goforward(){
                this.$router.forward()
            }
        }
    }
</script>

<style scoped>

</style>
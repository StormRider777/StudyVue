<template>
    <div>
        总计藏书:
        <span v-text="total" style="color: darkmagenta"></span>
        册
        <button class="btn btn-primary"
                style="margin-bottom: 5px" @click="reloaddata()">恢复初始值</button>
    </div>
</template>

<script>
    export default {
        name: "Title",
        props:['total','reload'],
        methods:{
            reloaddata(){
                this.reload()
            }
        }

    }
</script>

<style scoped>

</style>
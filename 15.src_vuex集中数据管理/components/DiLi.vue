<template>
    <div>
        <div class="container">
            <div v-text="dili.title" class="bt"></div>
            <div>
                <img :src="dili.img" alt="">
            </div>
            <div class="data-table">
            <table class="table table-hover">
                <tr v-for="r in dili.lists" :key="r.id">
                    <td>《<span  v-text="r.name"> </span>》</td>
                </tr>
            </table>

            </div>
            <div style="display: flex;justify-content: flex-end;padding-right: 10px">
                共计:
                <span v-text="dili.lists.length" style="color: red"></span>
                册
            </div>
            <slot :msg="msg"></slot>
            <slot :msg="age"></slot>
            <slot name="dili"></slot>
        </div>
    </div>
</template>

<script>
    import {mapState} from 'vuex'
    export default {
        name: "DiLi",
        data(){
            return{
                msg:'我来自子组件插槽数据',
                age:100000,
            }
        },
        computed:{
            dili(){
                return this.$store.state.books.dili
            }
            /*...mapState([{dili:'dili'}])*/
        },
        mounted() {

        },
    }

</script>

<style scoped>

</style>
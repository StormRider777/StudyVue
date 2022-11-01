<template>
     <div>
        <div class="container">
            <div v-text="xiaoshuo.title" class="bt"></div>
            <div>
                <img :src="xiaoshuo.img" alt="">
            </div>
            <div class="data-table">
            <table class="table table-hover">
                <tr v-for="r in xiaoshuo.lists" :key="r.id">
                    <td>《<span  v-text="r.name"> </span>》</td>
                </tr>
            </table>

            </div>
            <div style="display: flex;justify-content: flex-end;padding-right: 10px;">

                共计:
                <span v-text="xiaoshuo.lists.length" style="color: red"></span>
                册
            </div>
            <slot name="xiaoshuo"></slot>
        </div>
    </div>
</template>

<script>
    export default {
        name: "XiaoShuo",
        computed:{
            xiaoshuo(){
                return this.$store.state.books.xiaoshuo
            }
        }
    }
</script>

<style scoped>

</style>
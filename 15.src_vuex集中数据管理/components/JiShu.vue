<template>
     <div>
        <div class="container">
            <div v-text="jishu.title" class="bt"></div>
            <div>
                <img :src="jishu.img" alt="">
            </div>
            <div class="data-table">
            <table class="table table-hover">
                <tr v-for="r in jishu.lists" :key="r.id">
                    <td>《<span  v-text="r.name"> </span>》</td>
                </tr>
            </table>

            </div>
            <div style="display: flex;justify-content: flex-end;padding-right: 10px">
                共计:
                <span v-text="jishu.lists.length" style="color: red"></span>
                册
            </div>
            <slot name="jishu"></slot>
        </div>
    </div>
</template>

<script>
    export default {
        name: "JiShu",
        computed:{
            jishu(){
                return this.$store.state.books.jishu
            }
        }
    }
</script>

<style scoped>

</style>
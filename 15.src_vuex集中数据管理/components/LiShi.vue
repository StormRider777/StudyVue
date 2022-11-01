<template>
     <div>
        <div class="container">
            <div v-text="lishi.title" class="bt"></div>
            <div>
                <img :src="lishi.img" alt="">
            </div>
            <div class="data-table">
            <table class="table table-hover">
                <tr v-for="r in lishi.lists" :key="r.id">
                    <td>《<span  v-text="r.name"> </span>》</td>
                </tr>
            </table>

            </div>
            <div style="display: flex;justify-content: flex-end;padding-right: 10px">
                共计:
                <span v-text="lishi.lists.length" style="color: red"></span>
                册
            </div>
            <slot name="lishi"></slot>
        </div>
    </div>
</template>

<script>
    export default {
        name: "LiShi",
        computed:{
            lishi(){
                return this.$store.state.books.lishi
            }
        }
    }

</script>

<style scoped>

</style>
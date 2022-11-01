<template>
  <div id="app">
    <div id='content'>

      <div id='content_title'>
        <!---->
        getter获取放大数:<span v-text="zje"></span>
        <Title :reload="reload" :total="total" >

        </Title>
      </div>
      <div id="content_content" >
        <DiLi>
            <template v-slot:dili>
              <div style="display: flex;justify-content: center;margin: 0 auto">
                <button class="btn btn-success" @click="add('dili')">随机增一个</button>
                <button class="btn btn-warning" @click="dele('dili')">随机减一个</button>
              </div>
            </template>
            <template scope="{msg}">
              <span v-text="msg"></span>
            </template>
        </DiLi>

        <LiShi>
          <template v-slot:lishi>
            <div style="display: flex;justify-content: center;margin: 0 auto">
              <button class="btn btn-success" @click="add('lishi')">随机增一个</button>
              <button class="btn btn-warning" @click="dele('lishi')">随机减一个</button>
            </div>
          </template>
        </LiShi>
        <XiaoShuo>
            <template v-slot:xiaoshuo>
              <div style="display: flex;justify-content: center;margin: 0 auto">
                <button class="btn btn-success" @click="add('xiaoshuo')">随机增一个</button>
                <button class="btn btn-warning" @click="dele('xiaoshuo')">随机减一个</button>
              </div>
            </template>
        </XiaoShuo>
        <JiShu>
          <template v-slot:jishu>
              <div style="display: flex;justify-content: center;margin: 0 auto">
                <button class="btn btn-success" @click="add('jishu')">随机增一个</button>
                <button class="btn btn-warning" @click="dele('jishu')">随机减一个</button>
              </div>
            </template>
        </JiShu>

      </div>
    </div>
  </div>
</template>

<script>
  import DiLi from "./components/DiLi"
  import LiShi from "./components/LiShi"
  import XiaoShuo from "./components/XiaoShuo"
  import JiShu from "./components/JiShu"
  import Title from "./components/Title"

  import {nanoid} from "nanoid"
  import {defaultbooks_data} from "./store/defaultdata"
  export default {
    name: 'App',
    components: {
      DiLi,LiShi,XiaoShuo,JiShu,Title
    },
    computed:{
      total(){
        return this.$store.state.books.jishu.lists.length+
                this.$store.state.books.dili.lists.length+
                this.$store.state.books.lishi.lists.length+
                this.$store.state.books.xiaoshuo.lists.length
      },
      zje(){
        return this.$store.getters.JE
      },
    },
    methods:{
      add(var_mod){
        var book={id:nanoid(),name:"随机_"+Math.floor(Math.random()*100).toString()+"书",img:''}
        var data={f_mod:var_mod,book:book}
        this.$store.dispatch('add',data)
      },
      dele(var_mod){
        var book={}
        var data={f_mod:var_mod,book:book}
        this.$store.dispatch('dele',data)
      },
      reload(){
        this.$store.commit('Reloaddefault')
      }
    },
    beforeCreate(){
      if (JSON.parse(localStorage.getItem('mybooks'))){
        this.$store.dispatch('loaddata','')
      }else{
        this.reload()
      }
    },
    mounted(){

    }
  }

</script>

<style>
    #app{
      display: flex;
      justify-content:space-around;
      align-items: center;
    }
    #content{
      height: 800px;
    }
    #content_title{
      width: 80%;background: darkgray;border-radius: 10px;
      color: white;margin: 15px auto;border: 1px solid grey;
      line-height: 40px;font-size: 30px;
      text-align: center;
      display: flex;
      flex-wrap: wrap;
      justify-content: space-around;

    }
    #content_content{
      display: flex;
      flex-wrap: wrap;
      width: 100%;
      height: 90%;
      justify-content: space-around;
    }

  .container{
    margin: 10px auto;
    width: 90%;
    height: 400px;
    border: 1px solid gray;
    border-radius: 5px;
    box-shadow: 0px 0px 4px 4px grey;
  }


  img{
    width: 100%;
    height: 120px;
  }
  .bt{
    border: 1px solid grey;
    text-align: center;
    line-height: 25px;
    font-size: 20px;
    width: 95%;
    margin: 5px auto;
    height: 25px;
    background: #843534;
    color: white;
 }
  .data-table{
    margin: 8px auto;
    height: 160px;
    overflow-y: auto;
    border: 1px solid darkgray;
  }
  tr{
    height: 22px;
  }
  button{
    width: 90px;
    margin-right: 10px;
  }
</style>

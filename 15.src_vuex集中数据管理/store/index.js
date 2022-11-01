import Vue from "vue"
import Vuex from "vuex"
import {nanoid} from "nanoid"
Vue.use(Vuex)
import {defaultbooks_data} from "./defaultdata"
//console.log('@@:',defaultbooks_data,'$$$:',localStorage.getItem('defaultbooks_data'))
export default new Vuex.Store({
    state:{
      books: {
          dili:{title:'',img:'',lists:[]},
          lishi:{title:'',img:'',lists:[]},
          xiaoshuo:{title:'',img:'',lists:[]},
          jishu:{title:'',img:'',lists:[]},

      }
    },
    actions:{
        add(content,value){
            /*
            此处应从vue中传来的简单数据 进行 搜索 获取,等筛选,过滤等..然后校验等,然后把正确的无误的数据提交给
            mutations
            content 是mini版的vuex,携带了基本功能及数据 value 是请求数据 ,此处不建议修改数据
            */
            var obj=content.state.books[value.f_mod].lists
            //console.log('actions.add:',obj,typeof(obj))
            /*obj.unshift(value.book)*/ //可以添加数据
            if (obj.length>8){
              alert('数据检验不合法,终止提交,不能超过8条')
              return false
            }
            content.commit('ADD',value)
        },
        dele(content,value){
            var obj=content.state.books[value.f_mod].lists
            //console.log('actions.add:',obj,typeof(obj))
            /*obj.unshift(value.book)*/ //可以添加数据
            if (obj.length<1){
              alert('已经空空如也了.不能再减了')
              return false
            }
            content.commit('DELE',value)
        },
        loaddata(content,yn){
            content.commit('LoadData')
        },
    },
    mutations:{
        ADD(state,value){
            var book=value.book
            var f_mod=value.f_mod
            /*console.log(f_mod,state.books[f_mod])*/
            var books=state.books[f_mod].lists.unshift(book)
            books=state.books
            localStorage.setItem('mybooks',JSON.stringify(books))
        },
        DELE(state,value){   //随机删除
            var f_mod=value.f_mod
            var books=state.books[value.f_mod].lists
            var rno=Math.floor(Math.random()*books.length)
            books.splice(rno,1)
            localStorage.setItem('mybooks',JSON.stringify(state.books))
        },
        LoadData(state){
            state.books=JSON.parse(localStorage.getItem('mybooks'))
        },
        Reloaddefault(state,value){
            state.books=JSON.parse(JSON.stringify(defaultbooks_data))
            localStorage.setItem('mybooks',JSON.stringify(state.books))
        },
    },
    getters:{
        JE(state,value){
            //console.log(state,value)
            return state.books.dili.lists.length*100
        }

    },
    modules:{},
})



/*
* mapMutations
* mapGetters
* mapActions
* mapState
* */

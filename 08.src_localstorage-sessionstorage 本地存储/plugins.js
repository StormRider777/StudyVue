export default {  //export default = const plugin=
    install(Vue,m,n){
        console.log(Vue)
        Vue.filter('myslice',function (value) {
            return value.slice(0,4)
        })
        Vue.directive('fbind',{  //自定义指令
            bind(e,b) {
                e.value=b.value
            },
            inserted(e,b){
                e.focus()
            },
            update(e,b){
                e.value=b.value
                e.focus()
            }
        })
        Vue.mixin({
            methods:{
                editdata(){
                    this.name=this.name+' '+'Edited'
                }
            },
            data(){
                return{
                    x:1000,
                    y:2000,
                }
            }
        })
        Vue.prototype.hello=()=>{alert('hello word')}
    }
}
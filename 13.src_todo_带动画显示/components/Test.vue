<template>
    <div>
        <div style="width: 100%;margin: 0 auto;border-bottom: 2px dotted gray">
            <div id="mydiv1">
                <img id="myimg" src="../assets/logo.jpeg" alt="" >
            </div>
        </div>
        <div id="mywork" style="margin: 10px auto;width:500px;height: 500px;
                        border: 1px solid gray;box-shadow: 0px 0px 3px 3px grey;
                        border-radius: 5px;overflow-y: auto">
            <h3>这是我的工作区页面</h3>
            <hr>

            <pre style="word-wrap:break-word">
                ===================
                vue 的动画
                ===================
                1.可用css自定义动画,
                   #mydiv1{
                        /*background: linear-gradient(to right,yellowgreen,darkolivegreen,green,lightgreen,green,darkolivegreen,yellowgreen);*/
                        position:relative;
                        animation:mymove1 10s linear infinite ; // 设置动画名 时间 速度 是否循环
                    }
                    #myimg{

                        animation:mymove2 10s linear infinite ;
                    }
                    @keyframes mymove1{
                        0%   {top:0px;left:5%}
                        50%  {top:0px;left: 90%;transform:rotate(720deg)}  // transform旋转.rotate 度数
                        100% {top:0px;left:5%;transform:rotate(-720deg)}
                    }
                    @keyframes mymove2{
                        0%   {transform:rotateY(0deg)}
                        50%  {transform:rotateY(720deg)} //垂直方向的旋转.
                        100% {transform:rotateY(-720deg)}
                    }
                2.VUE动画
                模板中:
                    <transition appear>
                        <div ></div>
                    </transition>
                    transition group --多个元素时 里面的元素 key='1' ....

                    /*< s tyle>
                        v-enter{ transform: translateX(-100%)} 进入的起点
                        v-enter-active{

                            animation: mymove 1s linear
                        }进入的过程
                        v-enter-to {transform: translateX(0)}进入的终点

                        v-leave  v-leave-active v-leave-to
                     < /  tyle>*/

                3.引入第三方动画库

            </pre>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Test",
        data(){
            return{
              m_left:'0px',
            }
        },
    }


</script>

<style scoped>
    #mywork{
        animation: workdiv 0.5s linear;
    }
    @keyframes workdiv {
        0% {margin-left: -600px;}
        50% {margin-left: 0px;}
        100% {margin-left: 500px}
    }


    #mydiv1{
        width: 100px;height:100px;
        font-size: 30px;
        line-height: 100px;
        color: darkred;
        text-align: center;
        box-shadow: 0px 0px 6px 6px grey;
        border-radius: 100px;
        border-bottom-color: yellow;
        border-left-color: green;
        border-top-color: red;
        border-right-color: blue;
        border-width: 3px;
        border-style: double;
        overflow: hidden;
        /*background: linear-gradient(to right,yellowgreen,darkolivegreen,green,lightgreen,green,darkolivegreen,yellowgreen);*/
        position:relative;
        animation:mymove1 10s linear infinite ;
    }
    #myimg{
        width: 100%;
        height:100%;
        vertical-align: center;
        margin: 0 auto;
        border: 1px solid darkmagenta;
        object-fit:cover;
        border-radius: 100px;

        animation:mymove2 10s linear infinite ;
    }
    @keyframes mymove1{
        0%   {top:0px;left:5%}
        50%  {top:0px;left: 90%;transform:rotate(720deg)}
        100% {top:0px;left:5%;transform:rotate(-720deg)}
    }
    @keyframes mymove2{
        0%   {transform:rotateY(0deg)}
        50%  {transform:rotateY(720deg)}
        100% {transform:rotateY(-720deg)}
    }



        /*
        0%   {top:-50px;left:-50px}
        25%     {top:-50px;left:80%;transform:rotate(90deg);}
        50%  {top:80%;left:80%;transform:rotate(180deg)}
        75%  {top:80%;left:-50px;transform:rotate(270deg)}
        100% {top:-50px;left:-50px;transform:rotate(360deg)}
        */

    /*
    #mydiv2{
        width: 100px;height:100px;
        font-size: 30px;
        line-height: 35px;
        color: darkred;
        text-align: center;
        border: 1px solid blue;
        border-radius: 40px;
        position:relative;
        animation:mymove2 5s infinite;

    }
    @keyframes mymove2{
        0%   {width: 10%;height: 10%}
        25%  {width: 50%;height: 50%}
        50%  {width: 100%;height: 100%}
        75%  {width: 50%;height: 50%}
        100% {width: 10%;height: 10%}
    }
    */
</style>
const express=require('express')
const app = express()
app.use(express.static(__dirname+'/static'))

function randomdata(){
    const data=[
        {id:'001',name:'张三',hobby:['篮球','足球','排球','电子游戏']},
        {id:'002',name:'李四',hobby:['美食','喝酒','抽烟']},
        {id:'003',name:'王五',hobby:['大数据','天文','地理','烫头','动物']},
        {id:'004',name:'赵六',hobby:['历史','画画','旅游','社会工作']},
        {id:'005',name:'孙七',hobby:['篮球','足球','摄影','喝酒']},
        {id:'006',name:'欧阳锋',hobby:['射击','盗窃','爬墙头','游戏']},
        {id:'007',name:'东方不败',hobby:['美女','足球','游手好闲','吃白饭']},
        {id:'009',name:'令狐冲',hobby:['家电维修','电影','旅游','游泳']},
        {id:'008',name:'令狐冲',hobby:['家电维修','电影','旅游','游泳']},
        {id:'008',name:'令狐冲',hobby:['家电维修','电影','旅游','游泳']},
        {id:'008',name:'令狐冲',hobby:['家电维修','电影','旅游','游泳']},

    ]
    var l=data.length
    if (!l){
        var row={id:'',name:'没有数据',hobby:[]}
    }
    var s=Math.floor(Math.random()*l)
    return data[s]
}

app.get("/testdata",(req,res)=>{
    res.header("Access-Control-Allow-Origin","*")
    var dt=new Date()
    var dt=dt.toLocaleTimeString('zh-CN',{
          timeZone: 'Asia/Shanghai',
          hour12: false, year: 'numeric',month: 'numeric',day: 'numeric'
    })
    console.log(req.ip)
    console.log(req.hostname)

    var data={data:randomdata(),serverdatetime:dt}
    res.send(data)
})

/*
*     // Request
    // req.baseUrl 基础路由地址
    // req.body post发送的数据解析出来的对象
    // req.cookies 客户端发送的cookies数据
    // req.hostname 主机地址 去掉端口号
    // req.ip 查看客户端的ip地址
    // req.ips 代理的IP地址
    // req.originalUrl 对req.url的一个备份
    // req.params 在使用/:id/:name 匹配params
    // req.path 包含请求URL的路径部分
    // req.protocol http 或https协议
    // req.query 查询字符串解析出来的对象 username=zhangsan&password=123 { username:zhangsan }
    // req.route 当前匹配的路由 正则表达式
    // req.params 获取路由匹配的参数
    // req.get 获取请求header里的参数
    // req.is 判断请求的是什么类型的文件
    // req.param(key名称) 用来获取某一个路由匹配的参数
    //Response
    // res.headersSent 查看http响应是否响应了http头
    // res.append(名称,value) 追加http响应头
    // res.attachment(文件路径) 响应文件请求
    // res.cookie() 设置cookie
    //res.setHeader('Content-Type','text/html;charset=utf8')
    // res.append('Content-Type','text/html;charset=utf8')
    // res.append('hehe','1008')
    // res.append('haha','1008')
    // res.attachment('./xx.zip') //Content-Disposition: attachment; filename="xx.zip"
    // res.clearCookie(cookiename) 删除cookie
    // res.cookie('zhangsan','lisi') 设置cookie
    // res.cookie('zhangsan1','lisi2',{
    //     maxAge:900000,
    //     httpOnly:true,
    //     path: '/admin',
    //     secure: true,
    //     signed:true
    // })
    // res.clearCookie('zhangsan')
    // res.download(文件的path路径) 跟attachment类似 用来处理文件下载的 参数是文件地址
    // res.end http模块自带的
    // res.format()协商请求文件类型 format匹配协商的文件类型
    // res.format({
    //     'text/plain': function(){
    //         res.send('hey');
    //     },
    //     'text/html': function(){
    //         res.send('<p>hey</p>');
    //     },
    //     'application/json': function(){
    //         res.send({ message: 'hey' });
    //     },
    //     'default': function() {
    //         // log the request and respond with 406
    //         res.status(406).send('Not Acceptable');
    //     }
    // });
    // res.get('key') 获取响应header数据
    // res.json() 返回json数据 会自动设置响应header Content-type 为json格式 application/json
    // res.json({
    //     xx:100
    // })
    // res.json({
    //     xx:100
    // })
    // jsonp 利用的就是浏览器加载其他服务器的文件不会存在跨域问题
    // ajax请求就会有跨域问题
    // res.setHeader('Content-Type','text/javascript;charsert=utf8')
    // res.end(`typeof ${req.query.callback} == 'function' ? ${req.query.callback}({aa:100}):null`)
    // res.jsonp({aaa:100})
    // 重定向 把访问的地址跳转到另一个地址上
    // res.redirect(301,'/api/aes')
    // express jade
    // res.render('index',{title:"hehe",test:"23"})
    // res.send('') 发送数据 可以是任意类型的数据
    // res.sendFile() 发送文件的
    // res.sendStatus(200) 设置发送时的状态码
    // res.set('Content-Type', 'text/plain') //设置响应header
    // res.status(200) // 设置状态码
    // res.type('') // 直接设置响应的文件类型
    // res.type('pdf')
    // res.send({aa:100})
    // res.end('ok')
    // res.end({aa:100})
    // res.end('你好')
    // res.end(req.get('Accept-Language'))
    // res.json({
    //     is:req.is('text/html')
    // })
    // res.json({
    //     type:req.baseUrl,
    //     hostname:req.hostname,
    //     // ip:req.ip,
    //     // ips:req.ips,
    //     // route:req.route,
    //     ct:req.get('Accept'),
    //     cs:'22'
    // })
*
* */

const server = app.listen(5500,(err)=>{
    var port=''
    if (!err){
        port=server.address().port
        console.log('Server_test_1 启动成功!')
        console.log('访问地址:http://localhost:',port)
    }
})
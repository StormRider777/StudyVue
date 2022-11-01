import {nanoid} from "nanoid";

export const defaultbooks_data={
        dili: {
          title: '地理',img:'../../img/dili.jpeg',
          lists: [
            {id: nanoid(), name: '中国地理概论', img: ''},
            {id: nanoid(), name: '山东河流分布图', img: ''},
            {id: nanoid(), name: '珠穆朗峰研究', img: ''},
            {id: nanoid(), name: '甘肃喀斯特地貌', img: ''},
            {id: nanoid(), name: '新疆大草原现状', img: ''},
            {id: nanoid(), name: '山水桂林', img: ''},
            {id: nanoid(), name: '长江流域生态现状', img: ''},
          ]
        },
        lishi: {
          title: '历史', img:'../../img/lishi.jpeg',
          lists: [
            {id: nanoid(), name: '明朝那些事', img: ''},
            {id: nanoid(), name: '史记', img: ''},
            {id: nanoid(), name: '三国志', img: ''},
            {id: nanoid(), name: '汉书', img: ''},
          ]
        },
        xiaoshuo: {
          title: '小说', img:'../../img/xiaoshuo.jpeg',
          lists: [
            {id: nanoid(), name: '三国演义', img: ''},
            {id: nanoid(), name: '西游记', img: ''},
            {id: nanoid(), name: '红楼梦', img: ''},
            {id: nanoid(), name: '金瓶梅', img: ''},
          ]
        },
        jishu: {
          title: '技术', img:'../../img/jishu.jpeg',
          lists: [
            {id: nanoid(), name: 'Python高级进阶', img: ''},
            {id: nanoid(), name: 'Django+vue+Mysql', img: ''},
            {id: nanoid(), name: '股市一点通', img: ''},
            {id: nanoid(), name: 'Javascript前端', img: ''},
          ]
        }
      }


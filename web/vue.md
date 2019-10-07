
<!-- TOC -->

- [1. 说明](#1-说明)
- [2. socketio的坑](#2-socketio的坑)
- [3. this的坑](#3-this的坑)
    - [3.1. 普通函数](#31-普通函数)
    - [3.2. 对象函数](#32-对象函数)
    - [3.3. apply 和 call调用](#33-apply-和-call调用)
        - [3.3.1. call 和 apply的区别](#331-call-和-apply的区别)
    - [3.4. 箭头函数](#34-箭头函数)
        - [3.4.1. 没有箭头函数前](#341-没有箭头函数前)
        - [3.4.2. 有箭头函数后](#342-有箭头函数后)
- [4. let 和 var的区别](#4-let-和-var的区别)
    - [4.1. 块级和全局(函数级)](#41-块级和全局函数级)
- [5. ===的坑](#5-的坑)
- [6. 修改b-table绑定数据某一元素的某一key时,页面不刷新](#6-修改b-table绑定数据某一元素的某一key时页面不刷新)
- [7. 同步请求的方法](#7-同步请求的方法)
- [8. 页面跳转传参数query,params](#8-页面跳转传参数queryparams)

<!-- /TOC -->

# 1. 说明

* https://cn.vuejs.org/v2/guide/installation.html#Vue-Devtools (文档)

```bash
# 启动起来
vue init webpack supervue
cd supervue
cnpm run dev

# 安装bootstrip && bootstrap-vue
cnpm install --save bootstrap  bootstrap-vue

# index.js
import BootstrapVue from 'bootstrap-vue'
Vue.use(BootstrapVue)

import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.min.js';
import 'bootstrap-vue/dist/bootstrap-vue.min.css'

# 安装fontawesome
cnpm install font-awesome --save
import "font-awesome/css/font-awesome.min.css"

# http 请求
cnpm install axios --save

# socketio https://github.com/MetinSeylan/Vue-Socket.io  
# https://github.com/MetinSeylan/Vue-Socket.io/issues/62 (wsocket 问题) 
# https://github.com/heroku-python/flask-sockets (需要wsgi!!)
cnpm install vue-socket.io --save
cnpm install socket.io-client --save

# 时间库
cnpm install moment --save
```

# 2. socketio的坑

```bash
# 这个只能使用一个websocket连接
// import VueSocketIO from 'vue-socket.io';
// const socketInstance = io('ws://localhost:33333', {transports: ['websocket']});
// Vue.use(new VueSocketIO({connection: socketInstance}));
```

# 3. this的坑

## 3.1. 普通函数

```javascript
let fuck1 = "fuck1";
var fuck2 = "fuck2";
function fn() {
    console.log(this.fuck1);
    console.log(this.fuck2);
}
fn();

// nodejs:
undefined
undefined

// chrome:
undefined
fuck2

// 只有chrome的var定义才会定义到全局范围内
```

## 3.2. 对象函数
```js
let fuck1 = "fuck1";

let obj = {
    fuck2: "fuck2",
    fn: function () {
        console.log(this.fuck1);
        console.log(this.fuck2);
    }
};

obj.fn();

// nodejs:
undefined
fuck2

// chrome:
undefined
fuck2

// 对象函数的this指向对象
```

```js
let fuck1 = "fuck1";

let obj = {
    fuck2: "fuck2",
    fn: function () {
        console.log(this.fuck1);
        console.log(this.fuck2);
    }
};

fn2 = obj.fn;
fn2();

// this是指当时调用者对象
```

## 3.3. apply 和 call调用

```js
let obj1 = {
    fuck1: "obj1 fuck1"
};


let obj2 = {
    fuck1: "obj2 fuck1",
    fn: function () {
        console.log(this.fuck1);
    }
};

obj2.fn.call(obj1);

// 对象函数.call(对象) 就像c++的多态一样, this.foo, this.varible 根据不同的对象有不同的实现
```


### 3.3.1. call 和 apply的区别

```js
let fn = function (a, b, c) {
    console.log(a);
    console.log(b);
    console.log(c);
};

let arry = [1, 2, 3];
fn.call(window, arry[0], arry[1], arry[2]);
fn.apply(window, arry);

// 在nodejs中window是global
```

## 3.4. 箭头函数


### 3.4.1. 没有箭头函数前

```js
let obj = {
    fuck1: "fuck1",
    fn: function () {
        setTimeout(function() {
            console.log(this.fuck1);});
    }
};

obj.fn();

// nodejs:
undefined

// 回调函数是普通函数,this指向了全局空间,而全局空间没有name,所以输出了underfind
```

### 3.4.2. 有箭头函数后

```js

let obj = {
    fuck1: "fuck1",
    fn: function () {
        setTimeout(()=> {
            console.log(this.fuck1);});
    }
};

obj.fn();


// nodejs:
fuck1

// 箭头函数会自动寻找上层作用域,是对象
```


# 4. let 和 var的区别


## 4.1. 块级和全局(函数级)

```javascript
let fuck = function () {
    let fuck1 = "fuck1";
    {
        let fuck1 = 'shit1';
        console.log(fuck1);
    }
    console.log(fuck1);
};

fuck();

// nodejs
shit1
fuck1

// let 是块级的
```


```javascript
let fuck = function () {
    var fuck1 = "fuck1";
    {
        var fuck1 = 'shit1';
        console.log(fuck1);
    }
    console.log(fuck1);
};

fuck();

// nodejs
shit1
shit1

// var 是全局的,或者是函数级的. 无法是块级的!
```


# 5. ===的坑

* == 比较,判断两者相等, 比较时自动换数据类型
* === 用于严格比较,  判断两者不相等,不会进行自动转换


# 6. 修改b-table绑定数据某一元素的某一key时,页面不刷新

* https://segmentfault.com/a/1190000019470488
  
# 7. 同步请求的方法


```js
 async getSubs() {
                try {
                    // 查询到机器列表
                    let res = await this.$http.post(this.masterapiaddr + "/api", {
                        jsonrpc: "2.0",
                        method: 'getsubs',
                        params: {},
                        id: 0
                    });
                    let subs = JSON.parse(res.data.result);

                    // 每个机器都查询机器信息
                    for (let i = 0; i < subs.length; i++) {
                        let curip = subs[i].ip;
                        let res = await this.$http.post("http://" + curip + ":22222/api", {
                            jsonrpc: "2.0",
                            method: "getMachineState",
                            params: {},
                            id: 0
                        });

                        let machinestate = JSON.parse(res.data.result);
                        subs[i]["cpu"] = machinestate.cpuInfo.usage + "%";
                        subs[i]["mem"] = (100.0 * machinestate.memInfo.used / machinestate.memInfo.total).toFixed(2) + "%";
                        subs[i]["disk"] = (100.0 * machinestate.diskInfo.used / machinestate.diskInfo.total).toFixed(2) + "%";
                        subs[i]["network"] = "send: " + (machinestate.networkInfo.WLAN.persec_sent / 1000).toFixed(0) + "k" + " recv: "
                            + (machinestate.networkInfo.WLAN.persec_recv / 1000).toFixed(0) + "k";
                    }

                    this.items = subs;
                } catch (err) {
                    console.log(err);
                }
            }
```

# 8. 页面跳转传参数query,params

* https://segmentfault.com/a/1190000017072101
* https://www.cnblogs.com/sese/p/9595625.html


```

query:

this.$router.push(
    {
        path: '/xxx',
        query: {
            id: id
        }
    }
)


params:

this.$router.push(
    {
        name: 'xxx',
        params: {
            id: id
        }
    }
)

query 生成的urfl为/xx?id=id. params生成的url为xx/id
query this.$route.query.ip . params this.$route.params.ip
```





<!-- TOC -->

- [1. 资料](#1-资料)
- [2. 简介](#2-简介)
- [3. 我的看法](#3-我的看法)
    - [3.1. json2.0](#31-json20)
    - [3.2. json1.0](#32-json10)
    - [3.3. json1.1](#33-json11)

<!-- /TOC -->


<a id="markdown-1-资料" name="1-资料"></a>
# 1. 资料

* https://www.zhihu.com/question/28557115
* https://www.zhihu.com/question/27785028 (如何生动地理解)
* https://en.wikipedia.org/wiki/Representational_state_transfer
* http://www.ruanyifeng.com/blog/2011/09/restful.html (阮一峰的理解)
* http://www.infoq.com/cn/articles/webber-rest-workflow/ (用restful获取一杯咖啡)

<a id="markdown-2-简介" name="2-简介"></a>
# 2. 简介
> 用URL定位资源，用HTTP描述操作

![](http://ouxarji35.bkt.clouddn.com/20170925225307.jpg)

<a id="markdown-3-我的看法" name="3-我的看法"></a>
# 3. 我的看法

其实rest设计是一个使用场景非常有限的架构风格. 把所有的请求都当成资源来归类,用GET,POST,PUT,DELETE来调用. 本质上只适合纯粹的CRUD场景.  (参数放1. 路径 2. body)

大部分场景还是使用http + jsonrpc. 因为它最贴合我们日常的使用习惯 -- "我要请求远程服务器的一个函数,请求的参数是什么" .  并且json是一个非常好的数据交换格式, 有 null,boolean,string,number,array,object等类型, 可以转换成所有语言的内置结构体 (配合json schema)效果更加.

<a id="markdown-31-json20" name="31-json20"></a>
## 3.1. json2.0

请求:
```js
{
"jsonrpc": "2.0",
"method": "subtract",
"params": {
    "minuend": 42,
    "subtrahend": 23
},
"id": 3
}
```

应答:
```js
{
	"jsonrpc": "2.0",
	"result": 19,
	"id": 3
}
```


没有应答的请求:
```js
{
	"jsonrpc": "2.0",
	"method": "update",
	"params": [1, 2, 3, 4, 5]
}
```


<a id="markdown-32-json10" name="32-json10"></a>
## 3.2. json1.0

请求:
```js
{
	"method": "echo",
	"params": ["Hello JSON-RPC"],
	"id": 1
}
```

应答:
```js
{
	"result": "Hello JSON-RPC",
	"error": null,
	"id": 1
}
```

<a id="markdown-33-json11" name="33-json11"></a>
## 3.3. json1.1

请求:
```js
{
	"version": "1.1",
	"method": "confirmFruitPurchase",
	"params": [
		["apple", "orange", "mangoes"], 1.123
	],
	"id": "194521489"
}
```

应答:
```js
 {
 	"version": "1.1",
 	"result": "done",
 	"error": null,
 	"id": "194521489"
 }
```

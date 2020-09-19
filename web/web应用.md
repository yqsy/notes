<!-- TOC -->

- [1. 登录](#1-登录)
- [2. post 数据](#2-post-数据)
- [3. get,post动机](#3-getpost动机)
- [4. restful](#4-restful)
- [5. cookie 和 session](#5-cookie-和-session)
- [6. golang 怎么写完美的增删改查](#6-golang-怎么写完美的增删改查)
- [7. 返回状态码含义](#7-返回状态码含义)
- [8. golang 事务总结](#8-golang-事务总结)
- [9. mysql 默认数据库打爆问题](#9-mysql-默认数据库打爆问题)
- [10. left right inner all 区别](#10-left-right-inner-all-区别)
- [11. 数据库接口拼接](#11-数据库接口拼接)
- [12. 步骤](#12-步骤)
- [13. orm or ?](#13-orm-or-)
- [14. 控件数据和数据库数据的绑定](#14-控件数据和数据库数据的绑定)
- [15. 主线程请求堵塞](#15-主线程请求堵塞)
- [16. 线程安全](#16-线程安全)
- [17. mvc](#17-mvc)

<!-- /TOC -->


# 1. 登录


* https://github.com/Depado/gin-auth-example/blob/master/main.go


用户通过 `/login` 接口 post username 和 passowrd. 服务器验证Username 和 password在数据库中有没有. 如果有返回一个session, session就是一个会话的上下文 (context).

服务器可以根据这个context里面的数据,增删改查他拥有权限的数据.

session 是通过Cookie 机制保存的

# 2. post 数据

试了下在postman种post后服务器收不到, 是因为我配置错了. 


post -> body ->  两种:

1. form-data . 分割符号分开 body里
2. x-www-form-urlencoded. & 分割,  name1=value1&name2=value2.  字符串append到url后面. post时,浏览器将数据放到body里 (比较多)
3. raw. 任意格式


# 3. get,post动机

* get没有修改数据
* post有修改数据
  

# 4. restful

怎样用通俗的语言解释REST，以及RESTful？ - 覃超的回答 - 知乎
https://www.zhihu.com/question/28557115/answer/48094438

WEB开发中，使用JSON-RPC好，还是RESTful API好？ - 大宽宽的回答 - 知乎
https://www.zhihu.com/question/28570307/answer/541465581

restful 就是一个很扯的东西.  对资源的动作不可能仅仅只是被抽象成 GET SET POST DELETE. 还有很多. 业务比CRUD复杂很多.


最佳实践:

* 忘记REST这个事情
* 只用 GET和POST
* 用动作! 就去用,rest是很傻的

# 5. cookie 和 session

session 是利用cookie进行信息处理的. cookie数据保存在客户端, session数据保存在服务端.

客户端每次请求服务器时都会发送当前会话的sessionid,服务器根据当前sessionid判断当前相应的用户数据标志.


# 6. golang 怎么写完美的增删改查

* https://stackoverflow.com/questions/16184238/database-sql-tx-detecting-commit-or-rollback (事务回滚)

还是我的比较好啊哈哈

# 7. 返回状态码含义

* 关于 RESTful API 中 HTTP 状态码的定义的疑问？ - Liril的回答 - 知乎
https://www.zhihu.com/question/58686782/answer/159603453

关于 RESTful API 中 HTTP 状态码的定义的疑问？ - 寸志的回答 - 知乎
https://www.zhihu.com/question/58686782/answer/159196410



# 8. golang 事务总结

连接得坑问题

https://www.cnblogs.com/wangchaowei/p/7994022.html

```bash

# 事务三件套
tx, err := db.Begin()
if err != nil {
    panic(err)
}
defer tx.Rollback()

if err := tx.Commit(); err != nil {
    panic(err)
}
    
# 增加 (自动释放)
if _, err := db.Exec("insert") ...

# 修改 (自动释放)
if _,err := db.Exec("update") ...

# 查一行
if err := db.QueryRow("select").scan(&xxx,&xxx)

# 查多行
rows, err := db.Query
err != nil {

}

defer rows.Close()

for rows.Next() {

    if err := rows.Scan(&xxx,&xxx) {
        
    }
}
```


# 9. mysql 默认数据库打爆问题


```bash
# 查看连接数
show processlist; 

# 查询
show variables like "max_connections"; 

# 修改最大连接数
set GLOBAL max_connections=1000; 

# 查询关闭非交互连接时间
show global variables like 'wait_timeout'; 

# 设置连接关闭时间
set global wait_timeout=28800; 

# 关闭正在使用/没在使用的连接
#set global interactive_timeout=500; 
```


# 10. left right inner all 区别

https://stackoverflow.com/questions/448023/what-is-the-difference-between-left-right-outer-and-inner-joins


# 11. 数据库接口拼接

```
增  -> insert 不定参数

删 -> where 不定条件

改 -> 1. update 不定参数 2. where不定条件

查 -> where 不定条件 

```



# 12. 步骤


1. 设计界面

2. 数据库 

3. 数据库接口  + api

4. 驱动数据


阶段一: 拼接sql字符串
阶段二: 使用sql拼接库  + 自己元数据生成
阶段三: 使用高级orm  (一定要用orm, 否则你只是造了个搓的orm轮子)
 

确实需要orm, 遇到的问题是

1. 增删改查 接口都要写,很容易弄错
2. 表字段 增加, 删除  对应  增, 查 接口都要修改.  api层变化.

# 13. orm or ?

* https://github.com/jmoiron/sqlx (golang 拼接库)
* https://github.com/kayak/pypika  (python 拼接库)
* https://programtalk.com/python-examples/sqlalchemy.insert/  (python orm)
* https://github.com/jinzhu/gorm (golang orm)


能用orm就orm

# 14. 控件数据和数据库数据的绑定

能用view 就 view


# 15. 主线程请求堵塞


1. 主线程渲染. 2. 背景线程 线程/线程池 loop

当主线程想获取堵塞资源时, 创建一个堵塞函数(堵塞完成emit界面槽函数).  以task方式扔给背景线程.

主线程(ui) -> 背景线程(网络通讯)

global对象      background对象

                对象提供push task接口

pyqt协程案例
```py
class Global(QObject):

    # 测试槽函数
    test_emit = QtCore.pyqtSignal(str)


    def PutATaskToBack(self):
        asyncio.run_coroutine_threadsafe(foo(), self.background.loop)

class Background(QtCore.QThread):
    def __init__(self):
        super(Background, self).__init__()
        self.loop = asyncio.get_event_loop()

    def run(self):
        self.loop.run_forever()


g = Global()
g.background = Background()
g.background.start()
```

pyqt 线程池案例
```py

```


c++ 线程池案例
```py

```


# 16. 线程安全

一般情况下一个资源的使用者最好是一个线程/协程. 如果有多个线程/协程操作,  把资源整个拷贝过去.

实在要多线程/协程共享资源, 要加互斥体


```py
import asyncio


class A:

    def __init__(self):
        self.a = 1

    async def run(self):
        self.a += 1
        await asyncio.sleep(1)
        self.a -= 1
        print(self.a)


a = A()

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(a.run(), a.run(), a.run(), a.run()))

```


# 17. mvc

一定要用mvc!!!!!!!!!  痛的教训

model view controll

1. 有些数据展示在 table上, 还要二次利用,  单是利用的时候 是 model. 而不是展示的数据
RrNaaUKQ4ZKc1ErPtSI2g0LZFAGHVwBlT4gfM5TJhGsyPE46K3w1ALLTuHRz6DtB
8vSOvxaHuT67XCsxwJAdK5Y0WD9heqSmzWYum8aewdrWj6akZDr2SEgwVnj0A8SU
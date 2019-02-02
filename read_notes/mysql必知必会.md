---
title: mysql必知必会
date: 2017-12-3 15:21:54
categories: [读书笔记]
---

<!-- TOC -->

- [1. p2-什么是数据库](#1-p2-什么是数据库)
- [2. p2-组成数据库的元素](#2-p2-组成数据库的元素)
- [3. p5-什么是SQL](#3-p5-什么是sql)
- [4. p8-什么是MySQL](#4-p8-什么是mysql)
- [5. p21-是否使用分号](#5-p21-是否使用分号)
- [6. p21-SQL语句和大小写](#6-p21-sql语句和大小写)
- [7. p23-使用通配符](#7-p23-使用通配符)
- [8. p31-指定排序方向](#8-p31-指定排序方向)
- [9. p33-ORDER BY语句的位置](#9-p33-order-by语句的位置)
- [10. p36-NULL值](#10-p36-null值)
- [11. p42-OR与AND处理先后](#11-p42-or与and处理先后)
- [12. p44-为什么要使用IN操作符?](#12-p44-为什么要使用in操作符)
    - [12.1. p45-example](#121-p45-example)
    - [12.2. p45-使用IN](#122-p45-使用in)
- [13. p47-通配符](#13-p47-通配符)
- [14. p49-通配符使用技巧](#14-p49-通配符使用技巧)
- [15. p52-正则表达式](#15-p52-正则表达式)
    - [15.1. p52-example](#151-p52-example)
    - [15.2. p54-大小写区分问题](#152-p54-大小写区分问题)
- [16. p64-拼接字符串](#16-p64-拼接字符串)
    - [16.1. p65-Trim函数](#161-p65-trim函数)
- [17. p68-使用数据处理函数](#17-p68-使用数据处理函数)
    - [17.1. p69-文本处理函数](#171-p69-文本处理函数)
    - [17.2. p71-日期和时间处理函数](#172-p71-日期和时间处理函数)
        - [17.2.1. p73-使用Date()](#1721-p73-使用date)
    - [17.3. p74-数值处理函数](#173-p74-数值处理函数)
    - [17.4. p76-SQL聚集函数](#174-p76-sql聚集函数)
        - [17.4.1. p107-组合聚集函数](#1741-p107-组合聚集函数)
- [18. p84-分组数据](#18-p84-分组数据)
    - [18.1. p86-HAVING和WHERE的差别](#181-p86-having和where的差别)
- [19. p88-SELECT子句顺序](#19-p88-select子句顺序)
- [20. p97-联结](#20-p97-联结)
    - [20.1. p98-example](#201-p98-example)
    - [20.2. p101-笛卡儿积](#202-p101-笛卡儿积)
    - [20.3. p105-使用哪种语法?](#203-p105-使用哪种语法)
    - [20.4. p108-自联结而不是子查询](#204-p108-自联结而不是子查询)
    - [20.5. p106-别名的作用](#205-p106-别名的作用)
    - [20.6. p111-使用带聚集函数的联结](#206-p111-使用带聚集函数的联结)
    - [20.7. p112-使用联结和联结条件](#207-p112-使用联结和联结条件)
- [21. p114-组合查询和多个WHERE条件](#21-p114-组合查询和多个where条件)
- [22. p115-UNION规则](#22-p115-union规则)
- [23. p116-UNION ALL](#23-p116-union-all)
- [24. p134-INSERT操作可能很好耗时](#24-p134-insert操作可能很好耗时)
    - [24.1. p136-提高插入性能的INSERT用法](#241-p136-提高插入性能的insert用法)
- [25. p141-删除数据不省略WHERE](#25-p141-删除数据不省略where)
- [26. p142-更快地删除数据](#26-p142-更快地删除数据)
- [27. p151-MySQL引擎](#27-p151-mysql引擎)
- [28. p151-外键不能跨引擎](#28-p151-外键不能跨引擎)
- [29. p153-小心使用ALTER TABLE](#29-p153-小心使用alter-table)
- [30. p156-为什么使用视图?](#30-p156-为什么使用视图)
- [31. p164-为什么使用存储过程?](#31-p164-为什么使用存储过程)
- [32. p174-使用游标](#32-p174-使用游标)
- [33. p186-关于触发器的进一步介绍](#33-p186-关于触发器的进一步介绍)
- [34. p188-事务处理](#34-p188-事务处理)
    - [34.1. p189-事务处理的几个知识点](#341-p189-事务处理的几个知识点)
    - [34.2. p190-哪些语句可以回退?](#342-p190-哪些语句可以回退)
    - [34.3. p192-更改默认的提交行为](#343-p192-更改默认的提交行为)
- [35. p202-访问权限](#35-p202-访问权限)
- [36. p205-备份数据](#36-p205-备份数据)
- [37. p206-数据库维护](#37-p206-数据库维护)
    - [37.1. p205-检查表键是否正确](#371-p205-检查表键是否正确)
    - [37.2. p205-对表进行检查](#372-p205-对表进行检查)
    - [37.3. p207-诊断启动问题](#373-p207-诊断启动问题)
    - [37.4. p207-查看日志文件](#374-p207-查看日志文件)
- [38. p209-改善性能](#38-p209-改善性能)
- [39. p225-串数据类型](#39-p225-串数据类型)
- [40. p226-数值数据类型](#40-p226-数值数据类型)
- [41. p227-日期和时间数据类型](#41-p227-日期和时间数据类型)
- [42. p227-二进制数据类型](#42-p227-二进制数据类型)

<!-- /TOC -->


<a id="markdown-1-p2-什么是数据库" name="1-p2-什么是数据库"></a>
# 1. p2-什么是数据库
人们通常用**数据库**这个术语来代表他们使用的**数据库软件**,这是不正确的,它是引起混淆的根源.**数据库软件**应称为DBMS(数据库管理系统).**数据库**是通过DBMS创建和操纵的容器.
<a id="markdown-2-p2-组成数据库的元素" name="2-p2-组成数据库的元素"></a>
# 2. p2-组成数据库的元素

元素|说明
-|-
 表   | 某种特定类型数据的结构化清单                                           
 模式  | 模式用来描述数据库中特定的表以及整个数据库.关于数据库和表的布局及特性的信息                    
 列   | 表中的一个字段,所有表都是由一个或多个列组成的                                 
 行   | 表中的一个记录,可能听到用户在提到**row**时称其为**record**,从技术上来说,row才是正确的术语  
 主键  | 表中每一行都应该有可以唯一标识自己的一列.**应该总是定义主键**                        

<a id="markdown-3-p5-什么是sql" name="3-p5-什么是sql"></a>
# 3. p5-什么是SQL
SQL是结构化查询语言(Structured Query Language)的缩写.SQL是一种专门用来与数据库通信的语言.SQL不是一种专利语言,而且存在一个标准委员会,他们试图定义可供所有DBMS使用的SQL语法,但事实上任意两个DBMS实现的SQL都不完全相同.
<a id="markdown-4-p8-什么是mysql" name="4-p8-什么是mysql"></a>
# 4. p8-什么是MySQL
MySQL是一种DBMS,即它是一种数据库软件.

特点|说明
-|-
成本   | MySQL是开放源代码的,一般可以免费使用                                  
性能   | MySQL执行很快                                             
可信赖  | 某些非常重要和声望很高的公司,站点,使用MySQL,这些公司和站点都用MySQL来处理自己的重要数据  
简单   | MySQL很容易安装和使用                                          

<a id="markdown-5-p21-是否使用分号" name="5-p21-是否使用分号"></a>
# 5. p21-是否使用分号
如果愿意可以总是加上分号,事实上,即使不一定需要,但加上分号肯定没坏处.如果你使用的是mysql命令行,**必须加上分号**来结束SQL语句.
<a id="markdown-6-p21-sql语句和大小写" name="6-p21-sql语句和大小写"></a>
# 6. p21-SQL语句和大小写
SQL语句不区分大小写,因此**SELECT**与**select**是相同的,许多开发人员喜欢对所有SQL关键字使用大写,而**对所有列和表使用小写**,这样做使代码更易于阅读和调试.
<a id="markdown-7-p23-使用通配符" name="7-p23-使用通配符"></a>
# 7. p23-使用通配符
一般,除非你确实需要表中的每个列,否则最好别使用*通配符,虽然使用通配符可能会使你自己省事,不用明确列出所需列,单检索不需要的列通常会降低检索和应用程序的性能.

<a id="markdown-8-p31-指定排序方向" name="8-p31-指定排序方向"></a>
# 8. p31-指定排序方向
数据排序不限于升序排序(从A到Z).这只是默认的排序(**ASC**),为了进行降序排序,必须指定**DESC**关键字.

<a id="markdown-9-p33-order-by语句的位置" name="9-p33-order-by语句的位置"></a>
# 9. p33-ORDER BY语句的位置
应该保证它位于FROM子句之后,如果使用LIMIT,它必须位于ORDER BY之后.

<a id="markdown-10-p36-null值" name="10-p36-null值"></a>
# 10. p36-NULL值
NULL 空值(no value),它与以下不同
  * 字段包含0
  * 空字符串
  * 仅仅包含空格
<a id="markdown-11-p42-or与and处理先后" name="11-p42-or与and处理先后"></a>
# 11. p42-OR与AND处理先后
SQL(像大多数语言一样)在处理OR操作符之前,优先处理AND操作符.

<a id="markdown-12-p44-为什么要使用in操作符" name="12-p44-为什么要使用in操作符"></a>
# 12. p44-为什么要使用IN操作符?
  * 在使用长的合法选项清单时,IN操作符的语法更清楚且更直观
  * 在使用IN时,计算的次序更容易管理(因为使用的操作符更少)
  * IN操作符一般比OR操作符清单执行更快
  * IN的最大的优点是可以包含其他SELECT语句,使能够更动态地建立WHERE子句
<a id="markdown-121-p45-example" name="121-p45-example"></a>
## 12.1. p45-example
```sql
SELECT prod_name, prod_price
FROM products
WHERE vend_id = 1002 OR vend_id = 1003
ORDER BY prod_name;
```

<a id="markdown-122-p45-使用in" name="122-p45-使用in"></a>
## 12.2. p45-使用IN
```sql
SELECT prod_name, prod_price
FROM products
WHERE vend_id IN (1002,1003)
ORDER BY prod_name;
```

<a id="markdown-13-p47-通配符" name="13-p47-通配符"></a>
# 13. p47-通配符
  * %表示任何字符出现任意次数.
  * 搜索模式%anvil%表示匹配任何位置包含文本anvil的值.
  * %还能匹配0个字符.
  * 另一个通配符是_,与%一样,但下划线只匹配单个字符而不是多个字符.

<a id="markdown-14-p49-通配符使用技巧" name="14-p49-通配符使用技巧"></a>
# 14. p49-通配符使用技巧
  * 通配符搜索的处理一般要比其他搜索花时间更长
  * 不要过度使用通配符,如果其他操作符能达到相同的目的,应该使用其他操作符
  * 不要把通配符用在搜索模式的开始处,把通配符置于搜索模式的开始处,搜索起来是最慢的
  * 仔细注意通配符的位置,如果放错地方,可能不会返回想要的数据

<a id="markdown-15-p52-正则表达式" name="15-p52-正则表达式"></a>
# 15. p52-正则表达式
MySQL仅支持多数正则表达式实现的一个很小的子集.
<a id="markdown-151-p52-example" name="151-p52-example"></a>
## 15.1. p52-example
```sql
SELECT prod_name
FROM products
WHERE prod_name REGEXP '.000'
ORDER BY prod_name;
```
当然上面这个特殊的例子也可以用LIKE和通配符来完成.

<a id="markdown-152-p54-大小写区分问题" name="152-p54-大小写区分问题"></a>
## 15.2. p54-大小写区分问题
MySQL中的正则表达式匹配不区分大小写,为区分大小写,可使用BINARY关键字.
```sql
WHERE prod_name REGEXP BINARY 'JetPack .000';
```

<a id="markdown-16-p64-拼接字符串" name="16-p64-拼接字符串"></a>
# 16. p64-拼接字符串
多数DBMS使用+或||来实现拼接,MySQL则使用Concat()函数来实现.当把SQL语句转换成MySQL语句时一定要把这个区别铭记在心.

<a id="markdown-161-p65-trim函数" name="161-p65-trim函数"></a>
## 16.1. p65-Trim函数
MySQL除了支持**RTrim()**,还支持**LTrim()**以及**Trim()**

<a id="markdown-17-p68-使用数据处理函数" name="17-p68-使用数据处理函数"></a>
# 17. p68-使用数据处理函数
函数没有SQL的可移植性强,多数SQL语句是可移植的,在SQL实现之间有差异时,这些差异通常不那么难处理.而函数的可移植性却不强.几乎每种主要的DBMS的实现都支持其他实现不支持的函数,而且有时差异还很大.\\

大多数SQL实现支持以下类型的函数
  * 用于处理文本字符串(如删除或填充值,转换值为大写或小写)的文本函数
  * 用于在数值数据上进行算数操作(如返回绝对值,进行代数运算)的数值函数
  * 用于处理日期和时间值并从这些值中提取特定成分(例如,返回两个日期之差,检查日期有效性等)的日期和时间函数
  * 返回DBMS正使用的特殊信息(如返回用户登录信息,检查版本细节)的系统函数


<a id="markdown-171-p69-文本处理函数" name="171-p69-文本处理函数"></a>
## 17.1. p69-文本处理函数

函数|说明
-|-
 Left()       | 返回串左边的字符      
 Right()      | 返回串右边的字符      
 LTrim()      | 去掉串左边的空格      
 RTrim()      | 去掉串右边的空格      
 Trim()       | 去掉串左右的空格      
 Lower()      | 将串转换成小写       
 Upper()      | 将串转换为大写       
 Length()     | 返回串的长度        
 Locate()     | 找出串的一个子串      
 SubString()  | 返回子串的字符       
 Soundex()    | 返回串的SOUNDEX值  
<a id="markdown-172-p71-日期和时间处理函数" name="172-p71-日期和时间处理函数"></a>
## 17.2. p71-日期和时间处理函数

函数|说明
-|-
 Now()          | 返回当前日期和时间        
 CurDate()      | 返回当前日期           
 CurTime()      | 返回当前时间           
 Date()         | 返回日期时间的日期部分      
 Time()         | 返回日期时间的时间部分    
 AddDate()      | 增加一个日期(天,周等)     
 AddTime()      | 增加一个时间(时,分等)     
 Year()         | 返回一个日期的年份部分      
 Month()        | 返回一个日期的月份部分      
 Day()          | 返回一个日期的天数部分      
 Hour()         | 返回一个时间的小时部分      
 Minute()       | 返回一个时间的分钟部分      
 Second()       | 返回一个时间的秒部分      
 Date_Add()     | 高度灵活的日期运算函数      
 DateDiff()     | 计算两个日期之差        
 Date_Format()  | 返回一个格式化的日期或时间串   
 DayOfWeek()    | 对于一个日期,返回对应的星期几  

<a id="markdown-1721-p73-使用date" name="1721-p73-使用date"></a>
### 17.2.1. p73-使用Date()
如果要的是日期,请使用Date(),如果你想要的仅是日期,则使用Date()是一个良好的习惯,即使你知道相应的列只包含日期也是如此.
```sql
SELECT cust_id,order_num
FROM orders
WHERE Date(order_date) = '2005-09-01';
```

<a id="markdown-173-p74-数值处理函数" name="173-p74-数值处理函数"></a>
## 17.3. p74-数值处理函数

函数|说明
-|-
 Sin()   | 返回一个角度的正弦  
 Cos()   | 返回一个角的余弦  
 Tan()   | 返回一个角度的正切  
 Mod()   | 返回除操作的余数   
 Abs()   | 返回一个数的绝对值  
 Sqrt()  | 返回一个数的平方根  
 Exp()   | 返回一个数的指数值  
 Pi()    | 返回圆周率     
 Rand()  | 返回一个随机数    

<a id="markdown-174-p76-sql聚集函数" name="174-p76-sql聚集函数"></a>
## 17.4. p76-SQL聚集函数

函数|说明
-|-
 AVG()    | 返回某列的平均值  
 COUNT()  | 返回某列的行数  
 MAX()    | 返回某列的最大值  
 MIN()    | 返回某列的最小值  
 SUM()    | 返回某列值之和  
<a id="markdown-1741-p107-组合聚集函数" name="1741-p107-组合聚集函数"></a>
### 17.4.1. p107-组合聚集函数
```sql
SELECT COUNT(*) AS num_items,
       MIN(prod_price) AS price_min,
       MAX(prod_price) AS price_max,
       AVG(prod_price) AS price_avg
FROM products;
```

<a id="markdown-18-p84-分组数据" name="18-p84-分组数据"></a>
# 18. p84-分组数据
GROUP BY子句只指示MySQL分组数据,然后对每个组而不是整个结果集进行聚集.规定:
  * GROUP BY子句可以包含任意数目的列,这使得能对分组进行嵌套,为数据分组提供更细致的控制.
  * 如果在GROUP BY子句中嵌套了分组,数据将在最后规定的分组上进行汇总.换句话说,在建立分组时,指定的所有列都一起计算(所以不能从个别的列取回数据).
  * GROUP BY子句中列出的每个列都必须是检索列或有效的表达式.如果在SELECT中使用表达式,则必须在GROUP BY子句中指定相同的表达式,不能使用别名.
  * 除聚集计算语句外,SELECT语句中的每个列都必须在GROUP BY子句中给出
  * 如果分组列种具有NULL值,则NULL将作为一个分组返回,如果列中有多行NULL值,它们将分为一组
  * GROUP BY字句必须出现在WHERE子句之后,ORDER BY字句之前.
<a id="markdown-181-p86-having和where的差别" name="181-p86-having和where的差别"></a>
## 18.1. p86-HAVING和WHERE的差别
WHERE在数据分组前进行过滤,HAVING在数据分组后进行过滤.

```sql
SELECT vend_id, COUNT(*) AS num_prods
FROM products
WHERE prod_price >= 10
GROUP BY vend_id
HAVING COUNT(*) >= 2
```

这行语句中,第一行是使用了聚集函数的基本SELECT,它与前面的例子很相像.WHERE字句过滤所有prod_price至少为10的行.然后按vend_id分组数据,HAVING子句过滤计数为2或2以上的分组.

<a id="markdown-19-p88-select子句顺序" name="19-p88-select子句顺序"></a>
# 19. p88-SELECT子句顺序

子句 |说明|是否必须使用
-|-|-
 SELECT    | 要返回的列或表达式  | 是            
 FROM      | 从中检索数据的表   | 仅在从表选择数据时使用  
 WHERE     | 行级过滤       | 否            
 GROUP BY  | 分组说明       | 仅在按组计算聚集时使用  
 HAVING    | 组级过滤       | 否            
 ORDER BY  | 输出排序顺序     | 否            
 LIMIT     | 要检索的行数     | 否            

<a id="markdown-20-p97-联结" name="20-p97-联结"></a>
# 20. p97-联结
很好地理解联结及其语法是学习SQL的一个极为重要的组成部分.如果数据存储在多个表中,怎样用单条SELECT语句检索出数据?\\
答案是使用联结.简单地说,联结是一种机制,用来在一条SELECT语句中关联表,因此称之为联结.使用特殊的语法,可以联结多个表返回一组输出,联结在运行时关联表中正确的行.

<a id="markdown-201-p98-example" name="201-p98-example"></a>
## 20.1. p98-example

```sql
SELECT vend_name, prod_name, prod_price
FROM vendors, products
WHERE vendors.vend_id = products.vend_id
ORDER BY vend_name, prod_name;
```

<a id="markdown-202-p101-笛卡儿积" name="202-p101-笛卡儿积"></a>
## 20.2. p101-笛卡儿积
由没有联结条件的表关系返回的结果为笛卡儿积.检索出的行的数目将是第一个表的行数乘以第二个表的行数.

<a id="markdown-203-p105-使用哪种语法" name="203-p105-使用哪种语法"></a>
## 20.3. p105-使用哪种语法?
ANSI SQL规范首选INNER JOIN语法.此外,尽管使用WHERE子句定义联结的确比较简单,但是使用明确的联结语法能够确保不会忘记联结条件,有时候这样做也能影响性能.

<a id="markdown-204-p108-自联结而不是子查询" name="204-p108-自联结而不是子查询"></a>
## 20.4. p108-自联结而不是子查询
自联结通常作为外部语句用来替代从相同表中检索数据时使用的子查询语句.虽然最终的结果是相同的,但有时候处理联结远比处理子查询快得多,应该试一下两种方法,以确定哪一种的性能更好.

<a id="markdown-205-p106-别名的作用" name="205-p106-别名的作用"></a>
## 20.5. p106-别名的作用
  * 缩短SQL语句
  * 允许在单条SELECT语句中多次使用相同的表


<a id="markdown-206-p111-使用带聚集函数的联结" name="206-p111-使用带聚集函数的联结"></a>
## 20.6. p111-使用带聚集函数的联结
```sql
SELECT customers.cust_name,
       customers.cust_id,
       COUNT(orders.order_num) AS num_ord
FROM customers INNER JOIN orders
ON customers.cust_id = orders.cust_id
GROUP BY customers.cust_id;
```

<a id="markdown-207-p112-使用联结和联结条件" name="207-p112-使用联结和联结条件"></a>
## 20.7. p112-使用联结和联结条件
  * 注意所使用的联结类型,一般我们使用内部联结,但使用外部联结也是有效的
  * 保证使用正确的联结条件,否则将返回不正确的数据
  * 应该总是提供联结条件,否则会得出笛卡尔积

<a id="markdown-21-p114-组合查询和多个where条件" name="21-p114-组合查询和多个where条件"></a>
# 21. p114-组合查询和多个WHERE条件
任何具有多个WHERE子句的SELECT语句都可以作为一个组合查询给出.\\
利用UNION,可把多条查询的结果作为一条组合查询返回,不管它们的结果中包含还是不包含重复.使用UNION可极大地简化复杂的WHERE字句.

<a id="markdown-22-p115-union规则" name="22-p115-union规则"></a>
# 22. p115-UNION规则
  * UNION必须由两条或两条以上的SELECT语句组成,语句之间用关键字UNION分割
  * UNION中的每个查询必须包含相同的列.表达式或聚集函数(各个列不需要相同的次序列出)
  * 列数据类型必须兼容,类型不必完全相同,但必须是DBMS可以隐含地转换的类型(例如,不同的数值类型或不同的日期类型)

<a id="markdown-23-p116-union-all" name="23-p116-union-all"></a>
# 23. p116-UNION ALL
在使用UNION时,重复的行被自动取消.如果想返回所有匹配行,可使用UNION ALL而不是UNION.

<a id="markdown-24-p134-insert操作可能很好耗时" name="24-p134-insert操作可能很好耗时"></a>
# 24. p134-INSERT操作可能很好耗时
数据库经常被多个客户访问,对处理什么请求以及用什么次序处理进行管理是MySQL的任务.INSERT操作可能很耗时(特别是有很多索引需要更新时)而且它可能降低等待处理的SELECT语句的性能.

<a id="markdown-241-p136-提高插入性能的insert用法" name="241-p136-提高插入性能的insert用法"></a>
## 24.1. p136-提高插入性能的INSERT用法
```sql
INSERT INTO customers(cust_name,
    cust_address,
    cust_city,
    cust_state,
    cust_zip,
    cust_country)
VALUES(
        'Pep E. LaPew',
        '100 Main Street',
        'Los Angeles',
        'CA',
        '90046',
        'USA'
      ),
      (
        'M. Martian',
        '42 Galaxy Way',
        'New York',
        'NY',
        '11213',
        'USA'
      );
```
此技术可以提高数据库处理的性能,因为MySQL用单条INSERT语句处理多个插入比使用单条INSERT语句快.


<a id="markdown-25-p141-删除数据不省略where" name="25-p141-删除数据不省略where"></a>
# 25. p141-删除数据不省略WHERE

<a id="markdown-26-p142-更快地删除数据" name="26-p142-更快地删除数据"></a>
# 26. p142-更快地删除数据
如果想从表中删除所有行,不要使用DELETE,可以使用TRUNCATE TABLE语句,它完成相同的工作,但速度更快(TRUNCATE实际是删除原来的表并重新创建一个表,而不是逐行删除表中的数据)


<a id="markdown-27-p151-mysql引擎" name="27-p151-mysql引擎"></a>
# 27. p151-MySQL引擎
  * InnoDB是一个可靠的事务处理引擎,它不支持全文本搜索
  * MEMORY在功能等同与MyISAM,但由于数据存储在内存,速度很快
  * MyISAM是一个性能极高的引擎,它支持全文本搜素,但不支持事务处理

<a id="markdown-28-p151-外键不能跨引擎" name="28-p151-外键不能跨引擎"></a>
# 28. p151-外键不能跨引擎
即使用一个引擎的表不能引用具有使用不同引擎的表的外键.


<a id="markdown-29-p153-小心使用alter-table" name="29-p153-小心使用alter-table"></a>
# 29. p153-小心使用ALTER TABLE
使用ALTER TABLE时要极为小心,应该在进行改动前做一个完整的备份(模式和数据的备份).数据库表的更改不能撤销,如果增加了不需要的列,可能不能删除它们,类似地,如果删除了不应该删除的列,可能会丢失该列种的所有数据.


<a id="markdown-30-p156-为什么使用视图" name="30-p156-为什么使用视图"></a>
# 30. p156-为什么使用视图?
  * 重用SQL语句
  * 简化复杂的SQL操作,在编写查询后,可以方便地重用它而不必知道它的基本查询细节
  * 使用表的组成部分而不是整个表
  * 保护数据.可以给用户授予表的特定部分的访问权限而不是整个表的访问权限
  * 更改数据格式和显示.试图可返回与底层表的表示和格式不同数据

视图用CREATE VIEW语句来创建,更新视图时,可以用DROP再用CREATE,也可以直接用CREATE OR REPLACE VIEW.

<a id="markdown-31-p164-为什么使用存储过程" name="31-p164-为什么使用存储过程"></a>
# 31. p164-为什么使用存储过程?
  * 通过把处理封装在容易使用的单元中,简化复杂的操作
  * 由于不要求反复建立一系列处理步骤,这保证了数据的完整性
  * 简化对变动的管理,如果表名,列名或业务逻辑有变化,只需要更改存储过程的代码.使用它的人员甚至不需要知道这些变化
  * 提高性能,因为使用存储过程比使用单独的SQL语句更快
  * 存在一些只能用在单个请求中的MySQL元素和特性,存储过程可以使用它们来编写功能更强更灵活的代码

<a id="markdown-32-p174-使用游标" name="32-p174-使用游标"></a>
# 32. p174-使用游标
游标(cursor是一个存储在MySQL服务器上的数据库查询,它不是一条SELECT语句,而是被该语句检索出来的结果集,在存储了游标之后,应用程序可以根据需要滚动或浏览其中的数据.\\
**只能用于存储过程**,不像多数DBMS,MySQL游标只能用于存储过程(和函数)


<a id="markdown-33-p186-关于触发器的进一步介绍" name="33-p186-关于触发器的进一步介绍"></a>
# 33. p186-关于触发器的进一步介绍
  * 与其他DBMS相比,MySQL 5 中支持的触发器相当初级.未来的MySQL版本中有一些改进和增强触发器支持的计划.
  * 创建触发器可能需要特殊的安全访问权限,但是,触发器的执行是自动的.如果INSERT,UPDATE或DELETE语句能够执行,则相关的触发器也能执行
  * 应该用触发器来保证数据的一致性(大小写,格式等).在触发器中执行这种类型的处理的优点是它总是进行这种处理,而且是透明地进行,与客户机应用无关
  * 触发器的一种非常有意义的使用是创建审计跟踪.使用触发器,把更改记录到另一个表非常容易
  * 遗憾的是,MySQL触发器中不支持CALL语句,这表示不能从触发器内调用存储过程.所需的存储过程代码需要复制到触发器内.

<a id="markdown-34-p188-事务处理" name="34-p188-事务处理"></a>
# 34. p188-事务处理
事务处理是一种机制,用来管理必须成批执行的MySQL操作,以保证数据库不包含不完整的操作结果.利用事务处理,可以保证一组操作不会中途停止,它们或者作为整体执行,或者完全不执行.如果没有错误发生,整组语句提交给数据库表.如果发生错误,则进行回退以回复数据库到某个已知且安全的状态.

<a id="markdown-341-p189-事务处理的几个知识点" name="341-p189-事务处理的几个知识点"></a>
## 34.1. p189-事务处理的几个知识点
  * 事务(transaction)指一组SQL语句
  * 回退(rollback)指撤销指定SQL语句的过程
  * 提交(commit)指将未存储的SQL语句结果写入数据库表
  * 保留点(savepoint)指事务处理中设置的临时占位符(place-holder),你可以对它发布回退(与回退整个事务处理不同)

<a id="markdown-342-p190-哪些语句可以回退" name="342-p190-哪些语句可以回退"></a>
## 34.2. p190-哪些语句可以回退?
事务处理用来管理INSERT,UPDATE和DELETE语句

<a id="markdown-343-p192-更改默认的提交行为" name="343-p192-更改默认的提交行为"></a>
## 34.3. p192-更改默认的提交行为
默认的MySQL行为是自动提交所有更改.换句话说,任何时候你执行一条MySQL语句,该语句实际上都是针对表执行的,而且所有的更改立即生效,为指示MySQL不自动提交更改,需要使用以下语句:**SET autocommit=0;**

<a id="markdown-35-p202-访问权限" name="35-p202-访问权限"></a>
# 35. p202-访问权限

权限|说明
-|-
 ALL                      | 除GRANT OPTION外的所有权限                                                  
 ALTER                    | 使用ALTER TABLE                                                        
 ALTER ROUTINE            | 使用ALTER PROCEDURE和DROP PROCEDURE                                     
 CREATE                   | 使用CREATE TABLE                                                       
 CREATE ROUTINE           | 使用CREATE PROCEDURE                                                   
 CREATE TEMPORARY TABLES  | 使用CREATE TEMPORARY TABLE                                             
 CREATE USER              | 使用CREATE USER,DROP USER,RENAME USER和REVOKE ALL PRIVILEGES            
 CREATE VIEW              | 使用CREATE VIEW                                                        
 DELETE                   | 使用DELETE                                                             
 DROP                     | 使用DROP TABLE                                                         
 EXECUTE                  | 使用CALL和存储过程                                                          
 FILE                     | 使用SELECT INTO OUTFILE 和 LOAD DATA INFILE                             
 GRANT OPTION             | 使用GRANT和REVOKE                                                       
 INDEX                    | 使用CREATE INDEX和DROP INDEX                                            
 INSERT                   | 使用INSERT                                                             
 LOCK TABLES              | 使用LOCK TABLES                                                        
 PROCESS                  | 使用SHOW FULL PROCESSLIST                                              
 RELOAD                   | 使用FLUSH                                                              
 REPLICATION CLIENT       | 服务器位置的访问                                                             
 REPLICATION SLAVE        | 由复制从属使用                                                              
 SELECT                   | 使用SELECT                                                             
 SHOW DATABASES           | 使用SHOW DATABASES                                                     
 SHOW VIEW                | 使用SHOW CREATE VIEW                                                   
 SHUTDOWN                 | 使用mysqladmin shutdown(用来关闭mysql)                                     
 SUPER                    | 使用CHANGE MASTER,KILL,LOGS,PUGER,MASTER和SET GLOBAL.还允许mysqladmin调试登录  
 UPDATE                   | 使用UPDATE                                                             
 USAGE                    | 无访问权限                                                                


<a id="markdown-36-p205-备份数据" name="36-p205-备份数据"></a>
# 36. p205-备份数据
  * 使用命令行实用程序mysqldump转储所有数据库内容到某个外部文件.在进行常规备份前这个实用程序应该正常运行,以便能正确地备份转储文件
  * 可用命令行实用程序mysqlhotcopy从一个数据库复制所有数据(并非所有数据库引擎都支持这个实用程序)
  * 可以使用MySQL的BACKUP TABLE或SELECT INTO OUTFILE转储所有数据到某个外部文件.这两条语句都接受将要创建的系统文件名,此系统文件必须不存在,否则会出错.数据可以用RESTORE TABLE来复原

<a id="markdown-37-p206-数据库维护" name="37-p206-数据库维护"></a>
# 37. p206-数据库维护

<a id="markdown-371-p205-检查表键是否正确" name="371-p205-检查表键是否正确"></a>
## 37.1. p205-检查表键是否正确
```sql
ANALYZE TABLE
```

<a id="markdown-372-p205-对表进行检查" name="372-p205-对表进行检查"></a>
## 37.2. p205-对表进行检查
```sql
CHECK TABLE orders, orderitems
```

<a id="markdown-373-p207-诊断启动问题" name="373-p207-诊断启动问题"></a>
## 37.3. p207-诊断启动问题

  * --help显示帮助
  * --safe-mode装载减去某些最佳配置的服务器
  * --verbose显示全文文本消息
  * --version显示版本信息然后退出

<a id="markdown-374-p207-查看日志文件" name="374-p207-查看日志文件"></a>
## 37.4. p207-查看日志文件
  * 错误日志,日志名为hostname.err,位于data目录中,此日志名可用--log-error命令行选项修改
  * 查询日志,日志名为hostname.log,位于data目录中,此日志名可用--log命令行选项更改
  * 二进制日志,日志名为hostname-bin,位于data目录中,此日志名可用--log-bin命令行选项修改
  * 缓慢查询日志,日志名为hostname-slow.log,位于data目录中,此日志名可用--log-slow-queries命令行选项修改

<a id="markdown-38-p209-改善性能" name="38-p209-改善性能"></a>
# 38. p209-改善性能
  * 查看设置,SHOW VARIABLES; SHOW STATUS;可能需要调整内存分配,缓冲区大小
  * MySQL是一个多用户多线程的DBMS,换言之,它经常同时执行多个任务.如果遇到显著的性能不良,可使用SHOW PROCESSLIST显示所有活动进程,你还可以用KILL命令终结某个特定的进程
  * 总有不止一种方法编写同一条SELECT语句.应该试验联结,并,子查询等,找出最佳方法
  * 使用**EXPLAIN**语句让MySQL解释它如何执行一条SELECT语句
  * 存储过程执行得比一条一条地执行其中的各条MySQL语句快
  * 应该总是使用正确的数据类型
  * 绝不要检索比需求还多的数据.换言之不要用SELECT *
  * 在导入数据时,应该关闭自动提交.你可能还想删除索引,然后在导入完成后再重建它们
  * 必须索引数据库表以改善数据检索的性能.确定索引什么不是一件微不足道的任务,需要分析使用的SELECT语句找出重复的WHERE和ORDER BY语句
  * 你的SELECT语句中有一系列复杂的OR条件吗?通过使用多条SELECT语句和连接它们的UNION语句,你能看到极大的性能改进
  * 索引改善数据检索的性能,但损害数据插入,删除和更新的性能.如果你有一些表,它们收集数据且不经常被搜索,则在有必要之前不要索引它们(索引可根据需要添加和删除)
  * LIKE很慢.一般来说,最好使用FULLTEXT而不是LIKE
  * 数据库是不断变化的实体.一组优化良好的表一会儿后可能就面目全非了.由于表的使用和内容的更改,理想的优化和配置也会改变
  * 最重要的规则就是,每条规则在某些条件下都会被打破

<a id="markdown-39-p225-串数据类型" name="39-p225-串数据类型"></a>
# 39. p225-串数据类型

数据类型|说明
-|-
 CHAR        | 1~255个字符的定长串.它的长度必须在创建时指定,否则MySQL假定为CHAR(1)                   
 VARCHAR     | 长度可变,最多不超过255字节.如果在创建时指定为VARCHAR(n),则可存储0到n个字符的变长串(其中n<=255)  
 TINYTEXT    | 与TEXT相同,但最大长度为255字节                                           
 MEDIUMTEXT  | 与TEXT相同,但最长度为16k                                              
 TEXT        | 最大长度为64K的变长文本                                                 
 LONGTEXT    | 与TEXT相同,最大长度为4GB                                              
 SET         | 接受最多64个串组成一个预定义集合的零个或多个串                                      
 ENUM        | 接受最多64K个串组成的预定义集合的某个串                                         

<a id="markdown-40-p226-数值数据类型" name="40-p226-数值数据类型"></a>
# 40. p226-数值数据类型

类型|说明
-|-
 BIT        | 位字段, 1~64位.                                                                            
 BOOLEAN    | 布尔标志,或者为0或者为1,主要用于开/关标志                                                                
 TINYINT    | 整数值,支持-128~127(如果是UNSIGNED,为0~255)的数                                                   
 SMALLINT   | 整数值,支持-32768~32767(如果是UNSIGNED,为0~65535的数                                              
 MEDIUMINT  | 整数值,支持-8388608~8388607(如果是UNSIGNED,为0~16777215)的数                                      
 INT        | 整数值,支持-2147483648~2147483647(如果是UNSIGNED,为0~4294967295)的数                              
 BIGINT     | 整数值,支持-9223372036854775808~9223372036854775807(如果是UNSIGNED,为0~18446744073709551615)的数  
 REAL       | 4字节的浮点值                                                                                
 FLOAT      | 单精度浮点值                                                                                 
 DOUBLE     | 双精度浮点值                                                                                 
 DECLIMAL   | 精度可变的浮点值                                                                               

<a id="markdown-41-p227-日期和时间数据类型" name="41-p227-日期和时间数据类型"></a>
# 41. p227-日期和时间数据类型

类型|说明
-|-
 DATE       | 表示1000-01-01~9999-12-31的日期,格式为YYYY-MM-DD               
 TIME       | 格式为HH:MM:SS                                            
 DATETIME   | DATE和TIME的组合                                           
 TIMESTAMP  | 功能和DATETIME相同                                          
 YEAR       | 用2位数字表示,范围是70(1970年)~69(2069年),用4位数字表示,范围是1901年~2155年  

<a id="markdown-42-p227-二进制数据类型" name="42-p227-二进制数据类型"></a>
# 42. p227-二进制数据类型

类型|说明
-|-
 TINYBLOB    | 最大长度为255字节  
 BLOB        | 最大长度为64KB   
 MEDIUMBLOB  | 最大长度为16MB   
 LONGBLOB    | 最大长度为4GB    



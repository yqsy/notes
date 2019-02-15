<!-- TOC -->

- [1. 说明](#1-说明)
- [2. 实现方法选择](#2-实现方法选择)
    - [2.1. 列表](#21-列表)
    - [2.2. 选择](#22-选择)
- [3. 参考资料](#3-参考资料)

<!-- /TOC -->


<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

把json拿来对比

数据类型|实例值|解析思路|存储|bencode|含义
-|-|-|-|-|-
null|null|n开头|nil||
boolean|true false| t f 开头|bool||
string|""|"开头|string|数字:字符串内容 (4:spam) | 字符串spam
number|浮点数|默认|float64| ti开头e末尾 (i42e) | 数字42
array|[]|[开头|[]interface{}| l开头e末尾 (l4:spami42ee) | [spam,42]
object|{...}|{开头|map[string]interface{}| d开头e末尾 (d3:bar4:spam3:fooi42ee) | {"bar":"spam","foo":42}


<a id="markdown-2-实现方法选择" name="2-实现方法选择"></a>
# 2. 实现方法选择

参考几种语言的实现: python,js,java,go的json解析的方法. 我们主要关注异常情况:

```bash
# 1. 需求是1,输入是"1", 类型不匹配怎么处理
"{"num": "1"}"

# 2. 读取 "name1", key不存在怎么处理
{"name": "yq"}
```

python
```bash
# 情况一: -> TypeError
import json
x = '{"num": "1"}'
y = json.loads(x)
y["num"] += 1

# 情况二: -> KeyError
import json
x = '{"name": "yq"}'
y = json.loads(x)
print(y["name1"])
```

js
```js
// 情况一: -> 不严谨,不确定. 本地是数字,远程传过来一个字符串"数字". 做加法时逻辑会出错. 
var str = '{"num": "1"}';
var obj = JSON.parse(str);
// 只能: ensure(typeof obj.num === 'number');
obj["num"] += 1;
console.log(obj["num"]);

//               +    -     *     /
// 字符 数字    字符串 数字  数字   数字
// 数字 字符串  字符串  数字  数字  数字

// 情况二: -> 不严谨,不确定. 对象不存在,怎么可以和字符串判断呢. 逻辑不严谨.
var str = '{"name": "yq"}';
var obj = JSON.parse(str);
// 只能: 
// ensure(obj["name1"], "name1");
// ensure(typeof obj["name1"] === 'string', "name1");
if (obj["name1"] === "yq")
{
    console.log("yq");
}
```

java
```java
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

public class Test {
    public static void main(String[] args) {
        // 情况1:
        String jsonString = "{\"num\": \"1\"}";
        GsonBuilder builder = new GsonBuilder();
        builder.setPrettyPrinting();
        Gson gson = builder.create();
        JsonTest1 jsontest1 = gson.fromJson(jsonString, JsonTest1.class);
        System.out.println(jsontest1);

        // 情况2:
        jsonString = "{\"name\": \"yq\"}";
        JsonTest2 jsontest2 = gson.fromJson(jsonString, JsonTest2.class);
        System.out.println(jsontest2);
    }
}

class JsonTest1 {
    private int num;

    public String toString() {
        return "num: " + num;
    }
}

class JsonTest2 {
    private String name1;

    public String toString() {
        return "name: " + name1;
    }
}
```

go
```go
package main

import "encoding/json"

type Test1 struct {
	Num int `json:"num"`
}

type Test2 struct {
	Name1 string `json:"name1"`
}

// 情况一: error 返回值处理
func JsonTest1() {
	jsonString := "{\"num\": \"1\"}"
	test1 := Test1{}
	err := json.Unmarshal([]byte(jsonString), &test1)
	if err != nil {
		print("json.Unmarshal err\n")
	}
}

// 情况二: 默认值
func JsonTest2() {
	jsonString := "{\"name\": \"yq\"}"
	test2 := Test2{}
	err := json.Unmarshal([]byte(jsonString), &test2)
	if err != nil {
		print("json.Unmarshal err")
	}
	print(test2.Name1)
}

func main() {
	JsonTest1()

	JsonTest2()
}
```

<a id="markdown-21-列表" name="21-列表"></a>
## 2.1. 列表

语言|处理方式|类型不匹配|key不存在
-|-|-|-
python|解析到动态对象|异常|异常
js|解析到动态对象|不严谨|不严谨
java|反射解析到静态类|不严谨|null
go|反射解析到静态类|返回err|默认空值


<a id="markdown-22-选择" name="22-选择"></a>
## 2.2. 选择


综上,我们选择的方案还是go标准库的方案,其准确性强以及编码量更少.  


<a id="markdown-3-参考资料" name="3-参考资料"></a>
# 3. 参考资料

* https://en.wikipedia.org/wiki/Bencode

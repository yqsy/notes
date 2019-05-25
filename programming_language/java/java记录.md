
<!-- TOC -->

- [1. 说明](#1-说明)
- [2. 参考资料](#2-参考资料)

<!-- /TOC -->

# 1. 说明

代码:
```java
class HelloWorld 
{ 
    public static void main(String args[]) 
    { 
        System.out.println("Hello, World"); 
    } 
} 
```

构建:
```bash
# 源码编译成字节码 (.class)
javac HelloWorld.java

# 运行字节码
java HelloWorld

# 打包jar (生成什么jar, 执行的类名?, 文件名)
jar cvfe HelloWorld.jar HelloWorld HelloWorld.class

# 执行jar
java -jar HelloWorld.jar
```

# 2. 参考资料

* https://introcs.cs.princeton.edu/java/11hello/HelloWorld.java.html
* https://stackoverflow.com/questions/1238145/how-to-run-a-jar-file

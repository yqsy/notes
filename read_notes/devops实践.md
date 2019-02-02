---
title: devops实践
date: 2017-12-3 15:33:54
categories: [读书笔记]
---


<!-- TOC -->


<!-- /TOC -->


1.一个设计良好的持续交付流水线大约只需要几分钟就可以把提交的代码部署到生产环境

2.当一个提交发生时,构建服务器就从版本控制系统上更新自己本地的源代码.随即,构建代码并运行测试来验证代码提交的质量

3.当构建服务器确认了代码质量并将其编译成可交付物时,将这些编译好的二进制工件存放在工件库

4.Red Hat / centos 系统使用RPM格式的包, Debain / Ubuntu 使用deb的格式的包,只用一条命令就可以从二进制库里下载并安装这些包到服务器上

5.如果工作不正常,一次部署可能带来几天预期之外的烦恼

* 数据库结构变更
* 测试数据与预期不匹配
* 部署依赖于某人,而这个人没空
* 变更伴随着一堆没有实际作用的官僚流程


6.当升级数据库时,我们需要考虑状态,因为一个数据库几乎没有什么逻辑和结构.


7.**Liquibase**记录数据库变化

8.**Tolerant Reader** 服务的消费端应该忽略那些它无法识别的数据

9.有许多方法可以提供集中式代码库: **Github,Bitbucjer,GitLab**. 或云提供商,**AWS或Rackspace**

10.质量保证人员把自动化测试放在源代码里,诸如**Selenium**和**Junit**

11.文档不应该是**word**,**excel**,而**应该是wiki**,企业应该要花点精力让所有角色都可以轻松访问文档

12.Git flow是一个分支策略,但是太复杂了 
  * 主干分支,所有提交都打上标签
  * 开发分支,用来开发下一个发行版,合并到主干
  * 功能分支,区分不同的功能,合并到开发分支
  * 热修复分支,合并到开发分支,再合并到主干分支

13.需要在已发布的代码里修复缺陷时 
  * 创建一个缺陷修复分支在其上部署到生产环境
  * 功能开关

14.工件版本命名
通常转换成带有三四个部分的版本号:
  * 第一部分代表了主要的代码变更
  * 第二部分是次要变更,API向后兼容
  * 第三部分表示修复了缺陷
  * 第四部分可以是一个构建号 
参考http://semver.org

15.**Maven,Jaba**快照策略违背了一个基本的测试原则:部署到生产环境的二进制产品应该与测试的产品完全一致

16.增加密钥和新建项目的工作如果太频繁就太麻烦了,应该使用处理认证的中央服务器**LDAP,phpLDAPadmin**

17.**Git无法管理二进制文件**,这个问题的解决方案现在有如下竞争者**Git LFSGitHub**支持,**Git AnnexGitLab**支持,仅企业

18.**Gerrit是基于Git的代码审查工具**,由资深的开发者审查经验不足的开发者的变更.可以与docker搭配


19.构建系统历史 
  * Java Maven,Gradle,Ant
  * c c++ , make
  * JavaScript Grunt
  * Scala sbt
  * Rubt Rake

20.**FPM**是创建RPM,Debian还有其他种类的包的一个非常便利的方法

21.如果构建快到不至于让人感到无聊,开发者将会对频繁提交充满热情,集成问题将会更早出现

22.构建方案 
  * Jenkins 主流
  * Travis CI 托管方案
  * Buildbot Python编写的构建服务器
  * ThoughtWorks出品的Go服务器
  * Bamboo Atlassian 提供
  * GitLab支持

23.质量指标校验,**Sonar**

24.单元测试**Junit**,c#对应**NUnit**,网站前端测试**Selenium**

25.**Mocking,如果单元测试需要后端数据库在线,甚至需要独占访问,这可不方便了**,Mockito是一个Java的mock框架,被移植到了python

26.测试覆盖率,测试用例中执行的应用程序代码的百分比,**Cobertura,jcoverage,Clover**

27.**Selenium**自动化Gui测试,可以通过检查文档对象模型

28.部署代码用**Puppet,Ansible,Salt,PalletOps**

29.配置文件的格式**XML,YML,JSON,INI**

30.抽象底层硬件和在相互竞争的不同的虚拟机之间调度硬件资源的组建称为虚拟机监控程序**(hypervisor)**

31.虚拟化解决方案:**VMWare,KVM,Xen,VirtualBox,Vagrant虚拟机配置管理系统**

32.监控方案Nagios,Munin描绘服务器统计数据如内存使用,Hugin

33.RRD 轮询数据库Round-robin Database

34.**Ganglia**是大型集群的绘图和监控解决方案,使用RRD作为数据库存储和绘图,**图片很赞**

35.日志处理框架ELK,**Elasticsearch保存日志且索引**,**Logstash开源日志框架**,**Kibana日志搜索和可视化web界面**.**文件,数据库,网络进程,日志文件的轮替和归档.**

36.问题跟踪器,Bugzilla面向大众的大型跟踪器,Redmine与Trac相似,Gitlab也有问题跟踪器,Jira收费,无wiki, Trac主要卖点:wiki,问题跟踪与库紧密集成

37.wiki系统,Confluence Wiki,Fisheye代码浏览器

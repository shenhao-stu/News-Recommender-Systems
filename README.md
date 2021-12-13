﻿﻿﻿# News-Recommender-Systems

本项目是参考**Datawhale推荐系统团队**的开源教程：[Fun-Rec](https://github.com/datawhalechina/fun-rec) 中的推荐系统实战内容进行优化。从数据库、前端框架、后端框架和前后端交互的角度出发，记录笔者遇到的坑和如果填坑的过程。同时对于原项目中的部分代码和算法进行优化和较为清晰的介绍。帮助每一位visitor能够自己动手完成属于自己的新闻推荐系统项目。

## 学习教程

🤗 **GitHub地址** ：https://github.com/datawhalechina/fun-rec

## 学习安排

- [ ] **Task01：熟悉新闻推荐系统基本流程（2天）**

  截止日期：2021-12-15 03:00

- [ ] **Task02：数据库的基本使用（4天，MySQL、Mongodb、Redis）**

  截止日期：2021-12-19 03:00

- [ ] **Task03：离线物料系统的构建（4天，爬虫、构建画像、物料入库）**

  截止日期：2021-12-23 03:00

- [ ] **Task04：前后端基础及交互（5天，前端基础、Flask基础、后端请求逻辑）**

  截止日期：2021-12-28 03:00

- [ ] **Task05：推荐流程的构建（3天）**

  截止日期：2021-12-31 03:00




### Task01 熟悉推荐系统基本流程

飞书直播讲解新闻推荐系统基本流程和代码结构。

视频链接：https://datawhale.feishu.cn/minutes/obcnzns778b725r5l535j32o


### Task02 数据库的基本使用

【mysql, mongodb, redis】

github上给出了参考资料，其实也是用来作为查询的，因为每块的内容都非常的多，只有当自己忘记命令了，找相关资料来学习一下。对于数据库来说，需要掌握的程度有下面几个要求：

1. 了解不同数据库的特点
2. 掌握linux下数据库的安装
3. 了解linux下数据库的常用命令（增删改查）
4. 熟练python调用数据库相关包的用法，对于不同的数据库可能有不同的包, 包中的方法也只需要掌握增删改查
   1. mysql推荐学习sqlalchemy，这块的内容在[Flask简介及基础]()
   2. mongodb推荐学习pymongo
   3. redis推荐学习python中的redis包

注意：仅仅需要掌握增删改查的基本命令就够了，不要在数据库上花太多的时间，否则后面跟不上



### Task03 离线物料系统的构建

学习[自动化构建用户及物料画像]()，学习具体的代码的时候建议先把项目中所有文件中的README.md先看看，了解每个包大概是在干什么，然后再根据教程一点一点去理解流程，建议先梳理代码流程，等到最后自己觉得整个流程自己比较熟悉了，就可以慢慢的去看代码的实现细节。



### Task04 前后端基础及交互

前后端交互这块的内容也比较多，需要大家了解一些前后端框架的基础，建议大家可以把[前端基础及Vue实战]()和[Flask简介及基础]()好好看看，这两个文档主要是帮助大家了解前后端框架的基础，并且是直接跟项目代码相关的内容，不相关的内容都没有写进去，如果想进一步学习的话可以搜索其他的相关资料。

等前面的两个基础文档看完了之后，就可以好好的来看看后端代码的逻辑了，对于大家来说前端的逻辑不需要花什么时间，简单了解一下就行，但是对于后端每个请求的逻辑还是建议大家都去看看，因为每个逻辑都不难理解。



### Task05 用户倒排索引表的构建

当大家了解了新闻物料的构建以及前后端交互的基础之后，剩下的就是去了解推荐流程在当前项目中是怎么实现的了，这个可以参考[推荐流程的构建]()中的内容。




# 目标

如果大家最终在学习完本次的组队学习内容，可以理解下面这张流程图的话，那基本上就很不错了。因为内容真的比较多，而且比较偏向实战，如果要真的弄懂里面的详细流程需要大家花不少时间在看源码上面。

![](https://gitee.com/shenhao-stu/News-Recommender-Systems/raw/master/imgs/structure.png)

## 内容导航

**Chapter 1 离线物料系统的构建**

- 1.Mysql基础
- 2.MongoDB基础
- 3.Redis基础
- 4.Scrapy基础及新闻爬取实战
- 5.自动化构建用户及物料画像

**Chapter 2 前后端基础及交互**

- 1.前端基础及Vue实战
- 2.Flask简介及基础
- 3.前后端交互

**Chapter 3 推荐流程的构建**

- 1.推荐系统流程构建

## 前端展示

**新闻推荐系统前端显示页面及后端系统架构（项目没有任何商用价值仅供入门者学习**）

<div align=center> <img src="https://gitee.com/shenhao-stu/News-Recommender-Systems/raw/master/imgs/web_show.png" style="zoom:57%;" />
</div>


## 项目架构图

<div align=center>
<img src="https://gitee.com/shenhao-stu/News-Recommender-Systems/raw/master/imgs/structure.png" alt="Fun-Rec新闻推荐系统" style="zoom:55%;" />
</div>





## 关注我们

<div align=center>
<p>扫描下方二维码关注公众号：Datawhale</p>
<img src="https://gitee.com/shenhao-stu/News-Recommender-Systems/raw/master/imgs/qrcode.jpeg" width = "180" height = "180">
</div>




## LICENSE
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="知识共享许可协议" style="border-width:0" src="https://img.shields.io/badge/license-CC%20BY--NC--SA%204.0-lightgrey" /></a>

本作品采用<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">知识共享署名-非商业性使用-相同方式共享 4.0 国际许可协议</a>进行许可。

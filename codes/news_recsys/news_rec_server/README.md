# 新闻推荐系统

## 项目环境

**python环境**

1. 安装`conda`环境
2. 创建`conda`虚拟环境： `conda create -n news_rec_py3 python==3.8`
3. 进入虚拟环境： `conda activate news_rec_py3`
4. 安装依赖文件： `pip install -r requirements.txt`
5. 注意安装并启动snowflake（这个是用来生成用户id的），在requirements.txt中已经有了，所以只需要启动就行
   - 启动：`snowflake_start_server --address=127.0.0.1 --port=8910 --dc=1 --worker=1`

**数据库环境**

1. 参考 Mysql基础
2. 参考 MongoDB基础
3. 参考 Redis基础

**前端环境配置**

1. 安装node.js
2. 安装前端环境依赖：
   - 跳转到前端项目文件目录：`cd $HOME/fun-rec/codes/news_recsys/news_rec_web/Vue-newsinfo`
   - 命令行运行：`npm install`

## 数据库初始化

### 离线物料自动化构建

**每天0点爬取前一天的内容，爬取完数据再更新特征库，更新完特征库之后再更新用户的画像，然后将redis中所有数据都清空，将特征库中的前端展示信息存入redis**

配置crontab命令，命令行输入crontab -e，然后将下面命令的输入到crontab命令行中

```shell
0 0 * * * $HOME/fun-rec/codes/news_recsys/news_rec_server/scheduler/crawl_news.sh >>  $HOME/fun-rec/codes/news_recsys/news_rec_server/logs/offline_material_process.log && $HOME/fun-rec/codes/news_recsys/news_rec_server/scheduler/offline_material_and_user_process.sh >> $HOME/fun-rec/codes/news_recsys/news_rec_server/logs/material_and_user_process.log && $HOME/fun-rec/codes/news_recsys/news_rec_server/scheduler/run_offline.sh >> $HOME/fun-rec/codes/news_recsys/news_rec_server/logs/offline_rec_list_to_redis.log
```

## 项目启动

**启动后端服务**

1. 跳转到后端项目文件目录： `cd $HOME/fun-rec/codes/news_recsys/news_rec_server`
2. 启动后端服务： `python server.py `

**启动前端服务**

1. 跳转到前端项目文件目录：`cd $HOME/fun-rec/codes/news_recsys/news_rec_web/Vue-newsinfo`
2. 启动前端服务：`npm run dev`
3. 访问地址`http://localhost:5000`
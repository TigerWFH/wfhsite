# python

> 当前项目使用python@3.9.7

## 查看 python 版本

> python --version

## 创建 python 虚拟环境

> python -m venv wfhsite/env

## 激活虚拟环境

> source wfhsite/env/bin/activate

## 安装 wagtail

> pip install wagtail

## 创建 wagtail 应用

> wagtail start appName [path]
>
> wagtail start wfhsite wfhsite

## 配置 pip 镜像

> home 目录创建.pip/pip.conf

```INI
[global]
index-url = https://mirrors.aliyun.com/pypi/simple
```

## 启动应用

> python manage.py runserver
>
> 用户页面：http://127.0.0.1:8000
>
> 后台管理页面：http://127.0.0.1:8000/admin

[wagtail](./docs/wagtail.md)

> admin/admin

## 部署

> Pyhton 是编程语言，Django 和 Flask 本身是 Web 框架，并非 Web 服务，且 Django 和 Flask 自带的 runserver 和 Werkzeug 也仅仅用于开发测试环境，生产环境中处理并发的能力太弱
>
> runserver 方法是调试 Django 时经常用到的运行方式，它使用 Django 自带的
> WSGI Server 运行，主要在测试和开发中使用，并且 runserver 开启的方式也是单进程
>
> uWSGI 是一个 Web 服务器，它实现了 WSGI 协议、uwsgi、http 等协议。注意 uwsgi 是一种通信协议，而 uWSGI 是实现 uwsgi 协议和 WSGI 协议的 Web 服务器。uWSGI 具有超快的性能、低内存占用和多 app 管理等优点，并且搭配着 Nginx 就是一个生产环境了，能够将用户访问请求与应用 app 隔离开，实现真正的部署 。相比来讲，支持的并发量更高，方便管理多进程，发挥多核的优势，提升性能

## 术语

- `CGI`
- `FastCGI`
- `WSGI:Web Server Gateway Interface：`

  > `uWSGI：`是 Python 服务器，实现了 WSGI 通信规范和 uwsgi 协议
  >
  > `WSGI：`web 服务器和 web 应用通信规范
  >
  > `uwsgi：`是 WSGI 通信规范中的一种自有协议

## uWSGI 的安装和启动

> uWSGI 是一个 web 服务器，实现了 WSGI 协议、uwsgi 协议、http 等协议。Nginx 中的 HttpUwsgiModule 的作用就是与 uWSGI 服务器进行交换。
>
> uWSGI 的作用：uWSGI 是一个全功能的 HTTP 服务器，他要做的就是把 HTTP 协议转化成语言支持的网络协议。比如把 HTTP 协议转化成 WSGI 协议，让 Python 可以直接使用。

[uwsgi 配置资料](https://uwsgi-docs.readthedocs.io/en/latest/PSGIquickstart.html)

```shell
  pip install uwsgi
  uwsgi --http :8000 --module myprohetc.wsgi
  # 生产环境会使用配置文件
  uwsgi --ini uwsgi.ini
  sudo service uwsgi restart
  # 测试uwsgi
  def application(env, start_response):
    start_response("200 OK", [{'Content-Type', 'text/html'])
    return [b"Hello World"]
  # 启动
  uwsgi --http :8080 --wsgi-file test.py
```

- `uwsgi配置：`

```js
/*
[uwsgi]
uid=www-data #Ubuntu系统下默认用户名
gid=www-data #Ubuntu系统下默认用户组
project=wfhsite # 项目名
base=/home/user1 # 项目根目录

home=%(base)/Env/%(project) # 设置项目虚拟环境，Docker部署不需要
chdir=%(base)/%(project) # 设置工作目录
module=%(project).wsgi:application # wsgi文件位置

master=True # 主进程
processes=2 # 同时进行的进程数，一般

// 使用unix socket与nginx通信，仅限于uwsgi和nginx在同一主机场景
// Nginx配置中uwsgi_pass指向同一socket文件
socket=/run/uwsgi/%(project).sock

// 使用TCP socket与nginx通信
// Nginx配置中uwsgi_pass应指向uWSGI服务器IP和端口
socket=0.0.0.0:8000

// 使用http协议与nginx通信
// Nginx配置中proxy_pass指向uWSGI服务器IP和端口
http=0.0.0.0:8080

// socket权限配置
chown-socket=%(uid):www-data
chmod-socket=664

# 进程文件
pidfile=/tmp/%{project}-master.pid

# 以后台daemon进程运行，并将log日志存于temp文件夹
daemonize=/var/log/uwsgi/%(project).log

# 服务停止时，自动移除unix socket和pid文件
vacuum=True

# 为每个工作进程设置请求数的上限，当处理的请求总数超过这个量，进程回收重启
max-requests=5000
# 当一个请求被harakiri杀掉，会输出一条日志
harakiri-verbose=true
# uWsgi默认的buffersize为4096，如果请求数据超过这个量会报错。这里设置为64K
buffer-size=65536
# 如果http请求体的大小超过指定的限制，打开http body缓存，这里为64K
post-buffering=65536
# 开启内存使用情况报告
memory-report=true
# 设置平滑的重启的长等待时间（秒）
reload-mercy=10
# 设置工作进程使用虚拟内存超过多少MB就回收重启
reload-on-as=1024
*/
```

## django 数据库迁移原理

> ORM 就是将面向对象的 Python 操作转变为数据库可识别的 SQL 语句，数据库中每张表对应着 Django 中的一个模型类
>
> Django 每个应用都自带 migrations 目录，每次表结构变更操作都会生成增量的操作文件，这些文件叫做迁移文件，迁移文件也会记录依赖操作
>
> python manage.py makemigrations MODULE_NAME 在对应应用下的 migrations 下生成迁移文件
>
> python manage.py migrate MODULE_NAME 之后，对数据库进行操作
>
> 首先，根据更新文件创建或更新
>
> 其次，在 django_migrations 中增加一条数据，记录所做的操作

- `迁移步骤`

  - `首先在models.py`中创建或者修改模型
  - `运行makemigrations命令，创建增量修改迁移文件`
  - `运行migrate命令，进行迁移操作`

- `迁移回退操作：`直接对前一步的迁移文件重新手动迁移一次既完成回退操作

  > 直接跑：python manage.py migrate Four（应用名） 0003_auto_202000401_2321
  >
  > 然后手动删除 0004 迁移文件

- `重置django_migrations`指定的模块记录
  - `python manage.py migrate --fake MODEL_NAME zero`：将指定模块的迁移记录删除，仅仅删除迁移记录

## 软知识

### 版权相关内容<https://www.zhihu.com/question/19916364>

#### C 标，既 copyright 首字母外加一个圆圈

> copyright（版权）：既著作权，是指文学、艺术、科学作品的作者对其享有的权利。是知识产权的一种类型
>
> © 就是版权符号，为《世界版权公约》所规定的的版权标记，由符号 c（copyright）外加一个圆圈组成，版权所有者的姓名以及作品首次出版或注册年份三部分组成，版权标记须刊载在作品的显著部位
>
> 末尾数字表示版权时间，例如 2005-2015，表示最初在 2005 年登记，最后一次登记为 2015 年，一般软件的版权保护为 15 年
>
> All Rights Reserved，即“保留所有权利”。基本解释为：非经同意，他人不得出版或作更改

- `demo：企业和个人都可以使用`
  - 开头使用 © 符号，Copyright 或 Copr.简写字样
  - 跟随记载做平首次发表年份及更新使用年份，或二者选一
  - 跟随记载版权所有者名称
  - 跟随记载版权所有字样 All Rights Reserved，该部分可以省略

```plain
  Copyright©1996-2019 SINA Corporation, All Rights Reserved.
  Copyright©2019 Apple Inc. All Rights Reserved.
  ©2019 Baidu
  ©2019 赵三，All Rights Reserved
```

#### P 标，就是 ℗，是英文 phonogram（唱片），代表录音制作者版权所有声明

> P 标只用于实体唱片，在今天的互联网流媒体音乐时代已经不太常见了

- `demo`
  - 开头使用 ℗ 符号；
  - 跟随记载作品首次发表年份及最新使用年份（或二者选一）；
  - 跟随记载录音版权所有者名称

```plain
℗1979 zhaosi xxx
```

#### R 标，就是 ®，英文 registered（已注册）的简写，代表着商标为注册商标的含义。是商标非版权

> 商标（商品商标和服务商标）分为注册商标和非注册商标。注册商标受到法律保护的范围远远大于非注册商标，享有排他专用权等权益。R 标是为了表名商标已经经过国家商标机构登记注册，向全社会声明该商标已经登记为注册商标

- `demo`
  - 商标右侧标明 R 标 ®

#### TM 标就是 ™，英文 trademarks（商标）的简写，代表着商标为非注册商标的含义，为了与 R 标区分

- `demo`
  - 商标右侧标明 TM 标 ™

#### SM 标就是 ℠，是引文 Service markes（服务商标）的简写，代表着服务为非注册商标的含义

## chrome 修改 python 版本

> command + shift + p，输入 python select interpreter

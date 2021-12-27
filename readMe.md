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

## 部署

> runserver 方法是调试 Django 时经常用到的运行方式，它使用 Django 自带的
> WSGI Server 运行，主要在测试和开发中使用，并且 runserver 开启的方式也是单进程
>
> uWSGI 是一个 Web 服务器，它实现了 WSGI 协议、uwsgi、http 等协议。注意 uwsgi 是一种通信协议，而 uWSGI 是实现 uwsgi 协议和 WSGI 协议的 Web 服务器。uWSGI 具有超快的性能、低内存占用和多 app 管理等优点，并且搭配着 Nginx 就是一个生产环境了，能够将用户访问请求与应用 app 隔离开，实现真正的部署 。相比来讲，支持的并发量更高，方便管理多进程，发挥多核的优势，提升性能

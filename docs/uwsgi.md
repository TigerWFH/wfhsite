# uwsgi

> 在架构上是这样的，nginx 负责动态的转发和静态文件的直接访问，gunicorn 和 uwsgi 作为网关服务用来解析 http 请求，后面的 flask 只是个 application 而已，没有 server 的服务特征。

## 域名：本地域名

```js
/*
127.0.0.1 www.monkey.com
127.0.0.1 www.sit.monkey.com
127.0.0.1 www.dev.monkey.com
127.0.0.1 www.prod.monkey.com
127.0.0.1 www.cat.com
127.0.0.1 www.fish.com
*/
```

## openresty：类似 NGINX

> 使用 openresty 做 web server，承载大流量，并通过 HttpuwsgiModule 将请求转发给 uWSGI 服务器

```js
/*
    安装openresty
    brew install openresty/brew/openresty

    转发到uWSGI：
    location / {
    include uwsgi_params;
    uwsgi_pass 127.0.0.1:3031;
}
*/
```

## uWSGI: web 应用服务器

> Emperor 管理 uWSGI 的工具
> [uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/WSGIquickstart.html)

```js
/*
    安装uWSGI
    通过pip安装：pip install uwsgi
    通过下载源码编译：
    wget https://projects.unbit.it/downloads/uwsgi-latest.tar.gz
    tar zxvf uwsgi-latest.tar.gz
    cd <dir>
    make

    启动：
    uwsgi --http :9090 --wsgi-file foobar.py --master --processes 4 --threads 2 --stats 127.0.0.1:9191

    uwsgi --socket 127.0.0.1:3031 --wsgi-file foobar.py --master --processes 4 --threads 2 --stats 127.0.0.1:9191

    uwsgi --http-socket 127.0.0.1:3031 --wsgi-file foobar.py --master --processes 4 --threads 2 --stats 127.0.0.1:9191
*/
```

## 部署 Django

> uwsgi --socket 127.0.0.1:3031 --chdir /home/foobar/myproject/ --wsgi-file myproject/wsgi.py --master --processes 4 --threads 2 --stats 127.0.0.1:9191
>
> 上面命令太长了，uWSGI 支持 ini 配置文件，启动：uWSGI my.ini

```ini
; my.ini
[uwsgi]
socket = 127.0.0.1:3031
chdir=/Users/monkey/Documents/projects/wfhsite/wfhsite/
wsgi-file = wfhsite/wsgi.py
processes = 4
threads = 2
stats = 127.0.0.1:9191
```

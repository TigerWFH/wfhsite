# gunicorn<https://developer.aliyun.com/article/683283>

> gunicorn: gunicorn-绿色独角兽，是一个 Python 的 WSGI HTTP 服务器

> 在架构上是这样的，nginx 负责动态的转发和静态文件的直接访问，gunicorn 和 uwsgi 作为网关服务用来解析 http 请求，后面的 flask 只是个 application 而已，没有 server 的服务特征。

## gunicorn 提供服务方式

> gunicorn 框架对外服务的模式下有 http、tcp socket 和 unix domain socket
>
> - `http`
> - `tcp socket`
> - `unix domain socket`

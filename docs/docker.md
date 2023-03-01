# Docker

> docker 配置文件：/etc/docker/daemon.json

- `systemctl start docker`：启动 docker 服务
- `systemctl stop docker`：停止 docker 服务
- `systemctl restart docker`：重启 docker 服务
- `systemctl status docker`：查看 docker 服务状态
- `systemctl enable docker`：设置 docker 服务随机启动

## Definitions

### Dockerfile

- `docker build`：根据 dockerfile 生成镜像
  - `-f`：指定 Dockerfile 文件，默认使用当前目录下的配置文件
  - `-t`：指定生成镜像的名字[:版本]

### image

- `docker image：`查看本地镜像
- `docker search imageName：`查询镜像
- `docker pull imageName:imageVersion：`拉取镜像
- `docker rmi imageid：`删除本地镜像

### container

- `docker ps -a`：查看正在运行(所有)的容器
- `docker run -id --name=自定义容器名称 -p port:镜像端口 镜像名称`：根据镜像启动容器
- `docker stop 容器名称`：停止容器
- `docker start 容器名称`：启动容器
- `docker rm 容器名称`：删除容器

## Docker 使用

```js
/*
    docker run [options] IMAGE [COMMAND] [ARG...]
    docker run --name repo alpine/git clone https://github.com/docker/getting-started.git

    docker：二进制docker文件，用于执行相关docker命令
    run：docker run命令，运行容器
    --nam=repo：容器名称

    以上命令完整的意思可以解释为：Docker 以alpine/git 镜像创建一个容器repo，然后在容器里执行 clone https://github.com/docker/getting-started.git 

    docker：二进制docker文件，用于执行相关docker命令
    run alpine/git：docker run命令，根据镜像alpine/git启动容器repo，本地查找不到镜像，就去远程仓库查找镜像
    --name repo：为容器指定名称repo，不指定随机生成
    clone https://github.com/docker/：在启动的容器里面克隆仓库到git目录

    docker cp repo:/git/getting-started/ .
    将容器repo的/git/getting-started下的getting-started目录 拷贝到(命令最后有一个. 表示当前目录)当前目录

    cd getting-started
    docker build -t docker101tutorrial .
    使用当前目录的 Dockerfile 创建镜像，标签为 docker101tutorial

    docker run -d -p 80:80 --name docker-tutorial docker101tutorial
    使用镜像docker101tutorial，以后台模式启动一个容器并将容器命名为docker-tutorial，将容器的80端口映射到主机的80端口
*/
```

### dockerignore

> 使用它排除构建无关的文件及目录，如 node_modules

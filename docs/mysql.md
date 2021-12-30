# Mysql

> MySql 是 CS 架构既 client&server
>
> mysqld 服务端，只有一个
>
> mysql 客户端，可以有多个
>
> 还有其它 mysql\*系列工具
>
> 这些所有的 mysql\*组成了 mysql 数据库管理系统

## mysql@5.7

> 为了兼容旧项目，使用 homebrew 安装了低版本的 mysql

- `启动：`brew services (re)start mysql@5.7
- `停止：`brew services stop mysql@5.7
- `状态：`brew services

> if you don't want/need a background service you can just run:
>
> /usr/local/opt/mysql@5.7/bin/mysqld_safe --datadir=/usr/local/var/mysql

## mysql 常用命令

> mysqld 是数据库管理系统应用程序服务端；mysql 是数据库管理系统客户端

- `mysql -uroot -p：`mysql 客户端以 root 用户身份连接 mysql 服务端
- `show databases：`展示当前数据库实例下的所有数据库
- `use database_name：`选中要操作的数据库
- `show tables：`展示选中数据库下的所有表
- `desc table_name：`查看表结构
- `describe table_name：`查看表结构
- `show columns（fields） from table_name：`查看表结构

## 问题

### WARNINGS:wagtailcore.WorkflowState: (models.W036) MySQL does not support unique constraints with conditions.HINT: A constraint won't be created. Silence this warning if you don't care about it

# Mysql

## mysql@5.7

> 为了兼容旧项目，使用 homebrew 安装了低版本的 mysql

- `启动：`brew services (re)start mysql@5.7
- `停止：`brew services stop mysql@5.7
- `状态：`brew services

> if you don't want/need a background service you can just run:
>
> /usr/local/opt/mysql@5.7/bin/mysqld_safe --datadir=/usr/local/var/mysql

## 问题

### WARNINGS:wagtailcore.WorkflowState: (models.W036) MySQL does not support unique constraints with conditions.HINT: A constraint won't be created. Silence this warning if you don't care about it

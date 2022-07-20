# 常用命令

## 查看 django 版本

> python -m django version

## 创建 Django 工程

> django-admin startproject projectName

## 创建 wagtail 工程

> wagtail start projectName

## 创建虚拟环境

> python3 -m venv mysite\env

## 启动 python 服务

> pyhton manage.py runserver

## 创建 python app

> python manage.py startapp appName

## 生成 SQL

> python manage.py migrate

## 执行 SQL

> python manage.py makemigrations [appName]

## 查看 SQL 语句内容

> python manage.py sqlmigrate appName 0001

## 进入 shell

> python manage.py shell

## 创建管理员账号

> python manage.py createsuperuser

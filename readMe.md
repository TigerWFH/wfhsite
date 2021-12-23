# python

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

# 自动安装启动

> 两个脚本（也可以合成一个）
> 首次安装脚本
> 项目脚本

## 安装 pyenv

## 安装全局使用的 python

## 安装全局工具 supervisor

> 配置 supervisor

## 安装 openresty，提供静态资源服务

## 拉取源码 A

> 更新 supervisor 中 A 的配置

## 拉取源码 B

> 更新 supervisor 中 B 的配置

## 拉取源码 C

> 更新 supervisor 中 C 的配置

## 安装项目使用的 python

> pyenv install
> 会根据项目下的.python-version 安装项目所需要版本

## 创建虚拟环境

python -m venv ./.env

## 激活虚拟环境

source ./.env/bin/activate

## 安装依赖

pip install -r requirements.txt

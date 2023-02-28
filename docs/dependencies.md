# 依赖

## Django

> Web 框架

## wagtail

> 基于 Django 的 CMS 管理系统

## mysqlclient

> python 应用操作 mysql 数据库的驱动库

## requests

> 简单优雅的 http 协议实现库

## beautifulsoup4

> 可以从 HTML 或 XML 文件中提取数据的 Python 库

## django-modelcluster==3.1

> wagtail 的一员

## django-settings-export==1.1.0

> Django 的一员

## django-taggit==0.22.1

> 标签体系

## django-treebeard==4.0.1

> django-treebeard is a library that implements efficient tree implementations for the Django Web Framework 2.2 and later.

## djangorestframework==3.4.0

> Django REST framework

## html5lib==0.999999

> html5lib is a pure-python library for parsing HTML. It is designed to conform to the WHATWG HTML specification, as is implemented by all major web browsers.

## pytz==2016.6.1

> This library allows accurate and cross platform timezone calculations using Python 2.4 or higher. It also solves the issue of ambiguous times at the end of daylight saving time, which you can read more about in the Python Library Reference

## six==1.10.0

> It provides utility functions for smoothing over the differences between the Python versions with the goal of writing Python code that is compatible on both Python versions

## Unidecode==0.4.19

> It often happens that you have text data in Unicode, but you need to represent it in ASCII

## Willow==0.4

> 图像处理库，https://pillow.readthedocs.io/en/latest/

## django_qiniu_storage==2.3.0

## 其他

```js
/*
aiohttp==3.8.1
aiosignal==1.2.0
alibabacloud_cloudfw20171207==1.1.9
alibabacloud-credentials==0.2.0
alibabacloud-ecs20140526==2.1.0
alibabacloud-endpoint-util==0.0.3
alibabacloud-gateway-spi==0.0.1
alibabacloud-openapi-util==0.1.6
alibabacloud-ram20150501==1.0.2
alibabacloud-slb20140515==3.3.16
alibabacloud_sts20150401==1.1.2
alibabacloud-tea==0.2.8
alibabacloud-tea-openapi==0.3.3
alibabacloud-tea-util==0.3.5
alibabacloud-tea-xml==0.0.2
aliyun-log-python-sdk==0.7.11
aliyun-python-sdk-core==2.13.36
aliyun-python-sdk-kms==2.15.0
amqp==5.0.6
ansible==2.8.8
anyjson==0.3.3
asgiref==3.3.4
async-timeout==4.0.1
asynctest==0.13.0
attrs==21.2.0
backports.zoneinfo==0.2.1
bcrypt==3.2.0
billiard==3.6.4.0
cached-property==1.5.2
celery==5.1.2
certifi==2021.5.30
cffi==1.14.5
chardet==4.0.0
charset-normalizer==2.0.9
click==7.1.2
click-didyoumean==0.0.3
click-plugins==1.1.1
click-repl==0.2.0
crcmod==1.7
cryptography==3.4.7
dataclasses==0.6
dateparser==1.1.1
deepdiff==5.7.0
Django==3.2.4
django-celery-beat==2.2.1
django-celery-results==2.2.0
django-cors-headers==3.7.0
django-crontab==0.7.1
django-filter==2.4.0
#django-filters==0.2.1
django-timezone-field==4.2.1
djangorestframework==3.12.4
djangorestframework-jwt==1.11.0
djongo-celery-results==0.1.0
elastic-transport==8.1.2
elasticsearch==8.2.3
fortiosapi==1.0.5
frozenlist==1.2.0
gevent==21.1.2
greenlet==1.1.0
gunicorn==20.1.0
idna==2.10
idna-ssl==1.1.0
importlib-metadata==4.6.1
importlib-resources==5.4.0
Jinja2==3.0.1
jmespath==0.10.0
kombu==5.1.0
ldap3==2.9
MarkupSafe==2.0.1
multidict==5.2.0
mysqlclient==2.0.3
ordered-set==4.0.2
oss2==2.15.0
oyaml==1.0
paramiko==2.7.2
pika==1.2.0
Pillow==8.2.0
prompt-toolkit==3.0.19
protobuf==3.20.1
pyasn1==0.4.8
pycparser==2.20
pycryptodome==3.14.1
PyJWT==1.7.1
PyNaCl==1.4.0
python-crontab==2.5.1
python-dateutil==2.8.1
pytz==2021.1
pytz-deprecation-shim==0.1.0.post0
PyYAML==5.4.1
redis==3.5.3
regex==2022.3.2
requests==2.25.1
six==1.16.0
sqlparse==0.4.1
tencentcloud-sdk-python==3.0.457
typing-extensions==3.10.0.0
tzdata==2022.1
tzlocal==4.2
urllib3==1.26.5
vine==5.0.0
wcwidth==0.2.5
yarl==1.7.2
zipp==3.5.0
zope.event==4.5.0
zope.interface==5.4.0
kubernetes~=25.3.0


// asgi
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devops_wfh_api.settings')

application = get_asgi_application()

// wsgi
import os

from django.core.wsgi import get_wsgi_application
import platform

if platform.uname().system == 'Linux' and os.path.exists('devops_api/settings/prod.py'):
    os.environ['DJANGO_SETTINGS_MODULE'] = 'devops_api.settings.prod'
elif platform.uname().system == 'Linux' and os.path.exists('devops_api/settings/test.py'):
    os.environ['DJANGO_SETTINGS_MODULE'] = 'devops_api.settings.test'
else:
    os.environ['DJANGO_SETTINGS_MODULE'] = 'devops_api.settings.dev'

# os.environ.setdefault('DJANGO_LOG_LEVEL', 'DEBUG')
application = get_wsgi_application()

// 配置中定义路由表
# https://www.cnblogs.com/zhangxinqi/p/9094953.html
# https://docs.djangoproject.com/zh-hans/3.2/topics/db/multi-db/#topics-db-multi-db-routing 


gunicorn: gunicorn-绿色独角兽，是一个 Python 的 WSGI HTTP 服务器，对比uwsgi
supervisor
*/
```

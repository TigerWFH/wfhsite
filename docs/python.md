# Python

## 语法

### 类型判断

> type 和 isinstance
>
> Python 中的数据类型大致分为 6 类：
>
> Number(数字)，其中 boolean、int、float、complex 等都归为 Number
>
> String(字符串), Tuple(元组), List(列表), Dictionary(字典), Sets(集合)
>
> 不可变类型：Number、String、Tuple。不可变类型的变量在第一次赋值声明的时候，会在内存中开辟一块空间，用来存储这个变量被赋予的值，变量被声明后，变量的值就与开辟的内存空间绑定，我们不能修改存储在内存中的值，当我们想给此变量赋新值时，会开辟一块新的内存空间保存新的值。
>
> 可变类型：List、Dictionary、Sets。可变类型的变量在第一次赋值声明的时候，也会在内存中开辟一块空间，用来存储这个变量被赋予的值。我们能修改存储在内存中的值，当该变量的值发生了改变，它对应的内存地址不发生改变

### Built-in Types<https://docs.python.org/3/library/stdtypes.html#other-built-in-types>

[中文资料](https://docs.python.org/zh-cn/3/library/stdtypes.html#other-built-in-types)

- `Boolean Types：`True 和 False
  > 支持 and、or、not 操作
  >
  > 支持比较运算符操作 is、is not、>、...
- `Number Types：`int、float、complex
  > 支持算术运算
  >
  > 支持比较运算
  >
  > 支持位运算：|、^、&、<<、>>、~
- `Iterator Types`
- `Sequence Types：`list、tuple、str、range、bytes、bytearray、memoryview
- `Set Types：`set、frozenset
- `Mapping Types：`dict
- `Context Manager Types：`
- `Type Annotation Types：`Generic Alias、Union
- `Other Built-in Types：`Modules、Classes and Class Instances、Functions、Methonds、Code Objects、Type Objects、Null Object、Ellipsis Object、

### 序列（Sequence）

> 序列包括：列表（list）、元组（tuple）、字符串（string 和 unicode string

### 列表（list）：[]，列表是可修改的

### 元祖（tuple）：()，元组不可修改

### 字典（dict）：{}，无序

> 访问字典：dict['key']或者 dict.get('key')
>
> 访问对象属性用.

### 集合（set）

### 不可变集合（frozenset）

### 数字（Number）：int、long、float、complex

### 字符串（String）：''

```python
    n = 123
    s = '123_abc'
    # list
    list = [1,2,3, 'ac']
    # tuple
    t = ('a', 'a', 'v', 789)
    tinytuple = ('a', 'b')
    # dict
    d = {
        a: 'a'
    }
    # 类型转换函数
    # int(x[, base])、long(x[, base])、float(x)、complex(real[, image])
    # str(x)、repr(x)、eval(str)、tuple(s)、list(s)、set(s)、dict(d)
    # frozenset(s)、chr(x)、unichr(x)、ord(x)、hex(x)、oct(x)

```

### 枚举<https://juejin.cn/post/6844903901922066445>

```python
# 枚举具有自定义的元类，它会影响所派生枚举类及其实例（成员）的各个方面
from enum import Enum

# 枚举成员（即实例）EnumMeta 会在创建 Enum 类本身时将它们全部创建完成
# 类 Color 是一个 enumeration (或称 enum)
# 属性 Color.RED, Color.GREEN 等等是 枚举成员 (或称 enum 成员) 并且被用作常量
# 枚举成员具有 名称 和 值 (例如 Color.RED 的名称为 RED，Color.BLUE 的值为 3 等等)
# 枚举成员是可哈希的，因此它们可在字典和集合中可用


class Color(Enum):
    RED = 1,
    GREEN = 2,
    BLUE = 3

```

## lint and format

### flake8：Python 静态代码检查工具

> Python 官方发布的一款辅助检测 Python 代码是否规范的工具，相对于目前热度比较高的 Pylint 来说，Flake8 检查规则灵活，支持集成额外插件，扩展性强

### pylint：Python 静态代码检查工具

### yapf

> YAPF（Yet Another Python Formatter）是 Google 开源的一个用来格式化 Python 代码的工具，可以一键美化代码。支持 2 种代码规范：PEP8 和 google style

## pass 语句

> pass 是空语句，为了保持程序结构的完整性
>
> pass 不做任何事情，一般只做占位

## Python 类属性和对象属性

```python
class Person(object):
  # 这是类属性
  name = 'person'
  def __init__(self, name):
    # 对象属性
    self.name = name

# 对象属性的优先级高于类属性
```

## python 基础

> 用双下划线开头且结尾的变量，在 Python 中被称为内置变量

- `__name__`：python 内置变量，直接执行脚本值为"**main**"；简介执行则为脚本名称
- `__init__`：py3 返回的是文件所在位置的绝对路径；py2 返回的是相对路径
- `__dict__`
- `__file__:`

```python
# 查看内置变量：dir(__builtins__)
# __name__
# python a.py,__name__ = '__main__'; 否则__name__ = 'a';
# __file__是模块的特殊属性，标识文件的路径

```

### 系统内置模块

- `os：`操作系统提供的功能
- `sys：`提供了一系列有关 Python 运行环境的变量和函数
- `random：`random 模块用于生成随机数
- `time：`主要包含各种提供日期、时间功能的类和函数
- `datetime：`对 time 模块的一个高级封装
- `shutil：`是一种高层次的文件操作工具
- `logging：`将日志打印到了标准输出中
- `re：`可以直接调用来实现正则匹配
- `pymysql：`连接数据库,并实现简单的增删改查
- `thrading：`提供了更强大的多线程管理方案
- `queue：`实现了多生产者,多消费者的队列
- `json：`用于字符串和数据类型间进行转换 json

### 第三方模块

- `Requests：`最富盛名的 http 库
- `Scrapy`从事爬虫相关的工作
- `Numpy`为 Python 提供了很多高级的数学方法
- `matplotlib`一个绘制数据图的库。对于数据分析师非常有用
- `Scapy`用 Python 写的数据包探测和分析库
- `Django`开源 Web 开发框架，它鼓励快速开发,并遵循 MVC 设计，开发周期短

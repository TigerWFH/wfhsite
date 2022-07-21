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

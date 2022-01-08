# Python

## 语法

### 数字（Number）：int、long、float、complex

### 字符串（String）：''

### 列表（List）：[]

### 元祖（Tuple）：()

### 字典（Directory）：{}

```python
    n = 123
    s = '123_abc'
    list = [1,2,3, 'ac']
    t = ('a', 'a', 'v', 789)
    tinytuple = ('a', 'b')
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

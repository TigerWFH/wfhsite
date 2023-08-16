# Python

## 术语

- ` 模块（Module）：``是一个 python 文件，以.py 结尾 `，包含了 python 对象和 python 语句。模块能定义函数、类和变量，模块里也能包含可执行的代码。`一个模块只会被导入一次`，不管你执行了多少次 import。这样可以防止导入模块被一遍又一遍地执行。

- `包：`包是一个分层次的文件目录结构，它定义了一个由模块及子包，和子包下的子包等组成的 Python 的应用环境。包就是文件夹，但该文件夹下必须存在 \_\_init\_\_.py 文件, 该文件的内容可以为空。\_\_init\_\_py 用于标识当前文件夹是一个包。
  > \_\_init\_\_.py 一般用于标识包，主要是为了避免将文件夹名当作普通的字符串。\_\_init\_\_.py 的内容可以为空，一般用来进行包的某些初始化工作或者设置\_\_all\_\_值，\_\_all\_\_是在 from package-name import \*这语句使用的，全部导出定义过的模块

## python 版本管理工具

- `pyenv`

## python 包库

- `pypi`官方指定的软件包仓库[pypi](https://pypi.org)

  > - 国内镜像：http://mirrors.aliyun.com/pypi/simple/
  > - 科学计算镜像：https://repo.anaconda.com/

- `将包记录到描述文件：`pip freeze > requirements.txt

## python 包管理工具

> 包管理工具不仅仅提供了基本的包管理功能，还提供了虚拟环境构建，程序管理的功能

- `pip：`python 内置管理工具，使用 pypi 软件包
- `conda：`作为科学计算领域的包管理工具，conda 功能丰富，功能强大，所用软件包源为 Anacondarepository 和 AnacondaCloud，conda 不仅支持 Python 软件包，还可安装 C,C++,R 和其它语言的二定制软件包。除软件包管理外，还可提供相互隔离的软件环境
- `pipenv：`是 KennethReitz 于 2017 年 1 月发布的 Python 依赖管理工具，现在由 PyPA 维护。Pipenv 自动管理虚拟环境和依赖文件，提供一系列命令和选项，实现各种依赖和环境管理相关操作
- `poetry：`与 Pipenv 相似，是 Python 虚拟环境和依赖管理工具，此外还提供包管理功能，如包装和发布。您可以将其视为 Pipenv 和 Flit 工具的超集。使用 Poetry 可以同时管理 Python 库和 Python 程序
- `pdm：`是一个新的 Python 的包管理器，在 2021 年发布 1.0 版本，目前最高的版本是 1.12.8。

## python 虚拟环境管理工具

> Python 拥有大量的第三方库，引用这些库也非常方便，通过 pip install 就可以将这些第三方库安装到本地 Python 库文件目录中，然后就可以 import 到项目中，极大地提升了开发者的编码效率。但这也带来了一个问题：当 A 项目和 B 项目同时引用 Lib 库，而 A 项目需要 Lib 版本是 1.0，B 项目需要 Lib 的版本是 2.0。这样在使用 pip install 命令将 Lib 直接安装到本地全局环境中就会发生冲突，有可能会导致 A 和 B 的运行环境无法同时得到满足而运行失败。

> 虚拟环境是一个包含了特定 Python 解析器以及一些软件包的自包含目录，不同的应用程序可以使用不同的虚拟环境，从而解决了依赖冲突问题，而且虚拟环境中只需要安装应用相关的包或者模块，可以给部署提供便利

> Python 虚拟环境就是利用这个特性构建的，在激活虚拟环境之时，激活脚本会将当前命令行程序的 PATH 修改为虚拟环境的，这样执行命令就会在被修改的 PATH 中查找，从而避免了原本 PATH 可以找到的命令，从而实现了 Python 环境的隔离。

## Data model<https://docs.python.org/3/reference/datamodel.html>

> Every object has an `identity`, a `type` and a `value`.
>
> An object’s identity `never changes` once it has been created;
>
> An object’s type `determines` the operations that the object supports (e.g., “does it have a length?”) and also defines the possible values for objects of that type.
>
> The value of some objects can change. Objects whose value can change are said to be `mutable`; objects whose value is unchangeable once they are created are called `immutable`.

### Number

> Numeric objects are immutable; once created their value never changes.
>
> Python distinguishes between integers, floating point numbers, and complex numbers:
>
> - numbers.Integral
>   - `int()`,<\class 'int'>
>   - `bool()`,<\class 'bool'>
> - numbers.Real:`float()`,<\class 'float'>
> - numbers.Complex:`complex()`,<\class 'complex'>

### Sequences

> - `Immutable sequences`
>   - Strings:`str()`,<\class 'str'>
>   - Tuples: `tuple()`,<\class 'tuple'>
>   - Bytes: `bytes()`,<\class 'bytes'>
> - `Mutable sequences`
>   - Lists: `list()`,<\class 'list'>
>   - Byte Arrays: `bytearrays()`,<\class 'bytearrays'>

### Set types

> - Sets:`set()`,<\class 'set'>
> - Frozen Sets: `frozenset()`,<\class 'frozenset'>

### Mappings

> - Dictionaries: `dict()`,<\class 'dict'>

### Callable types

### Modules

### Custom classes

### Class instances

### Internal types

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

## python 基础

> 用双下划线开头且结尾的变量，在 Python 中被称为内置变量
>
> python 中实例化类`不需要使用关键字 new`（也没有这个关键字），类的实例化类似函数调用方式

- `__name__`：python 内置变量，默认是当前模块名（）文件名；如果当前文件被当做脚本直接执行，值为\_\_main\_\_
- `__init__`：py3 返回的是文件所在位置的绝对路径；py2 返回的是相对路径
- `__dict__`
- `__file__:`**file**表示当前文件的绝路径
- `__str__()`：方法将实例转换为一个字符串，使用 str() 或 print() 函数会输出这个字符串
- `__repr__()`：方法返回一个实例的代码表示形式，通常用来重新构造这个实例。 内置的 repr() 函数返回这个字符串
- `__format__()`：方法给 Python 的字符串格式化功能提供了一个钩子。 这里需要着重强调的是格式化代码的解析工作完全由类自己决定

```python
# 查看内置变量：dir(__builtins__)
# __name__
# python a.py,__name__ = '__main__'; 否则__name__ = 'a';
# __file__是模块的特殊属性，标识文件的路径

```

### Python 类属性和对象属性

> 静态属性，可以通过 self 或 class 访问；但是只能通过 class 修改
>
> 在类体中，根据变量定义的位置不同，以及定义的方式不同，类属性又可细分为以下 3 种类型
>
> - 类体中、所有函数之外：此范围定义的变量，称为`类属性或类变量`
> - 类体中，所有函数内部：以“self.变量名”的方式定义的变量，称为`实例属性或实例变量`
> - 类体中，所有函数内部：以“变量名=变量值”的方式定义的变量，称为`局部变量`

```python
class Person(object):
  # 这是类属性
  name = 'person'
  def __init__(self, name):
    # 对象属性
    self.name = name

# 对象属性的优先级高于类属性
```

### 静态方法、实例方法、类方法

> 在实际编程中，几乎不会用到类方法和静态方法，因为我们完全可以使用函数代替它们实现想要的功能，但在一些特殊的场景中（例如工厂模式中），使用类方法和静态方法也是很不错的选择。

- `静态方法：`使用装饰器@staticmethod 装饰的方法称为静态方法，但是此类方法没有 self 参数，且参数的个数是任意的。静态方法的调用，既可以使用`类对象`，也可以使用`类对象实例`
- `实例方法：`需要`类对象实例`之后才能调用的方法，该方法的第一个参数必须是 self
- `类方法：`使用装饰器@classmethod（@classonlymethod）装饰的方法称为类方法，但是此类方法第一个参数为 cls，用于标示该类方法所属的类
  > @classonlymethod：只允许使用`类对象.方法()` 的形式进行调用，不允许使用`类对象实例`的方式进行调用。

### import 和 from import

```js
/*
  import xxx：导入的是整个模块
  from xxx import yyy：导入的是模块中的一部分
  from xxx.yyy import zzz
  from xxx import *
 */
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

## python gil

[GIL](https://cloud.tencent.com/developer/news/743497)

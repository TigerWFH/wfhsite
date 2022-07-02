# Django<https://www.jianshu.com/p/3fc79a1e0edb>

## 查看 migration 文件生成的 sql

> python manage.py sqlmigrate user 0020
>
> python manage.py sqlmigrate appName 迁移文件序号

## Django 数据对应关系

> 关系型数据库存在一对多、一对一、多对多的关系
>
> 一对一：models.OneToOneField('class_name', on_delete=models.CASCADE)
>
> 一对多：models.ForeignKey('class_name', on_delete=models.CASCADE)
>
> 多对多：models.ManyToManyField('class_name')

- `ForeignKey(otherModel, on_delete, **options)`
  > otherModel：关联的表格（主表），默认外键存储的是主表的主键，但可以通过 to_field 修改
  >
  > on_delete：
  > CASCADE，当主表的字段被删除时，和它有关的子表字段也会被删除
  > PROJECT，阻止删除并抛出一个 ProjectedError
  > RESTRICT，类似 PROJECT
  > SET_NULL，将 ForeignKey 设置为 null，如果允许设置 null 值
  > SET_DEFAULT，
  > SET()，
  > DO_NOTHING，
  >
  > db_column：可以指定字段名
  >
  > options：to_field，改变关联的字段

```python
# 实体：Class(班级)、Teacher(老师)、Student(学生)、StudentDetail(学生信息)
# Class和Teacher是 多对多 关系
# Class和Student是 一对多 关系
# Student和StudentDetail是 一对一 关系
class Student(models.Model):
  id = models.AutoField(primary_key=True)
  sname = models.CharField(max_length=20)

  # 一对多外键
  cid = models.ForeignKey('Class', on_delete=models.CASCADE)
  # 一对一外键
  cid = models.OneToOneField('StudentDetail', on_delete=models.CASCADE)

class StudentDetail(models.Model):
  id = models.AutoField(primary_key=True)
  height = models.IntegerField()
  #...

class Class(models.Model):
  id = models.AutoField(primary_key=True)
  cname = models.CharField(max_length=20)

class Teacher(models.Model):
  id = models.AutoField(primary_key=True)
  cname = models.CharField(max_length=20)

  # 多对多
  cid = models.ManyToManyField('Class')

```

## Widgets

> A widget is Django’s representation of an HTML input element. The widget handles the rendering of the HTML, and the extraction of data from a GET/POST dictionary that corresponds to the widget.
>
> Whenever you specify a field on a form, Django will use a default widget that is appropriate to the type of data that is to be displayed.
>
> built-in Field classes<https://docs.djangoproject.com/en/4.0/ref/forms/fields/#built-in-fields>
>
> if you want to use a different widget for a field, you can use the widget argument on the field definition. For example:

```python
from django import forms

class CommentForm(forms.Form):
  name = forms.CharField()
  url = forms.URLField()
  comment = forms.CharField(widget=forms.Textarea)
```

## Model Field<https://docs.djangoproject.com/en/4.0/ref/models/fields/>

> Field is an abstract class that represents a database table column.Django uses fields to create the database table (db_type()), to map Python types to database (get_prep_value()) and vice-versa (from_db_value())
>
> Field including the field options and field types Django offers

### Django 模型之内置类 class Meta<https://docs.djangoproject.com/en/4.0/ref/models/options/>

> 使用内部类提供一些 metadata

- `abstract`定义外部类是否是抽象类
- `db_table`指定对应 Model 生成的表名。默认是 appname_modelname，例如 demos 中的 Student 对应的表名：demos_student
- `ordering`排序，是一个列表
- `unique_together`在数据进行写表操作的时候，我们往往会遇到两个字段组合起来需要唯一的情况
- `verbose_name`A human-readable name for the object singular（单数）
- `verbose_name_plural`The plural(复数形式可读性名字) name for the object

## django field options

> 以下 options 适应所有 Field，都是可选项

- `Field.null：`如果为 True，数据库字段将空值存储为 NULL，默认是 false。
- `Field.blank：`如果为 True，数据库字段允许为空，默认是 false
- `Field.choices：`A sequence consisting itself of iterables of exactly two items (e.g. [(A, B), (A, B) ...]) to use as choices for this field
- `Field.db_column：`The name of the database column to use for this field. If this isn’t given, Django will use the field’s name.
- `Field.db_index：`If True, a database index will be created for this field
- `Field.db_tablespace：`The name of the database tablespace to use for this field’s index, if this field is indexed
- `Field.default：`默认值
- `Field.editable：`If False, the field will not be displayed in the admin or any other ModelForm
- `Field.error_message：`
- `Field.help_text：`Extra “help” text to be displayed with the form widget
- `Field.primary_key：`
- `Field.unique：`If True, this field must be unique throughout the table
- `Field.unique_for_date：`
- `Field.unique_for_month：`
- `Field.unique_for_year：`
- `Field.verbose_name：`
- `Field.validators`

## django field types

> Django ModelField To FormField, ModelField 映射数据库；FormField 映射 HTML 表单组件
> ![ModelFieldToFormField](./Django_modelField_to_formField.png)

- `class AutoField(**options)：`An IntegerField that automatically increments according to available IDs
- `class BigAutoField(**options)：`
- `class BigIntegerField(**options)：`
- `class BinaryField(max_length=None, **options)：`
- `class BooleanField(**options)：`Default widget: CheckboxInput
- `class CharField(max_length=None, **options)：`Default widget: TextInput
- `class DateField(auto_now=False, auto_now_add=False, **options)：`Default widget: DateInput
- `class DateTimeField(auto_now=False, auto_now_add=False, **options)：`Default widget: DateTimeInput
- `class DecimalField(max_digits=None, decimal_places=None, **options)：`Default widget: NumberInput when Field.localize is False, else TextInput
- `class DurationField(**options)：`Default widget: TextInput
- `class EmailField(max_length=254, **options)：`Default widget: EmailInput
- `class FileField(upload_to=None, max_length=100, **options)：`Default widget: ClearableFileInput
- `class FilePathField(path='', match=None, recursive=False, allow_files=True, allow_folders=False, max_length=100, **options)：`Default widget: Select
- `class FloatField(**options)：`Default widget: NumberInput when Field.localize is False, else TextInput
- `class ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, **options)：`Default widget: ClearableFileInput
- `class IntegerField(**options)：`Default widget: NumberInput when Field.localize is False, else TextInput
- `class JSONField(encoder=None, decoder=None, **options)：`Default widget: Textarea
- `class PositiveBigIntegerField(**options)：`
- `class PositiveIntegerField(**options)：`
- `class PositiveSmallIntegerField(**options)：`
- `class SlugField(max_length=50, **options)：`Default widget: TextInput
- `class SmallAutoField(**options)：`
- `class SmallIntegerField(**options)：`
- `class TextField(**options)：`
- `class TimeField(auto_now=False, auto_now_add=False, **options)：`Default widget: TimeInput
- `class URLField(max_length=200, **options)：`
- `class UUIDField(**options)：`Default widget: TextInput
- `class ForeignKey(to, on_delete, **options)：`
- `class ManyToManyField(to, **options)：`
- `class OneToOneField(to, on_delete, parent_link=False, **options)：`

## django.contrib.staticfiles

> Websites 一般需要提供 images、javascript、css 等文件，在 Django 中这些文件被称为 static fiels
>
> django.contrib.staticfiles 提供了 static 模板标签
>
> 可以直接在对应的 app 下建立 static 目录，书写对应应用的静态文件

- `config static fiels`

  - `INSTALLED_APPS增加django.contrib.staticfiles`
  - `在settings中定义STATIC_URL：`STATIC_URL = 'static/'
  - `在template中使用static tag构建static files的真实路径`

  ```plain
    {% load static %}
    <img src="{% static 'my_app/example.png' %}" alt="MyImage" />

  ```

  - `将静态文件存储到static目录：my_app/static/example.png`
  - `可以定义一组静态路径`

  ```plain
    STATICFILES_DIRS = [
      BASE_DIR / "static",
      'var/www/static'
    ]
  ```

## template

> filter 一般接受 1-2 个参数；tags 可以接受多个参数
>
> filter 一般返回一个 template variable
>
> tags（simple_tag）可以返回 template varible，
> tags（inclusion_tag）可以返回 template

### filter 本质就是 python 函数

> filter 就是只能接收 1 或 2 个参数的 python 函数。它只适用于修改数据的呈现方式
>
> 因为模板语言不提供异常处理机制，所以任何从模板过滤器中抛出的异常都将被视为服务器异常

### tag

>

### django template tags and filters<https://docs.djangoproject.com/en/3.1/ref/templates/builtins/>

> When a Django app is added to INSTALLED_APPS, any tags it defines in the conventional location described below are automatically made available to load within templates
>
> 默认路径是：Your custom tags and filters will live in a module inside the templatetags directory. The name of the module file is the name you’ll use to load the tags later
>
> 自定义 tag 和 filter 会定义在 templatetags 模块中，对应的模块名就是要用到的标签。例如

```plain
polls/
  __init__.py
  models.py
  templatetags/
    __init__.py
    poll_extras.py // 过滤器
  views.py

  <!-- 加载 -->
  {% load poll_extras.py %}
  <!-- polls app必须添加到INSTALLED_APPS -->
```

#### build-in tag

> tag 的用法，tag 可以接收参数

```template
    {% tagName %}
        {{ 内容 }}
    {% endtagname %}
    {% autoescape on %}
        {{ body }}
    {% endautoescape %}
```

- `extends：`
- `block：`定义可以被 overridden 的 block
- `comment：`
- `for：`
- `for ... empty：`
- `if：`
- `filter：`
- `autoescape：`
- `csrf_token：`
- `cycle：`
- `debug：`
- `firstof：`
- `Boolean operators：`
  - `and`
  - `or`
  - `and not`
  - `==`
  - `!=`
  - `<`
  - `<=`
  - `>`
  - `>=`
  - `in`
  - `not in`
  - `is not`
- `Filters：`
  - `|`
- `Complex expressions：`
  - `or`
- `ifchanged：`
- `include：`
- `load：`
- `lorem：`
- `now：`
- `regroup：`
- `resetcycle：`
- `spaceless：`
- `templatetag：`
- `url：`
- `verbatim：`
- `widthratio：`
- `with：`

### built-in filter

> filter 用法

```template
    {{ value|add:"2"}}
```

- `add：`
- `addslashes：`
- `capfirst：`
- `center：`
- `cut：`
- `date：`
- `default：`
- `default_if_none：`
- `dictsort：`
- `dictsortreversed：`
- `divisibleby：`
- `escape：`
- `escapejs：`
- `filesizeformat：`
- `first：`
- `floatformat：`
- `force_escape：`
- `get_digit：`
- `iriencode：`
- `join：`
- `join_script：`
- `last：`
- `length：`
- `length_is：`
- `linebreaks：`
- `linebreaksbr：`
- `linenumbers：`
- `ljust：`
- `lower：`
- `make_list：`
- `phone2numeric：`
- `pluralize：`
- `pprint：`
- `random：`
- `rjust：`
- `safe：`
- `safeeq：`
- `slice：`
- `slugify：`
- `stringformat：`
- `striptags：`
- `time：`
- `timesince：`
- `timeuntil：`
- `title：`
- `truncatechars：`

### 三方库 tags 和 filters

#### django.contrib.humanize

- `static：`To link to static files that are saved in STATIC_ROOT Django ships with a static template tag. If the django.contrib.staticfiles app is installed, the tag will serve files using url() method of the storage specified by STATICFILES_STORAGE
- `get_static_prefix`
- `get_media_prefix`

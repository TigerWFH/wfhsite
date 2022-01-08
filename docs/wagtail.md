# wagtail

## 创建应用

> wagtail start appName [path]

## snippet<https://docs.wagtail.io/en/stable/topics/snippets.html>

> snippet 的菜单名成默认是 Snippets（一级入口就只能是 Snippets），不能修改
>
> Snippets 页面会展示不同的 Snippet（二级入口，可以自定义名字）

- `snippets包：`snippets 是一些 Django Models，非 Wagtail Page

```python
from wagtail.snippets.models import register_snippet
```

- `通过Templates Tags使用定义的Snippets`
  > 更多参考 Django custom template tags 文档<https://docs.djangoproject.com/en/4.0/howto/custom-template-tags/>

```python

```

## ModelAdminGroup<https://docs.wagtail.io/en/v2.15.1/reference/contrib/modeladmin/menu_item.html?highlight=ModelAdminGroup#id2>

> These stub classes allow us to put various models into the custom "Wagtail Bakery" menu item rather than under the default Snippets section
>
> 通过管理菜单，可以把 Snippet 做成一级入口

## 资料

[wagtail 图标](https://thegrouchy.dev/general/2015/12/06/wagtail-streamfield-icons.html)
[更多图标](https://fontawesome.com/v5.15/icons)

## MySql

## ER 图转换关系

- `1:1`
  > 1:1 关系时，可以把任意建个实体的主键作为其中一个实体的外键，加入关系模式
- `1:n`
  > 1:n 关系时，把 1 方的主键加入到 n 中
- `n:m`
  > 需要新抽出一个关系，并将 n 和 m 的主键存储在新关系中

## primary key（主键）

## foreign key（外键）

> 外键是用来解决 1 对多的问题，用于关联查询

```python
    # ForeignKey(othermodel, on_delete, **options)
    # othermodel：关联的表（主表），在默认情况下，外键存储的是主表的主键（primary key）
    # on_delete='CASCADE'当主表的字段被删除时，和他有关的子表子弹也会被删除
    #           'PROTECT'：阻止删除，返回错误提示; 'SET_NULL'：用null代替;
    #           'SET_DEFAULT'：用默认值代替; 'SET()'：自定义
```

## parentalkey

> ParentalManyToManyField(Django--ManyToManyField)：add categories to the BlogPage model, as a many-to-many field
>
> ParentalKey：one-to-many relations

## InlinePanel<https://docs.wagtail.io/en/v2.15.1/reference/pages/panels.html#inline-panels>

## ModelAdmin<https://docs.wagtail.io/en/v2.15.1/reference/contrib/modeladmin/menu_item.html?highlight=ModelAdminGroup#id2>

- `安装应用`

```python
INSTALLED_APPS = [
  'wagtail.contrib.modeladmin'
]
```

- `使用`

## Panel Types

> Django’s field types are automatically recognised and provided with an appropriate widget for input

### Django widgets<https://docs.djangoproject.com/en/4.0/ref/forms/widgets/#built-in-widgets>

> from django import forms
>
> forms.TextInput

- `Built-in widgets：`
  - `TextInput`
  - `NumberInput`
  - `EmailInput`
  - `URLInput`
  - `PasswordInput`
  - `HiddenInput`
  - `DateInput`
  - `DateTimeInput`
  - `TimeInput`
  - `Textarea`
  - `CheckboxInput`
  - `Select`
  - `NullBooleanSelect`
  - `SelectMultiple`
  - `RadioSelect`
  - `CheckboxSelectMultiple`
  - `FileInput`
  - `ClearableFileInput`
  - `MultipleHiddenInput`
  - `SplitDateTimeWidget`
  - `SplitHiddenDateTimeWidget`
  - `SelectDateWidget`

### wagtail.admin.edit_handlers

- `FieldPanel(field_name,classname=None,widget=None,heading='',disable_comments=False)`
  > This is the panel used for basic Django field types
- `StreamFieldPanel(field_name, classname=None, widget=None)`
  > This is the panel used for Wagtail’s StreamField type
- `MultiFieldPanel(children, heading="", classname=None)`
  > This panel condenses several FieldPanel s or choosers, from a list or tuple, under a single heading string
- `InlinePanel(relation_name, panels=None, classname='', heading='', label='', help_text='', min_num=None, max_num=None)`
  > This panel allows for the creation of a “cluster” of related objects over a join to a separate model, such as a list of related links or slides to an image carousel.
- `FieldRowPanel(children, classname=None)`
- `HelpPanel(content='', template='wagtailadmin/edit_handlers/help_panel.html', heading='', classname='')`
- `PageChooserPanel(field_name, page_type=None, can_choose_root=False)`

### wagtail.images.edit_handlers

- `ImageChooserPanel(field_name)`

### wagtail.contrib.forms.edit_handlers

- `FormSubmissionsPanel`

### wagtail.documents.edit_handlers

- `DocumentChooserPanel(field_name)`

### wagtail.snippets.edit_handlers

- `SnippetChooserPanel(field_name, snippet_type=None)`

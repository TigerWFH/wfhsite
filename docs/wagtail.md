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

##

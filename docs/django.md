# Django<https://www.jianshu.com/p/3fc79a1e0edb>

## template

### filter 本质就是 python 函数

> filter 就是只能接收 1 或 2 个参数的 python 函数。它只适用于修改数据的呈现方式

### tag

### django template tags and filters<https://docs.djangoproject.com/en/3.1/ref/templates/builtins/>

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

# Mysql

> MySql 是 CS 架构既 client&server
>
> mysqld 服务端，只有一个
>
> mysql 客户端，可以有多个
>
> 还有其它 mysql\*系列工具
>
> 这些所有的 mysql\*组成了 mysql 数据库管理系统

## 术语

- `主键：`
- `外键：`
- `主表：`若同一个数据库中，B 表的外键与 A 表的主键相对应，则 A 表为主表，B 表为从表
- `从表：`若同一个数据库中，B 表的外键与 A 表的主键相对应，则 A 表为主表，B 表为从表
  > 实体完整性是通过主键约束实现的，而参照完整性是通过外键约束实现的，两者都是为了保证数据的完整性和一致性
  >
  > 主键约束比较好理解，就是主键值不能为空且不重复
  >
  > 外键约束是相关联的两个表之间的数据操作约束，包括删除，插入，更新等。理论上，在对关联数据表进行数据操作时，只改其一，不改其二，不符合关系数据库的参照完整性。
  >
  > 主从表是一种数据关系模型，主表约束从表。一般我们会在从表中做一个外键字段，引用主表中的主键。
  >
  > 为了保持数据的一致性，主从表要尽量遵循一下规则：
  - `当主表中没有对应的记录时，不能将记录添加到从表：`成绩表中不能出现在学员信息表中不存在的学号
  - `不能更改主表中的值而导致从表中的记录孤立：`把学员信息表中的学号改变了，学员成绩表中的学号也应当随之改变
  - `从表存在与主表对应的记录，不能从主表中删除该行：`不能把有成绩的学员删除了
  - `删除主表前，先删从表：`先删学员成绩表、后删除学员信息表

## mysql@5.7

> 为了兼容旧项目，使用 homebrew 安装了低版本的 mysql

- `启动：`brew services (re)start mysql@5.7
- `停止：`brew services stop mysql@5.7
- `状态：`brew services

> if you don't want/need a background service you can just run:
>
> /usr/local/opt/mysql@5.7/bin/mysqld_safe --datadir=/usr/local/var/mysql

- `修改账号密码：`mysql_secure_installation
- `导出配置：`

```plain
A CA file has been bootstrapped using certificates from the system
keychain. To add additional certificates, place .pem files in
  /opt/homebrew/etc/openssl@3/certs
and run
  /opt/homebrew/opt/openssl@3/bin/c_rehash
openssl@3 is keg-only, which means it was not symlinked into /opt/homebrew,
because macOS provides LibreSSL.
If you need to have openssl@3 first in your PATH, run:
  echo 'export PATH="/opt/homebrew/opt/openssl@3/bin:$PATH"' >> ~/.zshrc
For compilers to find openssl@3 you may need to set:
  export LDFLAGS="-L/opt/homebrew/opt/openssl@3/lib"
  export CPPFLAGS="-I/opt/homebrew/opt/openssl@3/include"
For pkg-config to find openssl@3 you may need to set:
  export PKG_CONFIG_PATH="/opt/homebrew/opt/openssl@3/lib/pkgconfig"
```

## mysql 常用命令

> mysqld 是数据库管理系统应用程序服务端；mysql 是数据库管理系统客户端

- `mysql -uroot -p：`mysql 客户端以 root 用户身份连接 mysql 服务端
- `show databases：`展示当前数据库实例下的所有数据库
- `use database_name：`选中要操作的数据库
- `show tables：`展示选中数据库下的所有表
- `desc table_name：`查看表结构
- `describe table_name：`查看表结构
- `show columns（fields） from table_name：`查看表结构

## 问题

### WARNINGS:wagtailcore.WorkflowState: (models.W036) MySQL does not support unique constraints with conditions.HINT: A constraint won't be created. Silence this warning if you don't care about it

## 外键

> 如果表 A 的主键存在于表 B 的 FA 字段中，则 FA 称为 A 表的外键

## 数据库实践

> 现在开发不使用外键，直接在代码或者使用框架进行约束，用外键会带来迁移问题
>
> 逻辑外键：
> 那什么是逻辑外键呢？
> 我们在定义两张表（user/userInfon）的关系时，学校教我们的是用 foreign key 去创建，这种是物理外键。
> 而逻辑外键就是两者必然的关联但是没有 foreign key 来关联，而是在设计两张表的时候创建字段去存储相关联的数据内容。
> 如，user（用户表）中存在 user_id(用户 id)字段，userInfon（用户信息表）中也存在 user_id(用户 id)字段，
> 这样就可以通过
> 'select \* from user inner join userInfon on user.user_id = userInfon.user_id，
> 这样的 sql 语句来实现逻辑查询

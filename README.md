1. 此项目需由 python3 manage.py runserver 才能启动Django1.1, 如果
   是由python manage.py runserver 启动的话,则会使用系统默认的Django版本(改进之后可以由Django2.2启动),
   可能会报错!!!(也可以使用./manage.py runserver 启动,但需在manage.py所在的目录下)
2. Django中绝对导入和相对导入---> 可以直接写成 from appname.xx import yy, 不用在意
   其中的红线报错提醒!   
3. xadmin的使用方法需要自行查阅相关文档
4. 关于'Uncaught Error: Option 'ajax' is not allowed for Select2 when attached to a <select> element.'
   相关(也就是在xadmin中autocomplete自动补充下拉框不生效)问题的说明:
        这个问题是由于在adminforms.py中的class Meta类中的fields引起的,在其中定义了多个
        具有下拉select选项的字段, 其中的status和category, tag字段有冲突,暂时的解决办法是
        去掉status字段,但不是最好的解决方案(
        (1). 初步判断status和这两个字段不能共存,暂时先删除它
        (2). 在models里面再设立一个Status类,将status独自设置成一个外键,貌似可行,可惜数据库读不进去,显示表主键无法识别
            class Status(models.Model):
                STATUS_NORMAL = 1
                STATUS_DELETE = 0
                STATUS_DRAFT = 2
                STATUS_ITEM = (
                    (STATUS_NORMAL, '正常'),
                    (STATUS_DELETE, '删除'),
                    (STATUS_DRAFT, '草稿'),
                )
                    )
            class Post(models.Model):
                # 省略其他代码
                status = models.ForeignKey(Status, default=Status.STATUS_NORMAL, choices=Status.STATUS_ITEM,
                               verbose_name='状态', on_delete=models.DO_NOTHING)           
                               
5. django 中pymsql版本问题解决方案:                      
    到\Program Files\Python36\Lib\site-packages\Django-2.0.6-py3.6.egg\django\db\backends\mysql
        文件下的base.py文件中，将以下内容注释掉
    # version = Database.version_info
    # if version < (1, 3, 3): 
    # raise ImproperlyConfigured("mysqlclient 1.3.3 or newer is required; you have %s" % Database.__version__)
6. 将db.sqlite3更换为MySQL问题: 
    (1). __init__.py文件必须在总目录下
    (2). 生成迁移文件: python3 manage.py makemigrations 要指定对应的APP 不然数据库不会生成相应的表
         即 python3 manage.py makemigrations blog; python3 manage.py migrate blog;
7. djangorestframework 在进行URL反向解析时不支持namespace命名空间,需要删除该属性;
8. post模型中tag字段是多对多类型,不是外键类型!!!
9. xadmin2.0适配Django2.0时, 后台界面出现 报错信息 找不到错误所在  暂时无解(可能是由于select2模块不兼容的原因select2.full.js文件 和 select2.js)
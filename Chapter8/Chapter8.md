# <font><center>Chapter 8 : 函数</center></font>
## 8.1 函数
```python
def greet_user(username):              
""" 显示简单的问候语 """
print(f"Hello, {username.title()}!")
greet_user('jesse')
```
其中  
username ： 形参  
""" 显示简单的问候语 """ ： 文档字符串，描述函数的作用  
'jesse' ： 实参

## 8.2 传递多个实参
**位置实参** ： 按括号中的顺序将实参赋予形参  
**关键字实参** ： 形参 = 实参，此时不需要注意顺序  
**默认值** ： 在定义函数时，可以给形参指定默认值。由于位置仍起作用，故需将有默认值的实参放最后。  
==关键字实参和默认值中等号两边不要空格==

## 8.3 返回值
使用 return 将值返回到调用函数的代码

## 8.4 传递列表
==在函数中对列表的修改会影响到全局==  
若不希望影响全局，可在调用时复制列表  
```python
function_name(list_name[:])
```

## 8.5 传递任意数量的形参
### 8.5.1 任意数量的形参
```python
def make_pizza(*toppings):
    """ 打印所有配料 """
    print(toppings)
make_pizza('mushrooms', 'green peppers', 'extra cheese')
```
```> > >  ('mushrooms', 'green peppers', 'extra cheese')```  
形参中的 * 会给 toppings 创建一个元组，以接受任意数量的实参  
==需将该形参置于最后==  
### 8.5.2 任意数量的关键字形参
```python
def build_profile(first, last, **user_info):
    """ 创建一个用户字典"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('albert', 'einstein'，location='princeton', field='physics')
print(user_profile)
```
```> > > {'location': 'princeton', 'field': 'physics','first_name': 'albert', 'last_name': 'einstein'}```  
形参中的 ** 会给 user_info 创建一个字典

## 8.6 模块
先创建一个 .py 文件（模块)，其中只包含函数。如:  
```python
module_name.py

def function_name():
    ...
```
再在同目录下的程序中调用该模块
```python
import module_name
module_name.function_name()
```
或
```python
from module_name import function_name(, function_name2, function_name3)
function_name()  # 此时无需使用 module_name.
```
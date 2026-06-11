# <font><center>Chapter 4 : 操作列表</center></font>
## 4.1 遍历整个列表
```python
for variable in list:
    print(variable)
```

## 4.2 避免缩进错误
忘记缩进 -- 报错  
忘记缩进非首行代码 -- 不报错  
不必要的缩进 -- 报错  
循环后不必要的缩进 -- 不报错  
遗漏冒号 -- 报错  

## 4.3 创建数值列表
### 4.3.1 range()函数
```python
range( x , y , z )
```
x : 起始值（默认为0）  
y : 结束值，不含，不可省略  
z : 步长（默认为0）  
### 4.3.2 range()函数与列表
```python
numbers = list(range(1, 6))
```
利用 range() 可快速创建列表  
### 4.3.3 列表推导式
```python
squares = [value**2 for value in range(1, 11)]
```
### 4.3.4 数值列表的统计计算
许多函数也可作用于列表,如：
```python
min(list)
max(list)
sum(list)
```

## 4.4 切片
```python
list[ x : y : z ]
```
x ：起始值，默认为0  
y ：结束值，默认到末尾  
z ：步长，默认为1  

**复制列表**
```python
list1 = list2[:]
```

## 4.5 元组
元组与列表类似，列表的函数可以用在元组上，但元组中元素不可变
```python
# 元组示例
dimensions = (200, 50)
```
> 有时会创建只含一个元素的元组，必须含逗号
> ```python
> tuple = (3,)
>```
# <font><center>Chapter 6 : 字典</center></font>
## 6.1 使用字典
```python
alien_0 = {'color': 'green', 'points': 5}
alien_0['color']                          # 获得建对应的值
alien_0['y_position'] = 25                # 添加键值对
alien_0['color'] = 'yellow'               # 修改值
del alien_0['points']                     # 删除键值对
```
若指定的键不存在，则上述取值方式会报错，
可使用get()方法
```python
point_value = alien_0.get('points', 'No point value assigned.')
# 第一个是指定的键，第二个是指定键不存在时的返回值（省略则返回None）
```

## 6.2 遍历字典
**遍历键值对** ```dic.items()```
```python
for k, v in user_0.items():
```
**遍历键（默认）** ```dic.keys()``` 
```python
for name in favorite_languages.keys():
# 也可以不声明
for name in favorite_languages:
```
该操作返回的是列表,因此可以使用sorted()等函数  

**遍历值** ```dic.values()```
```python
for language in favorite_languages.values():
```

## 6.3 集合
```python
languages = {'python', 'rust', 'python', 'c'} # 无序
```
集合会自动剔除重复元素，因此可以用于寻找列表中的不重复元素
```python
set(list)
```
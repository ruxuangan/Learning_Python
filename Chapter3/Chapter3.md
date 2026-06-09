# <font><center>Chapter 3 : 列表</center></font>
## 3.1 列表(list)
```bicycles = ['trek', 'cannon dale', 'redline', 'specialized']```  
索引 : ```bicycles[0]```，若是字符串，同样可使用“.函数”  
> 第一个元素是0，最后一个元素是-1   

## 3.2 修改，删除，添加元素  
**修改** ：直接对元素赋新值```motorcycles[0] = 'ducati'```
**删除** ：删除：```del motorcycles[0]```或```.pop()```(默认最后一个元素)
&emsp;&emsp;&emsp; 删除特定值```.remove()```(只会删除第一个)
**添加** ：末尾追加 ：```.append()```
&emsp;&emsp;&emsp; 插入：```.insert()```

## 3.3 管理列表
### 3.3.1 排序
```python
list.sort()               # 按首字母升序排列
list.sort(reverse = True) # 按首字母降序排列
sorted(list)              # 临时性的排序，也可使用reverse
list.reverse()            # 逆序排列
```
### 3.3.2 确定列表长度
```python
len(list)
```

## 3.4 使用列表时避免索引错误
尝试打印列表
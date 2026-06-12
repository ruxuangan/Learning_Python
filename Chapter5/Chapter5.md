# <font><center>Chapter 5 : if 语句</center></font>
## 5.1 条件测试
| 符号 | 含义 |
|--|--|
| == | 相同，大小写敏感|
| != | 不同，大小写敏感 |
| and | 和，不必须加括号 |
| or | 或，不必须加括号 |   

**条件判断也适用于列表**
```python
if 1 (not) in number:
```  

## 5.2 if 语句
if elif else, 可包含多个elif

## 5.3 使用 if 语句处理列表  
### 5.3.1 确定列表非空
```python
number = []
if number:      # 若列表非空，会返回True
    some lines
else:
    some lines
```
> 对于数值0、空值None、单引号空字符串''、双引号空字符串""、空列表[]、空元组()、空字典{}，Python都会返回False。  


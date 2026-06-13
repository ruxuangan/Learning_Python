# <font><center>Chapter 7 : 用户输入和 while 循环</center></font>
## 7.1 input() 函数
```python
message = input(prompt)
```
- 在 prompt 后留一个空格
- 需要数值时，检查是否使用了int()

## 7.2 while 循环
在处理循环条件较复杂的情况，可使用flag（标志）作为条件
```python
flat = True
while flag:
    message = input(prompt)
    if message == 'quit':
        flag = False
    else:
        print(message)
```
- break : 直接退出循环
- continue : 返回循环开头
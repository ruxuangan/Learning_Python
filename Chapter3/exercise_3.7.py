list = ["孙权","刘备","曹操"]
print(f"{list[0]},{list[1]},{list[2]}来与我共进晚餐")
print("我找到了更大的餐桌")
list.insert(0, "孙亮")
list.insert(2, "刘禅")
list.append("曹丕")
print(f"{list[0]},{list[1]},{list[2]},{list[3]},{list[4]},{list[5]}来与我共进晚餐")

print("现在只能邀请两人")
pop_guest = list.pop()
print(f"{pop_guest},抱歉，无法邀请您共进晚餐")
pop_guest = list.pop()
print(f"{pop_guest},抱歉，无法邀请您共进晚餐")
pop_guest = list.pop()
print(f"{pop_guest},抱歉，无法邀请您共进晚餐")
pop_guest = list.pop()
print(f"{pop_guest},抱歉，无法邀请您共进晚餐")

print(f"{list[0]},{list[1]}仍在邀请之列")
del list[0]
del list[0]
print(list)
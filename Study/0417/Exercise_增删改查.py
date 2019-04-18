#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:acmemax
list = ["飘逸的云", "花凉忆成殇", "花殇", "倦鸟栖梧", "忘誋旋律", "扼晚风", "紫蝶夢", "彡丨king霸荒", "亡梦爱人"]
for friend in list:
    print(friend+"，你好！")

# 在数组后面加一个新的元素 append()在类比列表后面加上一个新的元素
list2 = ["飘逸的云", "花凉忆成殇", "花殇", "倦鸟栖梧", "忘誋旋律", "扼晚风", "紫蝶夢", "彡丨king霸荒", "亡梦爱人"]
list2.append("acmemax")
print(list2)

# 使用insert（）可以将元素加在任何位置
list3 = ["飘逸的云", "花凉忆成殇", "花殇", "倦鸟栖梧", "忘誋旋律", "扼晚风", "紫蝶夢", "彡丨king霸荒", "亡梦爱人"]
list3.insert(2, "acmemax")
print(list3)

# 如果知道元素所在的位置  可以使用del删除元素
list4 = ["飘逸的云", "花凉忆成殇", "花殇", "倦鸟栖梧", "忘誋旋律", "扼晚风", "紫蝶夢", "彡丨king霸荒", "亡梦爱人"]
del list4[1]
print(list4)

# pop()方法可以从列表末尾删除元素
list4.pop()
print(list4)

#remove()方法可以根据值来删除列表里面的元素
list4.remove("扼晚风")
print(list4)

# 练习
L1 = ["飘逸的云", "花凉忆成殇", "花殇", "倦鸟栖梧", "忘誋旋律", "扼晚风", "紫蝶夢", "彡丨king霸荒", "亡梦爱人"]
for L in L1:
    print(L+"先生，我在这诚邀年来参加我的晚会")

M = L1.pop(2)
L1.insert(2, "acmemax")
L=L1[2]
print("因为" + M + '先生有事不能前来参加，所以为邀请了' + L + "先生")
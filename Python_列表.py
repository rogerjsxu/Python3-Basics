# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 10:06:30 2020

@author: xujia
"""


#列表(注意各元素完整性)
list1 = [2020,[1,5,6],"Python_list"]
list2 = ["2020",[1,2,[3,4]],{"number":"3"}]
list3 = [] #空列表

#print (list1[1:4])

#列表遍历(迭代)
#for i in [list1]:
#    print(i)
    
#列表追加
#list1.append("appended_element")
#print (list1)

#列表元素删除
#del list1[1]
#print (list1)

#列表组合
#list3 = list1 + list2
#print (list3) 

#列表重复
#list4 = list1*2 
#print (list4) 
 
#列表元素个数
#len(list2)  

#


#词典遍历
d = {"data":{"list":[{"movie_name":"movie1","movieID":123},{"movie_name":"movie2","movieID":343}]}}
for i in d["data"]['list']:
    print("{},{}".format(i["movie_name"],i["movieID"]))
    

# task1
# 生成[2,4,6,8,10,12,14,16]
list1 = []
'''
for i in range(1,9):
    list1.append(2*i)
'''
x = 2
while x<=16:
    list1.append(x)
    x+=2


# task2
# 生成 3*4 的 零列表 3行4列
# [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
list2 = []
for i in range(3):
    list2.append([])
    for j in range(4):
        list2[i].append(0)


# task3
# 用函数生成a*b的 零列表 a行b列
# 函数接受a，b作为参数

def gen_list(a,b):
    list3 = []
    for i in range(a):
        list3.append([])
        for j in range(b):
            list3[i].append(0)
    return list3

a1 = gen_list(5,2)
a2 = gen_list(4,8)
a3 = gen_list(8,7)
print(a1)
print(a2)
print(a3)

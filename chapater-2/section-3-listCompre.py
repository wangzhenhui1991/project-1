# 列表生成式
# 即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。

# 举个例子，要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))
print(list(range(1,11)))

# 但是要成成[1x1, 2x2, 3x3, ..., 10x10]
# 方法1是循环
L = []
for x in range(1,11):
    L.append( x * x);
print(L)
# 方法2是使用列表生成式
L2 = [ x * x for x in range(1,11)]
print(L2)
L3 = [ x + x for x in range(1,11) if x % 2 ==0]  # 还可以加判断
print(L3)
L4 = [ x + y for x in 'ABC' for y in '123']  # 嵌套两个变量，生成全排列
print(L4)
L5 = [x + y + z for x in 'ABC' for y in '123' for z in '①②③']
print(L5)


import os
L6 = [d for d in os.listdir('.')]
print(L6)


d1 = {'Amy':17,'Bob':14,'Cindy':15}
L7 = [name +' is '+str(age)+' years old' for name,age in d1.items()]
print(L7)
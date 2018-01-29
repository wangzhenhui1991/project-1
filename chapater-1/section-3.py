### 本章节 用来介绍python的数据类型
#   这种变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言。
#   静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错。例如java


### 整数
print('测试整数类型:')
a =10
a1 = 100000000000000000000000000000000000000
a2 = 0xf #0x表示十六进制
print(a,a1,a2)
### 浮点
print('测试浮点类型:')
f = 1.23
f2 = -0.31
f3 = 1.23e9

print(f,f2,f3);

##关于python的除法精确问题
f4 = 10/3
f5 = f4*2
f6 = f5*3/2
print(f4,f5,f6)

f7 = 10//3 #还有一种除法是//，称为地板除，两个整数的除法仍然是整数
print(f7)
### 字符串
print('测试字符串类型:')
s = 'hello python!'
s1 = "hello python!"
s2 = '你好 python!'
s3 = '你好 \'python\'!' #转义字符\'='  还有\n \t \r  \\
print(s,s1,s2,s3)
# 如果字符串里面有很多字符都需要转义，就需要加很多\，
# 为了简化，Python还允许用r''表示''内部的字符串默认不转义，
s4 = '\t'
s5 = r'\t'
print(s4,s5)

#如果字符串内部有很多换行，用\n写在一行里不好阅读，
# 为了简化，Python允许用'''...'''的格式表示多行内容，

s6 = '''line1...line2...line3'''
s7 = '''line1
        ...line2
        ...line3'''
print(s6,s7)


s8 = '123'
print(int(s8))   #python 将字符串转成整形的方法


### 布尔值
print('测试布尔类型:')
b  = True
b1 = False
print(b,b1);
print(b and b1)
print(b or b1)
print(not b)


### 空值

n = None
print(n)


### 数组
list  = ['Amy','Bob','Cindy']
print(list,len(list))
print(list[0],list[1],list[2])   # print(list[3]) 会报错IndexError
print(list[-1],list[-2],list[-3]) #取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素
list.append('David')   ### 在末尾添加元素
print(list)
list.insert(2,'Bill')  ### 在制定位置添加元素
print(list)
list.pop()             ### 从末尾删除元素
list.pop(2)           ### 从指定位置删除元素
print(list)
list[0] = 'Alice'
print(list)
list.append(['Zak','Zues'])  ### 也可直接追加另一个数组，len只增加1
print(list,len(list),list[3][0])
list.append(2)          ### 哇，都支持 不同类型的元素！真厉害
print(list)

### tuple
# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
# 它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的
tuple = ('Amy','Bob','Cindy')  #因为tuple不可变，所以代码更安全
print(tuple)
# 但是请小心tuple中嵌套了list
tuple1= ('Amy','Bob',['Cindy','Can'])
print(tuple1)
tuple1[2][0] = 'Zak';
tuple1[2][1] = 'Zues';
print(tuple1)



### 字典Map---dict

dict = {'Amy':17,'Bob':18,'Cindy':19}
name = 'Amy'
print(dict)
print(dict['Amy'],dict[name],dict.get(name)) ### 可以通过这三种方式获取字典中的Value
print('Zak' in dict) ##判断dict字典中是否存在'Zak' 这个Key
dict.pop('Cindy')  ### 删除某个Key的元素
print(dict)



### set集合
# set和dict类似，也是一组key的集合，但不存储value。
# 由于key不能重复，所以，在set中，没有重复的key
print('开始测试Set相关操作')

set = set([1,2,3])
print(set)
set.add(3,2,1)
print(set)
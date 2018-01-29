## 本章节来介绍python的常用条件语句

### if 和else
age =10
if age>=18:
    print('成年人');
elif age>14:
    print('青少年');
else:
    print('少年')



### for循环

list = ['a','b','c','d']
for ite in list:
    print(ite)

for ite in list:
    if ite == 'a':
        m = ite
        break;
print(m)

### while
start,end = 0,100;
sum = 0;
while start<end:
    start = start + 1;
    sum = sum + start;
print(sum)
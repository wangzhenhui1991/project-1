# 生成器
# 通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。
# 而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。

#所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
# 这样就不必创建完整的list，从而节省大量的空间。
# 在Python中，这种一边循环一边计算的机制，称为生成器：generator。


# 要创建一个generator，有很多种方法。
# 第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
L1 = (x * x for x in range(1,11))
print(L1)
for n in L1:
    print(n)


## 如何理解以及创建一个generator函数
# 这里，最难理解的就是generator和函数的执行流程不一样。
# 函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
# generator函数与普通函数最大的不同就在于yield关键字，可以理解yield是一种return，但是又在return的基础上，通过next调用可以保存本次调用的上下文
def process():
    print('start')
    yield 'start'
    print('doing')
    yield
    print('finished')

L2 = process()
for n in L2:
    print(n)



## 另一种理解方式，我们来写一个斐波拉契数列，
# 第一种方式是通过普通函数调用，计算出当前n值
def fib1(x):
    L = []
    n,a,b=0,0,1
    while n<x:
        a ,b =b, a + b;
        n = n+1;
        L.append(b)
    return L;
print(fib1(5))
# 第二种方式是通过generator函数调用，

def fib2(x):
    n,a,b=0,0,1
    while n< x:
        a ,b =b, a + b;
        n = n+1
        yield b;

for x in fib2(5):
    print(x)




# 写个杨辉三角
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]


def triangles(x):
    n=1;
    L = []


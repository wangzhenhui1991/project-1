

### 定义一个计算圆形面积的函数，入参是圆的半径，返回值是圆的面积
def area_of_circle(r):
    validateRequest(r)
    PI = 3.1415926535758
    return PI*r*r;

### 定义一个专门检查入参类型的函数，如果不符合我们预定的参数类型，会抛出一个异常
def validateRequest(req):
    if not isinstance(req,(int,float)):
        raise TypeError('错误的请求参数!')

r1 = 2
print(area_of_circle(r1))

### 定义一个暂时什么也不做的函数，pass
def func1():
    pass

### 函数返回多个值 ，本质是返回了一个tuple类型
def returnMulityValue():
    a = 'abc' \
        's'
    b = 10;
    c = ['Amy','Bob','Cindy'];
    return a,b,c;

x,y,z = returnMulityValue();
print(x,y,z)
print(returnMulityValue())

### 函数参数默认值，定义了一个指数函数，默认指数n=2
def power(x,n=2):
    sum = x;
    while n>1:
        n = n-1;
        sum = sum * x;
    return sum;

print(power(2,2))
print(power(2,4))
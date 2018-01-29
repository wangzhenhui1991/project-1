### 本章节是关于如何使用输入和输出函数

### 输出print
print("hello python");
print('hello','python','\t','.');
print(100+200);
print();
print('中文也是可以输出的');

print('格式化 hello,%s'%'python')
print('格式化输出:hello,%s,%d,%f%%' % ('python',1000,1.234))
print('格式化输出:hello,{0},{1},{2}%'.format('python',1000,1.234))

### 输入input
print('接下来测试输入:');
name = input();
print('你输入的是:\t'+name)

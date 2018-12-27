'''
s=input('age: ')
age=int(s)
if age>18:
    print(age)
    print('adult')
else:
    print('v')
    print('child')


sum=0
for  x in range(101):
    sum=sum+x
print(sum)

d = {
    'Michael': 95,
    'Bob': 75,
    'Tracy': 85
}
print('d[\'Michael\'] =', d['Michael'])
print('d[\'Bob\'] =', d['Bob'])
print('d[\'Tracy\'] =', d['Tracy'])
print('d.get(\'Thomas\', -1) =', d.get('Thomas', -1))

n1=255
n2=1000
L: List[int]=[int(n1),int(n2)]
for l in L:
    print(hex(l))


from product import pro
print(pro(5,6,7))
from product import trim
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
m = (x * x for x in range(5))
print(m)
for x in m:
  print(x)

#直接加
b=int(input())
total=0;
for i in range(b+1):
     total = i+total
print(total)
#判断函数
a=int(input())
if a%2==0 and a%3==0:
    print('能被2和3整除')
elif b%2==0:
    print('该数字能被 2 整除')
elif b%3==0:
    print('该数字能被 3 整除')
else:
    print('不能被2和3整除')

for i in range(1000):
    if i<100:
        continue
    s = 0
    a = int(i//100)
    b = int(i//10%10)
    c = int(i%10)
    s = a**3+b**3+c**3
    if s == i:
        print("{%d} 是水仙花数"% i)
abs=10
print(abs)#abs(-11)此时不成立
del abs
print(abs(-11))

#sorted 排序
m=list(sorted([1,-1,15,59,12,-89],key=abs,reverse=True))
print(m)
#匿名函数
L=list(filter(lambda n:n%2==1,range(1,20)))
print(L)

#偏函数
import functools
int2 = functools.partial(int, base=2)
print(int2('1000000'))
'''
# 模块的使用
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
' a test module '

__author__ = 'Michael Liao'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()
'''
# 面向对象编程
# 类和实例,访问限制
'''
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def print_score(self):
       # print('%s: %s' % (self.name, self.score))
       return self.name,self.score  
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 80:
            return 'B'
        elif self.score >= 70:
            return 'C'
        else:
            return 'D' 

bart = Student('Bart Simpson', 59)
lisa=Student('Lias Rong',32)
print(lisa.name)
print(bart.name,bart.print_score())
'''
# 访问限制
'''
class Student(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender
    def get_gender(self):
        return self.__gender
    def set_gender(self,gender):
        self.__gender = gender
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')
'''
# 继承与多态
'''
class Animal(object):
    def run(self):
        print('animal is running...')
class Dog(Animal):
    def run(self):
        print('Dog is running...')
    def eat(self):
        print('Dog is eat...')
class Cat(Animal):
    def run(self):
        print('Cat is running...')
    def eat(self):
        print('Cat is eat...')
def run_twice(animal):
    animal.run()
    animal.run()
dog=Dog() ;dog.run()
cat=Cat();cat.run()
run_twice(dog);run_twice(cat)
def count():
    fs = []
    for i in range(1, 4):#1 2 3
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()#

print(f1())
'''


# 实例属性和类属性
class Student(object):
    def set_age(self, age):
        self.age = age

    def set_name(self, name):
        self.name = name

    __slots__ = ('name', 'age')


s = Student()
s.name = 'Manson'
print(s.name)
s.age = 15
print(s.age)

#! /usr/bin/env python3# -*- coding:utf-8 -*- 'meta class test'#import pdb'''class A(object):	print("class A set")	pass	class B(A):	print("class B set")	passa = A()b = B()print(A)''''''def upper_attr(future_class_name, future_class_parents,	future_class_attr):	attrs = ((name, value )  for name, value in future_class.attr.items() if not name.startwith('__') )	print(attrs)	uppercase_attr = dict((name.upper(), value) for name, value in attrs.items()) 	return type(future_class_name, future_class_parents, attrs)class Foo(object):	__metaclass__ = upper_attr	bar = 'bip'	print( hasattr(Foo, 'bar'))print( hasattr(Foo, 'BAR'))f = Foo()print(f.BAR)'''class A(object):	name = 'aaa'# 元类会自动将你通常传给‘type’的参数作为自己的参数传入  def upper_attr(future_class_name, future_class_parents, future_class_attr):      #'''返回一个类对象，将属性都转为大写形式'''      print('meta class ... ') 	#  选择所有不以'__'开头的属性      attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))            # 将它们转为大写形式      uppercase_attr = dict((name.upper(), value) for name, value in attrs)         # 通过'type'来做类对象的创建      return type(future_class_name, future_class_parents, uppercase_attr)     __metaclass__ = upper_attr  #  这会作用到这个模块中的所有类     class Foo(object):      # 我们也可以只在这里定义__metaclass__，这样就只会作用于这个类中      bar = 'bip'     #pdb.set_trace()    print('sssss')      print(hasattr(Foo, 'bar'))# 输出: False  print(hasattr(Foo, 'BAR')) # 输出:True     f = Foo()  print(f.BAR)# 输出:'bip'  
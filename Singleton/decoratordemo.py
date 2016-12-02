

def demo1(func):
	print("decorator no param")
	return func

def demo2(arg):
	def demofunc(func):
		print("decorator param :" + arg)
		return func
	return demofunc

def demo3(func):
	print("double decorator")
	return func

@demo1
def DecoratorNoParamFunc():
	pass

@demo1
class DecoratorNoparamClass():
	pass

@demo2("Hello World")
def DecoratorParamFunc():
	pass

@demo2("Hello World")
class DecoratorParamClass():
	pass

@demo3
@demo1
def DoubleDecorator():
	pass

def test():
	print("Hello world")






#python 2
'''
class Singleton():
	def __new__(cls,*args,**kwargs):
		if not hasattr(cls,'_instance'):
			orig = super(Singleton,cls)
			cls._instance = orig.__new__(cls,*args,**kwargs)
		return cls._instance
'''

#python 3
class Singleton():
	def __new__(cls,*args,**kwargs):
		if not hasattr(cls,"_instance"):
			orig = super()
			cls._instance = orig.__new__(cls,*args,**kwargs)
		return cls._instance

#Decorator
def singleton(cls):
	_instance = {}
	def getInstance(*args,**kwargs):
		if cls not in _instance:
			_instance[cls] = cls(*args,**kwargs)
		return _instance[cls]
	return getInstance

@singleton
class CA():
	pass

ins_1 = CA()
ins_2 = CA()


print(ins_1 == ins_2)



































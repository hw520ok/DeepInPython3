

_instance = {}
def singleton(cls):

	def _getInstance(*args,**kwargs):
		if cls not in _instance:
			_instance[cls] = cls(*args,**kwargs)
		return _instance[cls]
	return _getInstance



A_instance = None

class A():
	def __init__(self):
		print("init")

	def __call__(self,*args,**kwargs):
		print("call")
		if A_instance == None:
			A_instance = A(*args,**kwargs)
		return A_instance

	@classmethod
	def getInstance(cls):
		print(cls)
		return cls

print(A.getInstance())
#a = A.getInstance()
#b = A.getInstance()

#print(a)
#print(b)

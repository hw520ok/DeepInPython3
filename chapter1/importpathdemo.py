import sys


def dotest():
	print (sys.path)
	sys.path.insert(0,"./")
	print(sys.path)

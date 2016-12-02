
def dolistdemo():
	print("===============list===============")
	a_list = ["a","b", "hello world", "list test", "five or four"]
	print(a_list)
	print(a_list[0])
	print(a_list[-1])

	print("===============slice===============")
	a_slice = a_list[0:len(a_list)]
	print(a_slice)

	print("===============add item to list===============")
	a_list = ["list"]
	a_list = a_list + ["new Str1","new Str2"]
	print(a_list)
	a_list = a_list + [10.0,13]
	print(a_list)
	a_list.append(True)
	a_list.extend([True]) #param only a list
	a_list.insert(0,"O0")
	print(a_list)

	print("===============difffrent between append and extend===============")
	a_list = ["list"]
	a_list.append(["a","b","c"])
	print(a_list,"len:" + str(len(a_list)))
	a_list = ["list"]
	a_list.extend(["a","b","c"])
	print(a_list,"len:" + str(len(a_list)))

	a_list = [1]
	if a_list:
		print(True)
	else:
		print(False)

def dosetdemo():
	a_set = {1}

	a_list = ["a","b","c","d","a"]
	a_set = set(a_list)
	print(a_set)
	a_set.discard("a")
	print(a_set)

dosetdemo()

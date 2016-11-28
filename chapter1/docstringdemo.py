
SUFFIX = {
1000:['KB','MB','GB','TB','PB','EB','ZB','YB'],
1024:['KiB','MiB','GiB','TiB','PiB','EiB','ZiB','YiB']}

def approximate_size(size,a_kilobyte_is_1024_bytes=True):
	'''
		this is doc string
	'''
	multiple = 1000 if a_kilobyte_is_1024_bytes else 1024
	for suffix in SUFFIX[multiple]:
		size /= multiple
		if size < multiple:
			return "{0:.1f} {1}".format(size,suffix)

def dotest():
	print(approximate_size(1000000000000,True))
	print(approximate_size(1000000000000,False))
	print(approximate_size.__doc__)

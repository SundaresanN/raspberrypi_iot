x = 10
def add(a,b):
	global x
	c=a+b
	print(c)
	print(x)
	print(x+c)
	x+=c
	print(c)
add(10,10)

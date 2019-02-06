string="pythonbestforbeginners"
print(string[1:22:2])
print(string[::-1])
print(string.replace(string[2],"@"))
l=len(string)
for i in range(1,l):
	if(i%3==0):
		newstr=(string.replace(string[i],'@'))
print(newstr)
substr="hello world"
print(substr.replace("hello","hai"*3))
a=10
b=20
a=a+b
b=a-b
a=a-b
print(a)
print(b)





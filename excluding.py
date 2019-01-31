>>> print("numbers excluding multiples of 3 and 5 are:")
numbers excluding multiples of 3 and 5 are:

>>> for i in range(0,40):
	if(i%5==0 or i%3==0):
		continue
	print(i,end=' ')

	
1 2 4 7 8 11 13 14 16 17 19 22 23 26 28 29 31 32 34 37 38 
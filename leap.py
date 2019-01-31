>>> year=int(input("Enter the year:"))
Enter the year: 2004
>>> if((year%4==0) or (year%400==0) and (year%100!=0)):
	print("It is a leap year")
else:
	print("Not a leap year")

	
It is a leap year

>>> year=int(input("Enter the year:"))
Enter the year:2009
>>> if((year%4==0) or (year%400==0) and (year%100!=0)):
	print("It is a leap year")
else:
	print("Not a leap year")

	
Not a leap year
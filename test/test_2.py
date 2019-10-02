
number = input("Enter number: ")
number = list(str(number))

for i in range(len(number),-1,-1):
	for j in range(i):
		print(number[j],end=' ')
	print("")
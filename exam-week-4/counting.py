def counting(input1):
	list1=[]
	for i in range(input1+1):
		rep=bin(i)
		count=0
		
		for char in rep:
			if char=='1':
				count+=1
		list1.append(count)
	print(list1)

counting(15)
counting(16)
counting(1)
counting(25)
counting(5)
counting(6)
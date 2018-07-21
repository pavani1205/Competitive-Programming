def binary(input1):
	rep=bin(input1)
	list1=[]
	count=0
	count2=0
	count0=0
	countconseq=0
	if input1==0:
		print('0')
	else:
		for char in rep:
			if char=='1' and count0==0 and count==0:
				count=1
			elif char=='0' and count==1:
				count2+=1
				count0=1
			elif char=='1' and count0==1 and count==1:
				count2+=1
				count0=0
				count=0
				list1.append(count2)
			elif char=='1' and count==1 and count0==0:
				countconseq=1
		if countconseq==1 and len(list1)==0:
			print('1')
		elif countconseq==0 and len(list1)==0:
			print('0')
		else:
			print(max(list1))


binary(0)
binary(55)
binary(-5)
binary(12354)
binary(6)
binary(256)
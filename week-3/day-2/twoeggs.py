def eggs(number):
	num=14
	i=0
	j=0
	while i<number:
		j=i
		i=i+num
		num-=1
		print(i,end=",")
		
	for k in range(j+1,number+1):
		print(k,end=",")

eggs(13)
print()
eggs(98)
print()
eggs(89)
print()
eggs(31)
print()
eggs(72)
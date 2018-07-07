def couples(list1):
	count=0
	for i in range(len(list1)-1):
		if list1[i]%2==0:
			req=list1[i]+1
		else:
			req=list1[i]-1
		if list1[i+1]!=req:
			for j in range(i+1,len(list1)):
				if list1[j]==req:
					list1[i+1],list1[j]=list1[j],list1[i+1]
					count+=1
	return count

print(couples([1,3,4,0,2,5]))
print(couples([3,2,0,1]))
print(couples([1,0]))
def queueheight(list1):
	list1.sort()
	list3=[]
	for k in range(len(list1)):
		list2=[]
		for i in list1:
			if i[1]<=len(list3):
				list2.append(i)
		count=0
		for i in list2:
			for j in list3:
				if i[0]<=j[0]:
					count+=1
			if count==i[1]:
				list3.append(i)
				list1.remove(i)

			
	print(list3)

queueheight([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])
queueheight([[12,0],[6,3],[3,4],[9,2], [11,1],[1,5]])
queueheight([ [2,4], [5,1], [3,3], [1,5], [4,2], [6,0]])
queueheight([[6,0],[4,4],[5,3],[6,2],[4,0],[7,0],[7,1],[5,0]])
def meetingpoint(list1):
	list2=[]
	
	for i in range(len(list1)):
		for j in range(len(list1[i])):
			sum1=0
			for k in range(len(list1)):
				for k1 in range(len(list1[k])):
					if list1[k][k1]==1:
						sum1+=abs(i-k)+abs(j-k1)
			list2.append(sum1)
	print(min(list2))
meetingpoint([[1, 0, 0, 0, 1], 
                   [0, 0, 0, 0, 0],
                   [0, 0, 1, 0, 0]])
meetingpoint([[0, 0],
                     [0, 0]])
meetingpoint([[1, 0, 1, 0, 1],
                     [0, 1, 0, 0, 0], 
                     [0, 1, 1, 0, 0]])
meetingpoint([[1, 1],
                     [1,1]])
meetingpoint([[1, 0],
                     [0, 0]])
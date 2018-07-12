def morsecode(list1):
	set1=set()
	dict1={'A':".-",'B':"-...",'C':"-.-.",'D':"-..",'E':".",'F':"..-.",'G':"--.",
		'H':"....",'I':"..",'J':".---",'K':"-.-",'L':".-..",'M':"--",'N':"-.",'O':"---",'P':".--.",'Q':"--.-",
		'R':".-.",'S':"...",'T':"-",'U':"..-",'V':"...-",'W':".--",'X':"-..-",'Y':"-.--",'Z':"--.."}
	
	for str1 in list1:
		string=""
		str1=str1.upper()
		for char in str1:
			string+=dict1[char]
		set1.add(string)
	return len(set1)

print(morsecode(["gin", "zen", "gig", "msg"]))
print(morsecode(["a", "z", "g", "m"]))
print(morsecode(["bhi", "vsv", "sgh", "vbi"]))
print(morsecode(["a", "b", "c", "d"]))
print(morsecode(["hig", "sip", "pot"]))




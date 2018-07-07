import unittest


def get_permutations(string1,string2):
    string1=string1.lower()
    string2=string2.lower()
    list1=list(string1)
    list2=list(string2)
    for i in list1:
        if i==' ':
           list1.remove(i)
    for i in list2:
        if i==' ':
            list2.remove(i)
    for i in list1:
        if i in list2:
            list2.remove(i)
    return len(list2)==0

print(get_permutations("anagram","nagaram"))
print(get_permutations("Keep","Peek"))
print(get_permutations("Mother In Law","Hitler Woman"))
print(get_permutations("School Master","The Classroom"))
print(get_permutations("ASTRONOMERS","NO MORE STARS"))
print(get_permutations("Toss","Shot"))
print(get_permutations("joy","enjoy"))
print(get_permutations("Debit Card","Bad Credit"))
print(get_permutations("SiLeNt CAT","LisTen AcT"))
print(get_permutations("Dormitory","Dirty Room"))

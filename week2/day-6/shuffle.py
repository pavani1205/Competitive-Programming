import random

def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)

def shuffle(the_list):
    if len(the_list) <= 1:
        return the_list

    last = len(the_list) - 1
    for index in range(0, len(the_list) - 1):
    	random = get_random(index,last)
    	if random != index:
    		the_list[index], the_list[random] =the_list[random], the_list[index]


sample_list = [1, 2, 3, 4, 5]
print ('Sample list:', sample_list)
print ('Shuffling sample list...')
shuffle(sample_list)
print (sample_list)

sample_list = [6,7,8,9,10]
print ('Sample list:', sample_list)
print ('Shuffling sample list...')
shuffle(sample_list)
print (sample_list)

sample_list = [11,12,13,14,15]
print ('Sample list:', sample_list)
print ('Shuffling sample list...')
shuffle(sample_list)
print (sample_list)

sample_list = [16,17,18,19,20]
print ('Sample list:', sample_list)
print ('Shuffling sample list...')
shuffle(sample_list)
print (sample_list)

sample_list = [21,22,23,24,25]
print ('Sample list:', sample_list)
print ('Shuffling sample list...')
shuffle(sample_list)
print (sample_list)
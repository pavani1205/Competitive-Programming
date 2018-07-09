import random


def rand5():
    return random.randint(1, 5)


def rand7():
    while True:
        roll1 = rand5()
        # print("roll1 ",roll1)
        roll2 = rand5()
        # print("roll2 ",roll2)
        outcome_number = (roll1-1) * 5 + (roll2-1) + 1
        # print(outcome_number)
        if outcome_number > 21:
            continue
        # print(outcome_number % 7 + 1)
        return outcome_number % 7 + 1


print ('Rolling 7-sided die...')
print (rand7())
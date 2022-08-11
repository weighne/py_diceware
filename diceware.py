import random
import json

with open("diceware.json", "r") as word_list:
    dice_dict = json.load(word_list)

def random_number(seed):
    nums = [random.randint(1,6) for x in range(6,seed)] #generate a whole numch of numbers between 1,6 and pick some randomly
    return random.choice(nums)
        

while True:
    request = int(input("How many words?: "))
    seed = int(input("Enter seed number (ex:420): "))
    phrase = ''
    nums = [''.join([str(random_number(seed)) for x in range(5)]) for y in range(request)]
    phrase = ' '.join([dice_dict[str(x)] for x in nums])
    print(phrase)
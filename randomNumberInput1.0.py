import random

while True:
    question = input('Do you want to play? (Y/N)')
    answer1 = int(input('How many numbers you want?'))
    answer2 = int(input('max integer(1,X)')
    if (question == 'no'):
        break
    else:
        count = answer1
        # the amount of random numbers

        while count >= 1:
            count -= 1
            x = random.randint(1, answer2)
        # the numbers it barfs

            print(x)
import random

max_number = input("Choose a number between 10 and 100 ")
is_valid_max_number = False


while not is_valid_max_number:
    if not max_number.isdigit():
        print("You must choose a valid number, not a letter")
        max_number = input("Please, choose a number between 10 and 100 ")

    elif max_number.isdigit():
        max_number = int(max_number)
        if max_number < 10 or max_number > 100:
            print("You must choose a number between 10 and 100!\n")
            max_number = input("Please, choose a number between 10 and 100 ")
        else:
            is_valid_max_number = True

random_number = random.randint(1, max_number)
counter = 1

# ALTERNATIVE WAY FOR USING WHILE LOOP : CONTINUE AND BREAK STAMENTS
while True:
    answer = input("Guess a number between 1 and " + str(max_number)+": ")
    if answer.isdigit():
        answer = int(answer)
    else:
        print("Please, type a number, not a letter")
        continue
    # print("random number is " + str(random_number))
    counter += 1
    if answer > random_number:
        print("Wrong! Try a smaller number")
        continue
    elif answer < random_number:
        print("Wrong! Try a bigger number")
        continue
    elif answer == random_number:
        print("Welldone!\nYou got it in " + str(counter))
        break

import random
top_of_range = input("Type a range number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range < 0:
        print("Please type a number greater than 0 next time ")
        quit()
else:
    print("Please type a number next time...")
    quit()


random_number = random.randint(0, top_of_range)
count = 1
while True:
    user_guess = input("make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Type a number next time")
        continue

    if user_guess == random_number:
        print("You got it correct....")
        print("you made it in " +str(count)+" time")
        break
    else:
        if user_guess > random_number:
            print("The random number is less than "+ str(user_guess))
        else:
            print("The random number is greater than "+ str(user_guess))
        count += 1
quit()
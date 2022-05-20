print("Welcome to Quiz Game")
ask = input("Do you wana play Quiz Game? (y/n)")
if ask !="yes":
    print("Thank you")
    quit()
print("Lets Get started......")
score = 0
q1=input("What is the full form of CPU? ")
if q1.lower() == "central processing unit":
    print("Correct...")
    score = score+1
else:
    print("Incorrect")

q2 = input("What is the height of Mt everest? ")
if q2.lower() =="8848":
    print("correct...")
    score += 1
else:
    print("incorrect")

q3 = input("Where is swoyambhu? ")
if q3.lower() =="kathmandu":
    print("correct...")
    score = score + 1
else:
    print("incorrect")

q4 = input("What is full form of RAM? ")
if q4.lower() =="random access memory":
    print("correct...")
    score = score + 1
else:
    print("incorrect")

q5 = input("What is capital city of pakistan? ")
if q3.lower() =="isalamabad":
    print("correct...")
    score = score + 1
else:
    print("incorrect")
print("Your total score is: "+str(score))
print("you got:"+str((score/5)*100)+"%")
print("Thank you for playing this game..")





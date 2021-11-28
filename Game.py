import random
#This gets the questions for the true or false quiz
def get_tof_questions():
    statements = []
    statements.append(["Tigers have stripes","T"])
    statements.append(["The earth is flat","F"])
    statements.append(["The capital city of England is London","T"])
    statements.append(["Prince Harry is taller than Prince William","F"])
    statements.append(["The star sign Aquarius is represented by a tiger","T"])
    statements.append(["Meryl Streep has won two Academy Awards","F"])
    statements.append(["Marrakesh is the capital of Morocco","F"])
    statements.append(["Idina Menzel sings 'let it go' 20 times in 'Let It Go' from Frozen","F"])
    statements.append(["Waterloo has the greatest number of tube platforms in London","T"])
    return statements

#This gets the questions for the genral knowledge quiz
def get_questions():
    statements = []
    statements.append(["Quito is the capital of which South American country?","EQUADOR"])
    statements.append(["New York City's Brooklyn Bridge links Long Island with which other island in the city?","MANHATTAN"])
    statements.append(["The Royal Albert Dock is found in which UK city?","LIVERPOOL"])
    statements.append(["English astronomer John Couch Adams discovered which planet in 1846?","NEPTUNE"])
    statements.append(["Castel Sant'Angelo, or The Mausoleum of Hadrian, is a prominent building located in which European city?","ROME"])
    statements.append(["Martin Tyler is well-known for his appearance in the commentary box in which sport?","FOOTBALL"])
    statements.append(["As of 2021, Clement Attlee remains the longest-serving leader of which British political party?","LABOUR"])
    statements.append(["Footballer Kenny Dalglish won 102 caps for which country?","SCOTLAND"])
    statements.append(["The English word 'aviation', meaning the flying or operation of aircraft, origins in which European language?","FRENCH"])
    return statements

#This is where the true of false quiz is played
def play_tof_quiz():
    questions = get_tof_questions()
    random.shuffle(questions)
    score = 0
    print("Please answer with T for true or F for false")
    for s in questions[:5]:
        guess = input("True of false: "+s[0]+" ")
        if guess.upper() == s[1]:
            print("Correct")
            score = score + 1
        else:
            print("Incorrect")
    print("Your final score is",str(score)+"/5")

#this is where the genral knowledge quiz is played
def play_multiple():
    questions = get_questions()
    random.shuffle(questions)
    score = 0
    for s in questions[:5]:
        guess = input(s[0]+" ")
        if guess.upper() == s[1]:
            print("Correct")
            score = score + 1
        else:
            print("Incorrect, the correct answer was ",s[1])
    print("Your final score is",str(score)+"/5")

#this is where the easy maths game is played
def play_easy_maths():
    print("\nPlease answer in whole numbers")
    score = 0
    for counter in range(5):
        num1 = random.randint(1,10)
        num2 = random.randint(1,10)
        opration = random.randint(1,4)
        if opration == 1:
            answer = int(input("The question is: "+str(num1)+" x "+str(num2)+" "))
            if answer == (num1*num2):
                print("That was correct")
                score = score + 1
            else:
                print("That was incorrect, the correct answer was",num1*num2)
        if opration == 2:
            answer = int(input("The question is: "+str(num1)+" + "+str(num2)+" "))
            if answer == (num1+num2):
                print("That was correct")
                score = score + 1
            else:
                print("That was incorrect, the correct answer was",num1+num2)
        if opration == 3:
            answer = int(input("The question is: "+str(num1)+" - "+str(num2)+" "))
            if answer == (num1-num2):
                print("That was correct")
                score = score + 1
            else:
                print("That was incorrect, the correct answer was",num1-num2)
        if opration == 4:
            answer = int(input("The question is: "+str(num1)+" ÷ "+str(num2)+" "))
            if round(answer) == round(num1/num2):
                print("That was correct")
                score = score + 1
            else:
                print("That was incorrect, the correct answer was",round(num1/num2))
    print("You got",str(score)+"/5")

#this is where the the hard maths game is played
def play_hard_maths():
    print("\nPlease answer in whole numbers")
    score = 0
    for counter in range(5):
        num1 = random.randint(-100,100)
        num2 = random.randint(-100,100)
        opration = random.randint(1,4)
        if opration == 1:
            answer = int(input("The question is: "+str(num1)+" x "+str(num2)+" "))
            if answer == (num1*num2):
                print("That was correct")
                score = score + 1
            else:
                print("That was incorrect, the correct answer was",num1*num2)
        if opration == 2:
            answer = int(input("The question is: "+str(num1)+" + "+str(num2)+" "))
            if answer == (num1+num2):
                print("That was correct")
                score = score + 1
            else:
                print("That was incorrect, the correct answer was",num1+num2)
        if opration == 3:
            answer = int(input("The question is: "+str(num1)+" - "+str(num2)+" "))
            if answer == (num1-num2):
                print("That was correct")
                score = score + 1
            else:
                print("That was incorrect, the correct answer was",num1-num2)
        if opration == 4:
            answer = int(input("The question is: "+str(num1)+" ÷ "+str(num2)+" "))
            if round(answer) == round(num1/num2):
                print("That was correct")
                score = score + 1
            else:
                print("That was incorrect, the correct answer was",round(num1/num2))
    print("You got",str(score)+"/5")
    
#this is where the main menu is shown
def main():
    another_go = 0
    print("+--------------------------+")
    print("| Welcome to Oliver's quiz |")
    print("+--------------------------+")
    print("| Please select an option: |")
    print("|                          |")
    print("| 1. True or false quiz    |")
    print("| 2. Genral knowledge quiz |")
    print("| 3. Easy maths            |")
    print("| 4. Hard maths            |")
    print("| 0. Quit                  |")
    print("+--------------------------+")
    choice = input("What do you want to do? ")
    if choice == "1":
        play_tof_quiz()
    elif choice == "2":
        play_multiple()
    elif choice == "3":
        play_easy_maths()
    elif choice == "4":
        play_hard_maths()
    elif choice == "0":
        print("Thanks for playing")
        another_go = 1
    return another_go

#this is where the code is run to run the whole thing
replay = 0
while replay == 0:
    print("\n")
    replay = main()

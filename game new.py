import random
import time
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

#this gets the questions for the history quiz
def get_history_questions():
    statements = []
    statements.append(["Who was Henry VIII's last wife?","CATHERINE PARR"])
    statements.append(["Although never taking her seat, who was the first woman to be elected to the houses of parliament?","CONSTANCE MARKIEVICZ"])
    statements.append(["Which English king died in 1066, leaving no heir to the throne?","EDWARD THE CONFESSOR"])
    statements.append(["In which European country was there a civil war between 1946 and 1949?","GREECE"])
    statements.append(["Which St Albans pub claims to be the oldest English pub?","YE OLDE FIGHTING"])
    statements.append(["Who discovered penicillin?","ALEXANDER FLEMING"])
    statements.append(["What year did the Titanic sink?","1912"])
    statements.append(["Which Hertfordshire town had the first ever roundabout in the UK?","LETCHWORTH"])
    statements.append(["Which new British military force was established in 1918?","RAF"])
    statements.append(["Which Hertfordshire town was the first ever New Town after WWII?","STEVENAGE"])
    return statements

#this is where the multiple choice questions are created
def get_mul_questions():
    statements = []
    statements.append(["Which planet is closest to the sun?","A: Venus","B: Mercury","C: Mars","D: Saturn","B"])
    statements.append(["What is the longest that an elephant has lived?","A: 17 years","B: 49 years","C: 86 years","D: 109 years","C"])
    statements.append(["How did spider man get his powers?","A: Experiment went wrong","B: Born with them","C: Got them after a dream","D: Bitten by a radiocative spider","D"])
    statements.append(["Which animal dosn't appear in the Chinese zodiac?","A: Bear","B: Rabbit","C: Dragon","D: Dog","A"])
    statements.append(["How many holes are there on a standard bowling ball?","A: 1","B: 2","C: 3","D: 5","C"])
    statements.append(["What are the main colors on the the Spanish flag","A: Black and yellow","B: Green and white","C: Blue and white","D: Red and yellow","D"])
    statements.append(["In the nursery rhyme, how many blackbirds were baked in a pie?","A: 3","B: 13","C: 24","D: 36","C"])
    return statements

#this is where the multiple choice questions are played
def play_multiple_choice():
    questions = get_mul_questions()
    random.shuffle(questions)
    score = 0
    print("Please answer with A,B,C,D")
    for s in questions[:5]:
        print("\n"+s[0])
        for counter in range(1,5):
            print(s[counter])
        guess = input("What is your guess? ")
        if guess.upper() == s[5]:
            print("Correct")
            score = score + 1
        else:
            print("Incorrect: The correct answer was",s[5])
    print("Your final score is",str(score)+"/5")

#This is where the true of false quiz is played
def play_tof_quiz():
    questions = get_tof_questions()
    random.shuffle(questions)
    score = 0
    print("Please answer with T for true or F for false")
    print("\n")
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
    print("\n")
    for s in questions[:5]:
        guess = input(s[0]+" ")
        if guess.upper() == s[1]:
            print("Correct")
            score = score + 1
        else:
            print("Incorrect, the correct answer was ",s[1])
    print("Your final score is",str(score)+"/5")

#this is where the history quiz is played
def play_history_quiz():
    questions = get_history_questions()
    random.shuffle(questions)
    score = 0
    print("\n")
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
    
#this is where the calculator is programed
def calculator():
    while True:
        print("\nSelect operation.")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        choice = input("Please enter choice: ")
        if choice == "1" or choice == "2" or choice == "3" or choice == "4":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if choice == '1':
                print(num1, "+", num2, "=",(num1+num2))
            elif choice == '2':
                print(num1, "-", num2, "=",(num1-num2))
            elif choice == '3':
                print(num1, "x", num2, "=",(num1*num2))
            elif choice == '4':
                print(num1, "÷", num2, "=",(num1/num2))
        else:
            print("invalid input")
        redo = input("Another calculation Y/n: ")
        if redo == "n" or redo == "N":
          break
#this is where the adventure game is going to be played
def text_ad_game():
    #this determins the options that the user has
    ans_a = ["A","a"]
    ans_b = ["B","b"]
    ans_c = ["C","c"]
    yes = ["Y","yes","y","Yes","YES"]
    no = ["n","N","NO","no","No",]
    required = ("\nPlease only use A, B, or C\n")

    #this is where the game will be played
    def start():
        print("\nYou have woken up, you are in a prison cell"
          "\nYou have no reclation of this event")
        time.sleep(1)
        print("\nWhat will you do?"
          "\nA) Wait for the guard to arrive"
          "\nB) Try to pick the lock with a hair clip"
          "\nC) Bash on the cell to get the guards attention")
        choice = input("What do you want to do? ")
        if choice in ans_a:
            wait_for_guard()
        elif choice in ans_b:
            pick_lock()
        elif choice in ans_c:
            bash_on_cell()
        else:
            print(required)
            start()

    #this is what will happen if you go and wait for the guard
    def wait_for_guard():
        time.sleep(1)
        print("\nIt has been multiple hours")
        time.sleep(1)
        print("You are getting hungry, what will you do?"
              "\nA) Wait for the guard to arrive"
              "\nB) Try to pick the lock with a hair clip"
              "\nC) Bash on the cell to get the guards attention")
        choice = input("What do you want to do? ")
        if choice in ans_a:
            print("\nYou Died of hunger!")
        elif choice in ans_b:
            pick_lock()
        elif choice in ans_c:
            bash_on_cell()
        else:
            print(required)
            wait_for_guard()

    #this is what is going to happen if you pick the lock
    def pick_lock():
        time.sleep(1)
        print("\nYou sucsessfully picked the lock, but the guard heard you."
              "\nWill you"
              "\nA) Pretend the door is locked"
              "\nB) Make a run for it"
              "\nC) Leave the door open")
        choice = input("What do you want to do? ")
        if choice in ans_a:
            print("\nThe guard didn't suspect a thing"
                  "\nWhat will you do"
                  "\nA) Tip toe out"
                  "\nB) Run out")
            choice = input("What do you want to do? ")
            if choice in ans_a:
                outside()
            elif choice in ans_b:
                print("The guard caught you"
                      "\n Game over")
            else:
                print(required)
                pick_lock()
            
        elif choice in ans_b:
            print("The guard caught you"
                  "\n Game over")
        elif choice in ans_c:
            print("The guard brushed it off")
            time.sleep(1)
            print("\nWhat will you do?"
                  "\nA) Wait for the guard to arrive"
                  "\nB) Try to pick the lock with a hair clip"
                  "\nC) Bash on the cell to get the guards attention")
            choice = input("What do you want to do? ")
            if choice in ans_a:
                wait_for_guard()
            elif choice in ans_b:
                 print("\nYou sucsessfully picked the lock, but the guard heard you."
                        "\nWill you"
                       "\nA) Pretend the door is locked"
                       "\nB) Make a run for it"
                       "\nC) Leave the door open")
            choice = input("What do you want to do? ")
            if choice in ans_a:
                print("\nThe guard didn't suspect a thing"
                      "\nWhat will you do"
                      "\nA) Tip toe out"
                      "\nB) Run out")
                choice = input("What do you want to do? ")
                if choice in ans_a:
                    outside()
                elif choice in ans_b:
                   print("The guard caught you"
                          "\n Game over")
                else:
                    print(required)
                    pick_lock()
            
            elif choice in ans_b:
                print("The guard caught you"
                      "\n Game over")
            elif choice in ans_c:
                print("The guard caught you"
                      "\n Game over")
            else:
                print(required)
                pick_lock()
        else:
            print(required)
            pick_lock()

    #this is what is going to happen if you make noise
    def bash_on_cell():
        time.sleep(1)
        print("\nThe guard is constantly watching you now"
              "\nYou cant to anything"
              "\nGame over")
    def outside():
        time.sleep(1)
        print("\nWell done, you made it outside"
              "\nYou have the guard chasing after you"
              "\nWhat will you do?"
              "\nA) Give up"
              "\nB) Throw a stone at the guard"
              "\nC) Hide behind a tree")
        choice = input("What do you want to do? ")
        if choice in ans_a:
            time.sleep(1)
            print("The guard caught you"
                  "\n Game over")
        elif choice in ans_b:
            time.sleep(1)
            print("The guard is stunned"
                 "\nYou run out"
                 "\n\nYou Win!")
        elif choice in ans_c:
            time.sleep(1)
            print("The guard caught you"
                  "\n Game over")
        else:
            print(required)
            start()
    start()
    
#this is where the main menu is shown
def main_menu():
    menu = 1
    print("+--------------------------+")
    print("| Welcome to the main menu |")
    print("+--------------------------+")
    print("| Please select an option: |")
    print("|                          |")
    print("| 1. Quiz Menu             |")
    print("| 2. Maths menu            |")
    print("| 3. Game menu             |")
    print("| 0. Quit                  |")
    print("+--------------------------+")
    choice = input("What do you want to do? ")
    if choice == "1":
        menu = 3
    elif choice == "2":
        menu = 2
    elif choice == "3":
        menu = 4
    elif choice == "0":
        print("Thanks for playing")
        menu = 0
    return menu

#this is where the maths menu will be
def maths_menu():
    menu = 2
    print("+--------------------------+")
    print("| Welcome to the maths menu|")
    print("+--------------------------+")
    print("| Please select an option: |")
    print("|                          |")
    print("| 1. Calculator            |")
    print("| 2. Easy Maths            |")
    print("| 3. Hard Maths            |")
    print("| 0. Back                  |")
    print("+--------------------------+")
    choice = input("What do you want to do? ")
    if choice == "1":
        calculator()
    elif choice == "2":
        play_easy_maths()
    elif choice == "3":
        play_hard_maths()
    elif choice == "0":
        menu = 1
    return menu

#this is where the quizes menu is
def quizes_menu():
    menu = 3
    print("+--------------------------+")
    print("| Welcome to the quiz menu |")
    print("+--------------------------+")
    print("| Please select an option: |")
    print("|                          |")
    print("| 1. True or false quiz    |")
    print("| 2. Genral knowledge quiz |")
    print("| 3. History quiz          |")
    print("| 4. Multiple choice       |")
    print("| 0. Back                  |")
    print("+--------------------------+")
    choice = input("What do you want to do? ")
    if choice == "1":
        play_tof_quiz()
    elif choice == "2":
        play_multiple()
    elif choice == "3":
        play_history_quiz()
    elif choice == "4":
        play_multiple_choice()
    elif choice == "0":
        menu = 1
    return menu

#this is where the game menu is
def game_menu():
    menu = 3
    print("+--------------------------+")
    print("| Welcome to the game menu |")
    print("+--------------------------+")
    print("| Please select an option: |")
    print("|                          |")
    print("| 1. Adventure game        |")
    print("| 0. Back                  |")
    print("+--------------------------+")
    choice = input("What do you want to do? ")
    if choice == "1":
        text_ad_game()
    elif choice == "0":
        menu = 1
    return menu

#this is where the code is run to run the whole thing
replay = 0
menu = 1
while replay == 0:
    if menu == 1:
        print("\n")
        menu = main_menu()
    elif menu == 2:
        print("\n")
        menu = maths_menu()
    elif menu == 3:
        print("\n")
        menu = quizes_menu()
    elif menu == 4:
        print("\n")
        menu = game_menu()
    elif menu == 0:
        replay = 1
    else:
        main_menu

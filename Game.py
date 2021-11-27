import random
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

def main():
    another_go = 0
    print("+--------------------------+")
    print("| Welcome to Oliver's quiz |")
    print("+--------------------------+")
    print("| Please select an option: |")
    print("|                          |")
    print("| 1. True or false quiz    |")
    print("| 2. Genral knowledge quiz |")
    print("| 0. Quit                  |")
    print("+--------------------------+")
    choice = input("What do you want to do? ")
    if choice == "1":
        play_tof_quiz()
    elif choice == "2":
        play_multiple()
    elif choice == "0":
        print("Thanks for playing")
        another_go = 1
    return another_go

replay = 0
while replay == 0:
    print("\n")
    replay = main()

import random

def getWord():
    mywords = ["english","monitor","eagle","common","people",
               "during","attitude","difference","things",
               "walked","activate","shower","mobile","keyboard",
               "subtle","success","hardwork","doctor","driven",
               "determine","value","expert","strange","wicket",
               "miles","above","level","admission","amigo",
               "insane","eagle","merchant","princess"]

    word = random.choice(mywords)

    return word

chance = 5
while chance:
    score = 0

    print("Enter Correct word for the below letters: ")
    rword = getWord()

    shuffle_word = list(rword)

    random.shuffle(shuffle_word)

    shuffle_word = ''.join(shuffle_word)

    print(shuffle_word)

    userword = input()

    if userword == rword:
        print("Correct !!")
        score+=1
        chance-=1
    else:
        print("Wrong!!!")
        print("Correct Word is",rword)
        score-=1
        chance-=1

print("Your Score is",score)

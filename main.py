import random
words = ["hello", "about", "birds", "royal", "labor", "sunny", "cling", "manic", "bushy", "woody", "nurse"]
word = random.choice(words)
letter1 = word[0:1]
letter2 = word[1:2]
letter3 = word[2:3]
letter4 = word[3:4]
letter5 = word[4:5]
hang = 0
win = False

print(hang)
print(letter1 + letter2)
i = input("ENTER IN A LETTER: ")
while i != letter1:
        hang += 1
        if hang == 5 :
            print("UNFORTUNATELY YOU HAVE LOST THE GAME")
            break
        print("WRONG LETTER")
        print("ERRORS: " + str(hang))
        i = input("ENTER IN A LETTER: ")
if i == letter1:
    print(letter1)
    i = input("ENTER IN A LETTER: ")
    while i != letter2 :
        hang += 1
        if hang == 5 :
            print("UNFORTUNATELY YOU HAVE LOST THE GAME")
            break
        else:
            print("WRONG LETTER")
            print("ERRORS: " + str(hang))
        i = input("ENTER IN A LETTER: ")
    if i == letter2:
        print(letter1 + letter2)
        i = input("ENTER IN A LETTER: ")
        while i != letter3 :
            hang += 1
            if hang == 5 :
                print("UNFORTUNATELY YOU HAVE LOST THE GAME")
                break
            else :
                print("WRONG LETTER")
                print("ERRORS: " + str(hang))
            i = input("ENTER IN A LETTER: ")
        if i == letter3:
            print(letter1 + letter2 + letter3)
            i = input("ENTER IN A LETTER: ")
            while i != letter4 :
                hang += 1
                if hang == 5 :
                    print("UNFORTUNATELY YOU HAVE LOST THE GAME")
                    break
                else :
                    print("WRONG LETTER")
                    print("ERRORS: " + str(hang))
                i = input("ENTER IN A LETTER1: ")
            if i == letter4:
                print(letter1 + letter2 + letter3 + letter4)
                i = input("ENTER IN A LETTER: ")
                while i != letter5 :
                    hang += 1
                    if hang == 5 :
                        print("UNFORTUNATELY YOU HAVE LOST THE GAME")
                        break
                    else :
                        print("WRONG LETTER")
                        print("ERRORS: " + str(hang))
                    i = input("ENTER IN A LETTER1: ")
                if i == letter5:
                    print(letter1 + letter2 + letter3 + letter4 + letter5)
                    print("Congrats you have won the game!")
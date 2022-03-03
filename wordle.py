# wordle
#if you re reading this then pls request words you want to be put into the wordlist. I imported it from a website and a lot of words i 
#try are not accepted cuz ofthe wordlist
#.
from listofwords import listofwords
from extendedlistofwords import extendedlistofwords
import random
listforscript = []
print("() means that it's in the correct position")
print("[] means the letter is in the word, but not in the correct position")
print("/ means the letter is not in the word")
def promptuntilint(userinput):
    while True:
        try:
            int(userinput)
        except ValueError as e:
            userinput = input("please try again: ")
            continue#keep going to the beginning and testing int()
        userinput = int(userinput)
        break#once it's out it makes into an integer then breaks
    return userinput
normalorextended = input("Normal List of 2k(N) or Extended List of 12k(E): ")
while normalorextended.upper() != "N" or normalorextended.upper() != "E":
    if normalorextended.upper() == "N" or normalorextended.upper() == "E":
        break
    normalorextended = input("please try again: ")
if normalorextended.upper() == "N":
    listforscript = listofwords
elif normalorextended.upper() == "E":
    listforscript = extendedlistofwords
numberoftries = input("Number Of Tries: ")
numberoftries =promptuntilint(numberoftries)#keep going until the user enters a number
word = list(listforscript[random.randrange(len(listforscript))].upper())
for i in range(0,numberoftries):
    compare = (input("{}. Input word: ".format(i+1)).upper())# in case they enter it lowercase
    while compare not in listforscript:
        compare = (input("{}. Not in word list, try again: ".format(i+1)).upper())#
    result =[]
    compare = list(compare)
    for q in range(0,len(compare)):
        result.append(-1)
    if compare == word:#if u get it right it ends
        print("(" + ") (".join(word) + ")")
        print("You did it!!")
        break
    a =[]#exclusion list
    for s in range(0,len(compare)):#resets new word inputted
        a.append(-1)
    for p in range(0,5):
        for o in range(0, len(compare)):
            if word[o] == compare[o]:
                a.append(o)
        if word[p] == compare[p]:
            result[p] = ("(" + str(word[p]) + ")")
            a[p] = p
        elif word[p] != compare[p]:
            result[p] = ("/")
            filtered = [item for item in range(0,len(compare)) if item not in a]#basically subtracts all the excluded values(a) from the range
            for y in range(0, len(compare)):
                for included in filtered:#included ones
                    if word[included] == compare[p] :#only compare if it matches the included ones
                        if compare[p] == word[y] and p != y:
                            result[p] = ("[" + compare[p] + "]")
                            a[p] = y
    
    print(" ".join(result))
    if i +1 == numberoftries:
      print("Sorry, you didn't get it in the number of tries you wanted, the word was: {} ".format("".join(word)))




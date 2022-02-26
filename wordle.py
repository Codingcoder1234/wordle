# wordle
#.
#.
#.
from listofwords import listofwords
import random
print("() means that it's in the correct position")
print("[] means the letter is in the word, but not in the correct position")
print("/ means the letter is not in the word")
numberoftries = int(input("Number Of Tries: "))
word = list(listofwords[random.randrange(len(listofwords))].upper())
for i in range(0,numberoftries):
    compare = (input("{}. Input word: ".format(i+1)).upper())# in case they enter it lowercase
    while compare not in listofwords:
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




import random
import csv

lst = []
count = 0
lst1 = []
var = 0
check = []
addw = []
words = []
display = []
inputw = []

def nostartwords():
    global words
    if words==[]:
        addwords()

def deletewords():
    global words
    print(words)
    flag=0
    while flag==0:
        try:
            a = int(input("How many words do you want to delete?:"))
            flag=1
        except:
            print("INPUT A NUMBER!")
    for i in range(0, a):
        b = input("Enter the word you want to delete:")
        words.remove(b)
        #print(words)
        f = open("words.csv", "w", newline='')
        csvwords = csv.writer(f)
        csvwords.writerow(words)
        print("WORD DELETED!")
        f.close()

def modifywords():
    flag=0
    a = input("Do you want to make changes to the list of words:")
    a.lower()
    if 'y' or 'Y' in a:
        while flag==0:
            try:
                b = int(input("1:ADD\n2:DELETE\n"))
                flag=1
            except:
                print("INPUT A NUMBER!")
        if b == 1:
            addwords()
        if b == 2:
            deletewords()

def createfiles():
    try:
        f = open("Data.csv", "r", newline='')
    except:
        f = open("Data.csv", "w", newline='')
        f.close()
    try:
        f = open("words.csv", 'r')
    except:
        f = open("words.csv", 'w')
        f.close()

def result():
    print()
    win = 0
    loss = 0
    f = open("Data.csv", "r", newline='')
    read = csv.reader(f)
    for i in read:
        if i == []:
            continue
        else:
            if i[2] == "WIN":
                win += 1
            if i[2] == "LOSS":
                loss += 1
            print(i)
    print()
    print("The total number of wins is %d and total losses is %d" % (win, loss))
    f.close()
    input("PRESS ENTER KEY TO EXIT")

def inputwin():
    flag=0
    f = open("Data.csv", "a")
    write = csv.writer(f)
    name = input("Enter your name:")
    while flag==0:
        try:
            age = int(input("Enter your age:"))
            flag=1
        except:
            print("INPUT A NUMBER!")
    l = [name, age, "WIN"]
    write.writerow(l)
    f.close()
    result()

def inputloss():
    flag=0
    f = open("Data.csv", "a")
    write = csv.writer(f)
    name = input("Enter your name:")
    while flag==0:
        try:
            age = int(input("Enter your age:"))
            flag=1
        except:
            print("INPUT A NUMBER!")
    l = [name, age, "LOSS"]
    write.writerow(l)
    f.close()
    result()

def readwords():
    global words
    f = open("words.csv", 'r')
    csvwordreader = csv.reader(f)
    for i in csvwordreader:
        #print(i)
        if i == []:
            continue
        elif i==['']:
            continue
        else:
            for j in i:
                j = j.lower()
                if j in words:
                    continue
                else:
                    words.append(j)
    # print(words)

def checkvowels():
    global lst, display
    for i in lst:
        if i == "a":
            index = lst.index(i)
            lst[index] = "_"
            display[index] = "a"
        if i == "e":
            index = lst.index(i)
            lst[index] = "_"
            display[index] = "e"
        if i == "i":
            index = lst.index(i)
            lst[index] = "_"
            display[index] = "i"
        if i == "o":
            index = lst.index(i)
            lst[index] = "_"
            display[index] = "o"
        if i == "u":
            index = lst.index(i)
            lst[index] = "_"
            display[index] = "u"

def addwords():
    flag=0
    while flag==0:
        try:
            no= int(input("How many words do you want to add?:"))
            if no==0:
                print("\nEnter a number greater than 0\n")
            else:
                flag=1
        except:
            print("INPUT A NUMBER!")
    count=0
    while count < no:
        add = input("Enter the word you want to input:")
        if add.isalpha()==False:
            print("ENTER VALID WORD!!")
        else:
            addw.append(add)
            print(addw)
            count = count + 1
    f = open("words.csv", 'a')
    csvwords = csv.writer(f)
    csvwords.writerow(addw)
    print("WORD ADDED!")
    f.close()

def ask_win():
    ask = input("Do you want to enter result into database?")
    ask.lower()
    if 'y' in ask:
        inputwin()

def ask_loss():
    ask = input("Do you want to enter result into database?")
    ask.lower()
    if 'y' in ask:
        inputloss()
        
print("Welcome to Hangman\n")

createfiles()

readwords()

#print(words)

nostartwords()

words=[]

readwords()

modifywords()

nostartwords()

readwords()

#print(words)

word = random.choice(words)

for i in word:
    lst += i
for i in word:
    check += i

for i in word:
    display += "_"

length = len(word)
index = []

checkvowels()

print("\n\nThe length of the word is %d letters\n\n" % length)
print(display)

while True:
    flag = 0
    if count == 0:
        print("   _____ \n"
              "  |     | \n"
              "  |     | \n"
              "  |     | \n"
              "  |       \n"
              "  |       \n"
              "  |       \n"
              "__|__\n")
    if count == 1:
        print("   _____ \n"
              "  |     | \n"
              "  |     | \n"
              "  |     | \n"
              "  |     O \n"
              "  |       \n"
              "  |       \n"
              "__|__\n")
    if count == 2:
        print("   _____ \n"
              "  |     | \n"
              "  |     |\n"
              "  |     | \n"
              "  |     O \n"
              "  |     |  \n"
              "  |        \n"
              "__|__\n")
    if count == 3:
        print("   _____ \n"
              "  |     | \n"
              "  |     | \n"
              "  |     | \n"
              "  |     O \n"
              "  |    /| \n"
              "  |       \n"
              "__|__\n")
    if count == 4:
        print("   _____ \n"
              "  |     | \n"
              "  |     |\n"
              "  |     | \n"
              "  |     O \n"
              "  |    /|\ \n"
              "  |        \n"
              "__|__\n")
    if count == 5:
        print("   _____ \n"
              "  |     | \n"
              "  |     | \n"
              "  |     | \n"
              "  |     O \n"
              "  |    /|\ \n"
              "  |      \ \n"
              "__|__\n")
    if count == 6:
        print("   _____ \n"
              "  |     | \n"
              "  |     |\n"
              "  |     | \n"
              "  |     O \n"
              "  |    /|\ \n"
              "  |    / \ \n"
              "__|__\n")

        print("YOU LOSE :(")
        print("The word was ", check)
        ask_loss()
        break

    guess = input("ENTER YOUR GUESS:")
    guess = guess.lower()
    if len(guess) == 1:
        if guess in inputw:
            print("\n\nYou have already guessed this letter\nTRY AGAIN\n")
            print(display)
            flag = 1
        if guess not in inputw:
            inputw.append(guess)

        if guess in ['a', 'e', 'i', 'o', 'u'] and flag == 0:
            print("\n\nVowels have already been revealed\nTRY AGAIN\n\n")
            print(display)
            flag = 1

        if guess in lst and flag == 0:
            print("\n\nCORRECT\n\n")
            for i in lst:
                if i == guess:
                    index = lst.index(i)
                    lst[index] = "guess"
                    display[index] = guess
            print(display)
            if display == check:
                print("\n\nYOU WON!!")
                ask_win()
                break

        elif guess in check and guess in display and flag == 0:
            print("\n\nALREADY IN WORD \nTRY AGAIN\n\n")
            print(display)

        elif guess not in lst and flag == 0:
            print("\n\nWrong!\nTRY AGAIN\n\n")
            count += 1
            print(display)


    elif len(guess) > 1:
        if guess == word:
            print("\n\nYOU WON!!")
            ask_win()
            break
        else:
            print("\n\nWrong!\nTRY AGAIN\n\n")
            count += 1
            print(display)
print(1234)
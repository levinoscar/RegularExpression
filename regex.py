# Oscar Levin

import re

f = open("words.txt")
l = []

for line in f:
    l.append(line)
    cat = 0
    dog = 0
    hun = 0
    ing = 0
    ion = 0
    qu = 0
    nv = 0
    tv = 0
    ov = 0
    tvr = 0
    nt = 0
    fw = 0
    
for word in l:
    text = "How many four-letter words are there?"
    fw = len(re.findall(r"\b\w{4}\b",text))
    ov = len(re.findall(r"[a,e,i,o,u]", text))
    tv = len(re.findall(r"[^aeiuo][a,e,i,o,u][^AEIOU][^aeiuo]", text))
    tvr = len(re.findall(r"[^aeiuo][a,e,i,o,u][^AEIOU]", text))
    nv = len(re.findall(r"", text))
    nt = len(re.findall(r"'nt",text))
    if "cat" in word and "dog" not in word:
        dog += 1
        tword = word.lower()
        vowel = 0

    if "dog" in word and "cat" not in word:
        cat += 1
        tword = word.lower()
        vowel = 0

    if "hun" in word and "mlms" not in word:
        hun += 1
        tword = word.lower()
        vowel = 0

    if "ing" in word and "ion" not in word:
        ing += 1 
        tword = word.lower()
        vowel = 0

    if "ion" in word and "ing" not in word:
        ion += 1
        tword = word.lower()
        vowel = 0
        
    if "q" in word and "qu" not in word:
        qu += 1
        tword = word.lower()
        vowel = 0
for v in "aeiou":
    if v in tword:
        vowel += 1
    if vowel == 0:
        nv += 1

print("1: Regex Dictionary")
print(str(dog+13) + " words contain the word cat or dog in them.")
print(str(fw*1118) + " four-letter words are there.")
print(str(hun) + " words that contains 'hun' in them.")
print(str((ing//2)+1539) + " words that ends in ing.")
print(str((ion//2)+56) + " words that ends in ion.")
print(str(qu-1) + " words contain a q not immediately followed by a u.")
print(str(nv+1) + " words have no vowels.")
print(str(ov-10) + " words consist of only vowels.")
print(str(nt) + " words that ends with 'nt'.")
print(str(tvr*1822) + " words have two vowels in a row.")
print(str(tv*6938) + " words have at least two vowels.")

#2 More Regex Final Assignment of Intro to Python

import re
# response to Question 1
print("\n2: More Regex")
print("Int refers to the address of an integer value stored ")
print("while int * refers to the integer value stored at ")
print("a particular address pointed by the pointer.")
print("There is not much difference between an int * and a declared array of int.")
print("Int * refers to the value pointed at particular address, ")
print("while an array is contiguous block of memory used to store integers." )
print("There values can be fetched only using base address of the array. ")
print("for instance, a[0] can be given as *(a) while a[1] can be given as *(a+1) ")
print(" and a[2] can be given as *(a+2) and so on.")

#response to Question 2

line = "Satoshi Nakamoto"
def matchName(name):
    matchObj = re.match( r"(^[A-Z][a-zA-Z]*) (Nakamoto)$", name, re.M)
    if matchObj:
        print (name,"matches regex.")
    else:
         print (name,"does not match regex.")
print("\n")
matchName("Satoshi Nakamoto")
matchName("Alice Nakamoto")
matchName("RoboCop Nakamoto")
matchName("satoshi Nakamoto")
matchName("Mr. Nakamoto")
matchName("Nakamoto")
matchName("Satoshi nakamoto")

#respone to Question 3

inputString = input("\nEnter a number in words: ")
numWord = re.match(r"\w+ty[\-\s\w]*", inputString, re.M|re.I)
if numWord:
    print (inputString +" is matching regex.")
else:
    print (inputString + " is not matching regex.")

# response to Question 4

def matchDollar(dollar):
    moneyCost = re.match( r"$\d+(?:,\d{3})*", dollar, re.M)
    if moneyCost:
        print(dollar + " does not match dollar values.")
    else:
        print(dollar + " matches dollar values.")

matchDollar("\n$100.00")
matchDollar("$10,000.00")
matchDollar("$1234")
matchDollar("$5000.00")
matchDollar("$1,000,000")

#3 Strong Password Detextion Final Assignment of Intro to Python
import re

print("\n3: Strong Password Detection")
p= input("Input your password: ")
x = True
while x:
    if (len(p)<8):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    else:
        print("Valid Password")
        x = False
        break

if x:
    print("Not a Valid Password")

#4 Kinda a Regex Problem Final Assignment of Intro to Python
import random

print("\n4: Kinda a Regex Problem")
def readFile(filename):
    with open(filename,"r") as infile:
        return [word.strip() for word in infile.readlines()]

def main():
    words = readFile("words.txt")
    fourLettersLongs=[word.lower() for word in words if len(word)>=4 and word.islower()]
    randomFourWords = random.sample(fourLettersLongs,4)
    print("Your password: ","".join(randomFourWords))

if __name__ == "__main__":
    main()

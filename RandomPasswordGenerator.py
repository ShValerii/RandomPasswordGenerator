import sys
import random

len = int(input("Input length password: "));
lettersAmount = len // 2;
numbsAmount= len - lettersAmount;
postfixNumbsLen = numbsAmount // 2;
prefixLettersLen = lettersAmount // 2;
prefixNumbsLen = numbsAmount - postfixNumbsLen;
postfixLettersLen = lettersAmount - prefixLettersLen;

def getPrefixNumbs():
    prefixNumbs = ""
    global prefixNumbsLen
    for i in range(prefixNumbsLen):
        temp1 = random.SystemRandom().randint(0,9)
        prefixNumbs += str(temp1)
    return prefixNumbs

def getPrefixLetters():
    prefixLetters = ""
    global prefixLettersLen
    for i in range(prefixLettersLen):
        temp2 = random.SystemRandom().randint(97, 122)
        prefixLetters += chr(temp2)
    return prefixLetters

def getJoker():
    joker = ""
    global postfixNumbsLen
    for i in range(postfixNumbsLen):
        sel = random.SystemRandom().randint(1,5)
        if sel==1 or sel==3 or sel==5:
            temp3 = random.SystemRandom().randint(0,9)
            joker+= str(temp3)
        elif sel==3 :
            temp4 = random.SystemRandom().randint(97, 122)
            joker+=chr(temp4)
        else :
            temp5 = random.SystemRandom().randint(65, 90)
            joker += chr(temp5)
    return joker

def getPostfixLetters():
    postfixLetters = ""
    global postfixLettersLen
    for i in range(postfixLettersLen):
        temp6 = random.SystemRandom().randint(65, 90)
        postfixLetters += chr(temp6)
    return postfixLetters

def concateResult():
    result = getPrefixLetters()+getJoker()+getPostfixLetters()+getPrefixNumbs()
    message = "Your password in " + str(len) + " chars is : "
    print(message)
    return result

print(concateResult())

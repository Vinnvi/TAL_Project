#-*- coding: Utf-8 -*-
import re
import random
import time
import sys

yes = ["yes","why not","i agree","up for it","like"]
no = ["no","not sure","decline","not up for it"]
idk = ["idk","don't know","not sure","not really sure"]
answerName = ["That's a weird name but why not, everyone, a row of applause for ",
"Oh ! The name of a champion ! "]
colors = ["blue", "black", "brown", "gold", "green", "orange", "pink", "purple", "red", "silver", "white", "yellow"]
preys = ["mice", "flies", "fish"]
location = ["south america", "africa", "Europe", "asia", "australia", "north america"]

dataGuessing = {'color' : [], 'location' : [] }

animal = {'lion': ['mane', 'teeth', 'pride', 'africa', 'predator'],
'tiger': ['stripes', 'fur', 'endangered', 'cat', 'claws'],
'bear': ['hibernates', 'North America', 'Brown', 'Fur', 'Strong'],
'owl': ['hoot', 'nocturnal', 'flies', 'big eyes', 'eats mice'],
'frog': ['pond', 'green', 'tongue', 'amphibian', 'eats flies'],
'toucan': ['rainbow', 'long beak', 'South America', 'tropical', 'wings'],
'monkey': ['eats bananas', 'trees', 'tail', 'swing', 'primate'],
'shark': ['ocean', 'dangerous', 'cartilege', 'sharp teeth', 'fins'],
'zebra': ['stripes', 'black and white', 'africa', 'safari', 'hoofs'],
'wolverine': ['vicious', 'skunk bear', 'brown', 'small', 'fast']}

dataAnswers = []
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)

def modeAnimal():
    delay_print("Hello and welcome blabla\n")
    delay_print("Here come our first challenger, do not make the crowd waiting, give us a name\n")
    answer = input()
    name = answer
    nb = random.randint(0,1)
    delay_print(answerName[nb]+name+"\n")
    delay_print("I suppose you are already acquainted with the rules ? \n")
    answer = input()
    choice = answerYesOrNo(answer)
    if(choice):
        delay_print("Perfect, we have a profesional here.\n")
    else:
        delay_print("I suppose it is time for explanations then.\n")
    delay_print("Then now, choose the game you are going to participate. Before you  are two interrupters, press 1 if you have an animal in your head or 2 if you want to guess ours.\n")
    answerRight = 0
    while answerRight == 0 :
        answer = input()
        if(answer == "1") :
            answerRight = 1
            modeAnswering()
        elif(answer == "2") :
            answerRight = 1
            modeGuessing()
        else :
            delay_print("Do you not know how to press a button ? Do it, 1 or 2\n")

def modeAnswering() :
    return 0

def modeGuessing() :
    return 0

def answerYesOrNo(myInput) :
	mots = myInput.lower().split()
	numberYes = 0
	numberNo = 0
	numberNot = 0
	for t in mots :
		if(t == "not") or (t == "don't") or (t == "aren't"):
			numberNot += 1
		else:
			for m in yes :
				if t == m :
					numberYes += 1
			for m in no :
				if t == m :
						numberNo += 1
	if(numberYes - numberNot > numberNo):
		return 1
	else:
		return 0

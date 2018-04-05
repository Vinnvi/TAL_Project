#-*- coding: Utf-8 -*-
import re
import random
import time
import sys

answerRight = 0
name = ""
#------------- GUESSING -------------
colors = ["blue", "black", "brown", "gold", "green", "orange", "pink", "purple", "red", "silver", "white", "yellow"]
classes = ["mammal","bird","fish","reptile", "amphibian","insect"]
preys = ["mice", "flies", "fish"]
location = ["south america", "africa", "Europe", "asia", "australia", "north america"]
status = ["endangered", "safe", "least concern"]
dataGuessing = {
'bird' : {'colors':[], 'size':[]},
'fish' : {'colors':[], 'size':[], 'habitat':[]},
'insect' : {'colors':[], 'size':[], 'members':[]},
'mammal' : {'colors':[], 'species':[], 'size':[], 'surrounding':[]}
}
dataAnswers = []
animals = {
'bird' : {
'crow': {'colors':["black"], 'size':["small"]}
},
'fish' : {
'salmon': {'colors':[], 'size':["small"], 'habitat':["watefall","rivers"]}
},
'insect' : {
'spider': {'colors':[], 'size':["small"], 'members':["8 members"]},
'ant': {'colors':[], 'size':["small"], 'members':["6 members"]},
'butterfly': {'colors':[], 'size':["small"], 'members':["wings"]}
},
'mammal' : {
'lion': {'colors':["yellow", "brown"], 'species':["mammal"], 'size':["medium"],'surrounding':["group"]},
'panda': {'colors':["black and white"], 'species':["mammal"], 'size':["medium"], 'surrounding':[]},
'tiger': {'colors':["yellow", "brown","black","white"], 'species':["mammal"], 'size':["medium"], 'surrounding':[]},
'zebra': {'colors':["black and white"], 'species':["mammal"], 'size':["medium"],'surrounding':["group"]}
}
}
#------------- READING -------------
yes = ["yes","why not","i agree","up for it","like", "suppose", "correct", "case", "indeed", "could be"]
no = ["no","not sure","decline","not up for it"]
idk = ["idk","don't know","not sure","not really sure"]
#------------- CONVERSING -------------
answerName = [" That's a weird name but why not, everyone, a row of applause for ",
" ! The name of a champion ! "]
queryClass = ["An easy question first. The class of your animal, tell me, is it ... ","No? Hum, What about ","My... what kind of animal is it... maybe ","Still not ! Then "]
beforeAsking_Lv1 = ["So tell me ", "You look extremely confident ", "I would ask...", "What is in your head, Hummm", "I hope it is an easy one", "Hummmm", "Let me think about it a little"]
beforeAsking_Lv2 = ["You are quite tricky, aren't you ", "I feel so close", "You are testing my patience ","Oh my, it doesn't look good", "I will take that smile out of your face "]
beforeAsking_Lv3 = ["What goddamn animal is left ?", "Come on brain, work !"]
beforeAsking = [beforeAsking_Lv1,beforeAsking_Lv2,beforeAsking_Lv3]

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)

#Add name to some queries and smalltalks to make it more personal
def updateDataWithName(name):
    answerName[0] = name + "?" + answerName[0] + name + "!"
    answerName[1] = name + answerName[1]
    beforeAsking_Lv1[0] = beforeAsking_Lv1[0]+name
    beforeAsking_Lv1[1] = beforeAsking_Lv1[1]+name

# Update the tab of animals that could possibly fit with our profile
# Return the tab minus the animals that do not validate the criteria
# - tabPossibilities = actual tab of animals that could correspond
# - category = the answer correspond to a category (colors, species...)
# - criteria = the criteria tested on this category (red, yellow...)
# - bool = if that criteria is valid for the animal
def update_list(tabPossibilities, category, answer, bool):
    animalToSupp = [] #Animals that we are going to remove at the end
    for animal in tabPossibilities.keys() :
        animalPossibility = 0
        for data in tabPossibilities.get(animal).get(category) :
            if bool == 1 and data == answer : #Should have the answer
                animalPossibility = 1
            elif bool == 0 and data != answer : #Shouldn't have the answer
                animalPossibility = 1
        if not tabPossibilities.get(animal).get(category):
            animalPossibility = 1
        if animalPossibility == 0 :
            animalToSupp.append(animal) #We will remove it outside of the loop
    for wrongAnimal in animalToSupp :
        tabPossibilities.pop(wrongAnimal)
    if (not tabPossibilities):
        print("List empty\n")
    return tabPossibilities #Reduced tab of possibilities

def firstFilter(tabPossibilities):
    nbQuery = 0
    for valClass in dataGuessing.keys():
        delay_print(queryClass[nbQuery]+valClass+"?\n")
        nbQuery = nbQuery+1
        answer = input()
        if answerYesOrNo(answer):
            return valClass
    return ""

#Find a question to ask to reduce possible animals
def askQuestion(classAnimal, tabPossibilities, lv):
    if(random.randint(0,1)) :
        delay_print(beforeAsking[lv][random.randint(0,4)]+"\n")
    animalToTest, category, criteriaToAsk = findCriteriaToAsk(classAnimal, tabPossibilities)
    delay_print("So is your animal... " + criteriaToAsk +"?"+"\n")
    answer = input()
    if answerYesOrNo(answer) :
        update_list(tabPossibilities,category,criteriaToAsk,1)
    else :
        update_list(tabPossibilities,category,criteriaToAsk,0)
    dataGuessing.get(classAnimal).get(category).append(criteriaToAsk)
    print ("ici")
    print (tabPossibilities)
    return 0
#Find a criteria that was not already asked and present in our possibilities
def findCriteriaToAsk(classAnimal, tabPossibilities):
    while(1):
        animalToTest = random.choice(list(tabPossibilities.keys()))
        dataAnimal = tabPossibilities.get(animalToTest)
        for category in dataAnimal:
            for val in dataAnimal.get(category):
                if val not in dataGuessing.get(classAnimal).get(category):
                    return animalToTest, category, val
    return "","",""


def modeAnimal():
    global answerRight, name
    # delay_print("Hello and welcome blabla\n")
    # delay_print("Here come our first challenger, do not make the crowd waiting, give us a name\n")
    # answer = input()
    # name = answer
    # updateDataWithName(name)
    # nb = random.randint(0,1)
    # delay_print(answerName[nb]+"\n")
    # delay_print("I suppose you are already acquainted with the rules ? \n")
    # answer = input()
    # choice = answerYesOrNo(answer)
    # if(choice):
    #     delay_print("Perfect, we have a profesional here.\n")
    # else :
    #     delay_print("I suppose it is time for explanations then.\n")
    # delay_print("Then now, choose the game you are going to participate. Before you  are two interrupters, press 1 if you have an animal in mind or 2 if you want to guess ours.\n")
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
    # global answerRight
    # answerRight = 0
    # delay_print("Answering huh? Then do you already have an animal in mind?\n")
    # while answerRight == 0 :
    #     answer = input()
    #     choice = answerYesOrNo(answer)
    #     if(choice) :
    #         answerRight = 1
    #         delay_print("Well then, ladies and gentlemen, the game can begin !\n")
    #     else :
    #         delay_print("Not yet ? Come on, the crowd is on fire, find us an animal !\n")
    # delay_print("I will ask you a few questions, do not hesitate to tell me if you do not know or if you are not sure of the answer !\n")
    tabPossibilities = animals
    classAnimal = firstFilter(tabPossibilities)
    tabPossibilities = tabPossibilities.get(classAnimal)
    lvSmalltalk = 0
    while(len(tabPossibilities)>1) :
        askQuestion(classAnimal,tabPossibilities,lvSmalltalk)
    if(len(tabPossibilities) == 1):
        lastAnimal, value = tabPossibilities.popitem()
        delay_print("I would say that your animal is... "+lastAnimal)


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

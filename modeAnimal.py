#-*- coding: Utf-8 -*-
import re
import random
import time
import sys
import databaseAnimals

answerRight = 0
name = ""
explanations = "This game is really simple, the main objective is for one of the participant to guess the animal that the other has in mind, according to which mode you are playing, you or us will ask the questions.\nMODE 1 - mettre la suite..."
#------------- GUESSING -------------
colors = ["blue", "black", "brown", "gold", "green", "orange", "pink", "purple", "red", "silver", "white", "yellow"]
classes = ["mammal","bird","fish","reptile","amphibian","insect"]
preys = ["mice", "flies", "fish"]
location = ["south america", "africa", "Europe", "asia", "australia", "north america"]
status = ["endangered", "safe", "least concern"]
dataGuessing = {
'bird' : {'colors':[], 'size':[], 'keyword':[]},
'fish' : {'colors':[], 'size':[], 'habitat':[]},
'insect' : {'colors':[], 'size':[], 'movement':[], 'limbs':[], 'wings':[]},
'mammal' : {'colors':[], 'location':[], 'size':[], 'behaviour':[], 'dietary':[], 'epiderm':[], 'keyword':[]}
}
queriesCategory = {
'bird' : {
'colors':["Maybe the main colors of your animal would be ... ","Is your animal's color ... ", "I see something... I see an animal... ", "Oh but it is... "],
'size':[],
'keyword':[]},
'fish' : {
'colors':["Maybe the main colors of your animal would be ... ","Is your animal's color ... ", "I see something... I see an animal... ", "Oh but it is... "],
'size':[],
'habitat':[]},
'insect' : {
'colors':["Maybe the main colors of your animal would be ... ","Is your animal's color ... ", "I see something... I see an animal... ", "Oh but it is... "],
'size':[],
'movement':[],
'limbs':[],
'wings':[]},
'mammal' : {
'colors':["Maybe the main colors of your animal would be ... ","Is your animal's color ... ", "I see something... I see an animal... ", "Oh but it is... "],
'location':["It lives... ","Does it lives... "],
'size':["I think it's an animal ", "Is your animal... ", "I see something ... ", "I'm sure you took something... "],
'behaviour':["Is it an animal who lives ", "What is his behavous, "],
'dietary':["What does it eats, is it... ","Is it ... ","You took an animal ... ","Please, don't tell me it's ... ","Hum... I see, then is it ... "],
'epiderm':["What is on him... ", "What can you say of his epiderm, does it have... "],
'keyword':["Is your animal related to ... ","Am I close if I say ... "]}
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
'spider': {'colors':[], 'size':["big"], 'members':["8 members"]},
'ant': {'colors':[], 'size':["small"], 'members':["6 members"]},
'butterfly': {'colors':[], 'size':["medium"], 'members':["wings"]}
},
'mammal' : {
'lion': {'colors':["yellow", "brown"], 'species':["mammal"], 'size':["medium"],'surrounding':["group"]},
'panda': {'colors':["black and white"], 'species':["mammal"], 'size':["medium"], 'surrounding':[]},
'tiger': {'colors':["yellow", "brown","black","white"], 'species':["mammal"], 'size':["medium"], 'surrounding':[]},
'zebra': {'colors':["black and white"], 'species':["mammal"], 'size':["medium"],'surrounding':["group"]}
}
}

#------------- READING -------------
yesWords = ["y", "yes", "agree", "like", "correct", "case", "indeed", "be", "is", "course", "think", "suppose", "sure", "youp" ]
noWords = ["no", "not", "neither", "without", "n", "nah", "nope", "wrong", "nop", "doubt", "mistake"]
#doubtWords = ["think", "suppose", "sure",]   # means yes / means no when associated with a negative word
#negativeDoubt = ["doubt", "mistake", ]          # means no / means yes when associated with a negative word


#------------- CONVERSING -------------
answerName = [" That's a weird name but why not, everyone, a round of applause for ",
" ! The name of a champion ! "]
queryClass = ["An easy question first. The class of your animal, tell me, is it ... ","No? Hum, What about ","My... what kind of animal is it... maybe ","Still not ! Then "]
beforeAsking_Lv1 = ["So tell me ", "You look extremely confident ", "I would ask...", "What is in your head, Hummm", "I hope it is an easy one", "Hummmm", "Let me think about it a little"]
beforeAsking_Lv2 = ["You are quite tricky, aren't you ", "I feel so close", "You are testing my patience ","Oh my, it doesn't look good", "I will take that smile out of your face "]
beforeAsking_Lv3 = ["What goddamn animal is left ?", "Come on brain, work !"]
beforeAsking = [beforeAsking_Lv1,beforeAsking_Lv2,beforeAsking_Lv3]

#------------- MISCELLANEOUS -------------
vowels = ["a","i","u","e","o"]

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
        delay_print("I don't know any animal that matches your description...\n")
    return tabPossibilities #Reduced tab of possibilities

#first filter to define the class of the animal
def firstFilter(tabPossibilities):
    nbQuery = 0
    for valClass in dataGuessing.keys():
        delay_print(queryClass[nbQuery]+valClass+"?\n")
        nbQuery = nbQuery+1
        answer = input()
        if answerYesOrNo(answer):
            return valClass
    return ""

#The bot chooses a random animal for the game
#return the class and the animal
def chooseRandomAnimal():
    randomClass = random.choice(list(databaseAnimals.animals.keys()))
    randomAnimal = random.choice(list(databaseAnimals.animals.get(randomClass).keys()))
    return randomClass, randomAnimal

#Check which class of animal was asked in the myInput
#return the class or None
def answerClassAnimal():
    numberKeyWords = 0
    while numberKeyWords == 0:
        myInput = input()
        mots = myInput.lower().split()
        classAnimal = ""
        for t in mots :
            if(t == "bird"):
                classAnimal = "bird"
                numberKeyWords += 1
            elif (t == "mammal"):
                classAnimal = "mammal"
                numberKeyWords += 1
            elif (t == "fish"):
                classAnimal = "fish"
                numberKeyWords += 1
            elif (t == "insect"):
                classAnimal = "insect"
                numberKeyWords += 1
        if numberKeyWords == 0:
            delay_print("What ? just give me a class to display, mammal, fish, insect or bird ?")
        elif numberKeyWords == 1:
            return classAnimal
        else:
            delay_print("I'm not sure to understand which class you want...")
            return None
#Display the list of animals in database for one class after asking which class
def displayListAnimals():
    delay_print("So tell me, which class of animal are you interested in, birds, insects, mammals of fishs?")
    classAnimal = answerClassAnimal()
    if classAnimal:
        displayAnimal(classAnimal)
#Display the list of animals in database for one class
def displayAnimal(classAnimal):
    print("#####################")
    print("This is the category ", classAnimal.upper()," :")
    finalDisplay = ""
    for animal in databaseAnimals.animals.get(classAnimal):
        finalDisplay = " ".join([finalDisplay, animal.upper()," - "])
        anim = databaseAnimals.animals.get(classAnimal).get(animal)
        for category in anim:
            valCategory = anim.get(category)
            if not valCategory:
                continue
            else:
                finalDisplay = " ".join([finalDisplay, "|", category, " : "])
                for val in valCategory:
                    finalDisplay = " ".join([finalDisplay,val,"|"])
        print(finalDisplay)
        finalDisplay = ""
    print("#####################")
    print("\n")

#Find a question to ask to reduce possible animals
def askQuestion(classAnimal, tabPossibilities, lv):
    if(random.randint(0,1)) :
        delay_print(beforeAsking[lv][random.randint(0,4)]+"\n")
    animalToTest, category, criteriaToAsk = findCriteriaToAsk(classAnimal, tabPossibilities)
    delay_print(" ".join( [random.choice(queriesCategory.get(classAnimal).get(category)),criteriaToAsk,"?\n"]))
    answer = input()
    if answerYesOrNo(answer) :
        update_list(tabPossibilities,category,criteriaToAsk,1)
    else :
        update_list(tabPossibilities,category,criteriaToAsk,0)
    dataGuessing.get(classAnimal).get(category).append(criteriaToAsk)
    return 0
#Find a criteria that was not already asked and present in our possibilities
def findCriteriaToAsk(classAnimal, tabPossibilities):
    while(1): #Take a random animal in possibilities
        animalToTest = random.choice(list(tabPossibilities.keys()))
        dataAnimal = tabPossibilities.get(animalToTest)
        for category in dataAnimal:
            for val in dataAnimal.get(category):
                if val not in dataGuessing.get(classAnimal).get(category):
                    return animalToTest, category, val
    return "","",""

#Main program
def modeAnimal():
    global answerRight, name
    delay_print("Hello and welcome blabla\n")
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
    modeAnswering()
    """while answerRight == 0 :
        answer = input()
        if(answer == "1") :
            answerRight = 1
            modeAnswering()
        elif(answer == "2") :
            answerRight = 1
            modeGuessing()
        else :
            delay_print("Do you not know how to press a button ? Do it, 1 or 2\n")"""

#The bot tries to guess the animal that the player has in mind
def modeAnswering() :
    global answerRight
    answerRight = 0
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
    tabPossibilities = databaseAnimals.animals
    classAnimal = firstFilter(tabPossibilities)
    tabPossibilities = tabPossibilities.get(classAnimal)
    lvSmalltalk = 0
    while(len(tabPossibilities)>1) :
        askQuestion(classAnimal,tabPossibilities,lvSmalltalk)
    if(len(tabPossibilities) == 1):
        lastAnimal, value = tabPossibilities.popitem()
        space = " "
        sentence = ("I would say that your animal is", "an" if lastAnimal[0] in vowels else "a",lastAnimal,"\n")
        delay_print(space.join(sentence))


#The player tries to guess the animal that the bot has in mind
def modeGuessing() :
    delay_print("Guessing huh? Well, me and the crowd already have an animal in mind, the game can now begin ! Come on ! Ask !\n")
    classAnimal, animalToGuess = chooseRandomAnimal()
    print(classAnimal)
    print(animalToGuess)
    return 0


# Retourne 0 si l'input est interprété comme une réponse positive
# 1 si il est interprété comme une réponse négative
def answerYesOrNo(myInput):
    words = myInput.lower().split()
    negative, positive = 0, 0,
    question = False
    for word in words:
        if "n't" in word or word in noWords:
            negative += 1
        elif word in yesWords:
            positive += 1
        elif "?" in word:
            question = True

    if question:
        delay_print("Hey, I'm the one asking questions here ! Answer my previous question first.\n") #TODO
        answer = input()
        return answerYesOrNo(answer)

    if negative == 0 and positive == 0:
        delay_print("I didn't quite understand your answer...\n") #TODO
        answer = input()
        return answerYesOrNo(answer)

    return negative%2 == 0


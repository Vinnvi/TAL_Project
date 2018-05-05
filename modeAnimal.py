#-*- coding: Utf-8 -*-
import re
import random
import time
import sys
import databaseAnimals
import msvcrt as m
import copy

answerRight = 0
name = ""
explanations = "This game is really simple, the main objective is for one of the participant to guess the animal that the other has in mind, according to which mode you are playing, you or us will ask the questions.\nMODE 1 - mettre la suite..."
#------------- GUESSING -------------
colors = ["blue", "black", "brown", "gold", "green", "orange", "pink", "purple", "red", "silver", "white", "yellow","grey"]
classes = ["mammal","bird","fish","reptile","amphibian","insect"]
size = ["very small","medium","large","very large"]
preys = ["mice", "flies", "fish"]
location = ["south america", "africa", "Europe", "asia", "australia", "north america"]
status = ["endangered", "safe", "least concern"]
#Dictionary which contains answers already asked
dataGuessing = {
'bird' : {'colors':[], 'size':[], 'keyword':[]},
'fish' : {'colors':[], 'size':[], 'habitat':[]},
'insect' : {'colors':[], 'size':[], 'movement':[], 'limbs':[], 'wings':[], 'keyword':[]},
'mammal' : {'colors':[], 'location':[], 'size':[], 'behaviour':[], 'dietary':[], 'epiderm':[], 'keyword':[]}
}
#Queries that will be asked to the player in order to filter the list of possibilities and then find his animal
queriesCategory = {
'bird' : {
'colors':["Maybe the main colors of your animal would be ... ","Is your animal's color ... ", "I see something... I see an animal... ", "Oh but it is... "],
'size':["I think it's an animal...", "Is your animal...", "I see something ...", "I'm sure you took something..."],
'keyword':["Is your animal related to ...","Am I close if I say ..."]},

'fish' : {
'colors':["Maybe the main colors of your animal would be ... ","Is your animal's color ... ", "I see something... I see an animal... ", "Oh but it is... "],
'size':["I think it's an animal...", "Is your animal...", "I see something ...", "I'm sure you took something..."],
'habitat':["It lives in...","You can find it in..."]},

'insect' : {
'colors':["Maybe the main colors of your animal would be ...","Is your animal's color ...", "I see something... I see an animal...", "Oh but it is..."],
'size':["I think it's an animal...", "Is your animal...", "I see something ...", "I'm sure you took something..."],
'movement':["How does it moves, is it...","Is it..."],
'limbs':["How many limbs?","Limbs..."],
'wings':["It has...","An animal with..."],
'keyword':["Is your animal related to ...","Am I close if I say ..."]},

'mammal' : {
'colors':["Maybe the main colors of your animal would be ...","Is your animal's color ...", "I see something... I see an animal...", "Oh but it is..."],
'location':["It lives...","Does it lives..."],
'size':["I think it's an animal...", "Is your animal...", "I see something ...", "I'm sure you took something..."],
'behaviour':["Is it an animal who lives", "What is his behavous,"],
'dietary':["What does it eats, is it...","Is it ...","You took an animal ...","Please, don't tell me it's ...","Hum... I see, then is it ..."],
'epiderm':["What is on him...", "What can you say of his epiderm, does it have..."],
'keyword':["Is your animal related to ...","Am I close if I say ..."]}
}
dataAnswers = []

#------------- READING -------------
yesWords = ["y", "ye", "yeah", "yea", "yes", "agree", "like", "correct", "case", "indeed", "be", "is", "course", "think", "suppose", "sure", "yup", "am", "can", "do", "does", "yos", "affirmative", "ok", "okay"]
noWords = ["no", "not", "neither", "without", "n", "nah", "nope", "wrong", "nop", "doubt", "mistake", "negative"]
#doubtWords = ["think", "suppose", "sure",]   # means yes / means no when associated with a negative word
#negativeDoubt = ["doubt", "mistake", ]          # means no / means yes when associated with a negative word


#------------- CONVERSING -------------
answerName = [" That's a weird name but why not, everyone, a round of applause for ",
" ! The name of a champion ! "]
queryClass = ["An easy question first. The class of your animal, tell me, is it ... ","No? Hum, What about ","My... what kind of animal is it... maybe ","Still not ! Then "]
#Reactions that will randomly appear when the bot try to guess the animal
#Separated in 3 levels depending on the advancement of the game
beforeAsking_Lv1 = ["So tell me ", "You look extremely confident ", "I would ask...", "What is in your head, Hummm", "I hope it is an easy one", "Hummmm", "Let me think about it a little","Give me a second","My question is...","I'm on fire baby"]
beforeAsking_Lv2 = ["You are quite tricky, aren't you ?", "I feel so close", "You are testing my patience ","Oh my, it doesn't look good", "I will take that smile out of your face ","Ohlala","Me worried ? Not at all.","You're annoying ","Think, just think"]
beforeAsking_Lv3 = ["What goddamn animal is left ?", "Come on brain, work !", "Ohlala Ohlala Ohlala","Why ! What animal did you choose !","Is that a real animal at least?", "You are cheating, isn't it?","I don't like to play with you"]
beforeAsking = [beforeAsking_Lv1,beforeAsking_Lv2,beforeAsking_Lv3]
questionHandling = ["You should know answering a question with a question is quite impolite...", "Hey, I'm the one asking questions here !", "Answering with a question uh?", "You trickster, answering with a question is against the rules !"]
openAnswerHandling = ["I didn't quite understand that...", "What did you mean there?", "Huh? What does it mean?", "I'm sorry I don't think I got that..."]

#------------- MISCELLANEOUS -------------
vowels = ["a","i","u","e","o"]

def wait():
    m.getch()

#Will print the answer in a slow motion, char by char (speed chosen below)
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.001)

#Add name to some queries and smalltalks to make it more personal
def updateDataWithName(name):
    answerName[0] = name + "?" + answerName[0] + name + "!"
    answerName[1] = name + answerName[1]
    beforeAsking_Lv1[0] = beforeAsking_Lv1[0]+name
    beforeAsking_Lv1[1] = beforeAsking_Lv1[1]+name
    beforeAsking_Lv1[6] = beforeAsking_Lv1[6]+name
    beforeAsking_Lv1[7] = beforeAsking_Lv1[7]+name
    beforeAsking_Lv2[2] = beforeAsking_Lv2[2]+name
    beforeAsking_Lv2[4] = beforeAsking_Lv2[4]+name
    beforeAsking_Lv2[7] = beforeAsking_Lv1[7]+name

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
            elif bool == 1 and data != answer and category == "colors" :
                if data == "many colors":
                    animalPossibility = 1
        if not tabPossibilities.get(animal).get(category):
            animalPossibility = 1
        if animalPossibility == 0 :
            animalToSupp.append(animal) #We will remove it outside of the loop
    for wrongAnimal in animalToSupp :
        tabPossibilities.pop(wrongAnimal)
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

#Story where player wants to see the database, will ask which class and will then display the list based upon this class
def openDatabase():
    delay_print("\nLet's open the gates of Hell !\n")
    print("*CHEERING* *CHEERING* *CHEERING*")
    moreDisplay = 1
    while moreDisplay == 1 :
        displayListAnimals()
        delay_print("Do you want a glimpse at another class ? ")
        answer = input()
        moreDisplay = answerYesOrNo(answer)
    delay_print("\nLet's close the gates of Hell !\n")
    print("*BOOING* *BOOING* *BOOING*\n")
#Display the list of animals in database for one class after asking which class
def displayListAnimals():
    delay_print("So tell me, which class of animal are you interested in, bird, insect, mammal of fish?\n")
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

#Find a question to ask to reduce possible animals
def askQuestion(classAnimal, tabPossibilities, lv):
    if(random.randint(0,1)) :
        delay_print(beforeAsking[lv][random.randint(0,4)]+"\n")
    animalToTest, category, criteriaToAsk = findCriteriaToAsk(classAnimal, tabPossibilities)
    if animalToTest == "" :
        return 0
    delay_print(" ".join( [random.choice(queriesCategory.get(classAnimal).get(category)),criteriaToAsk,"?\n"]))
    answer = input()
    if answerYesOrNo(answer) :
        update_list(tabPossibilities,category,criteriaToAsk,1)
    else :
        update_list(tabPossibilities,category,criteriaToAsk,0)
    dataGuessing.get(classAnimal).get(category).append(criteriaToAsk)
    if len(tabPossibilities) > 1 :
        return 1
    else :
        return 0
#Find a criteria that was not already asked and present in our possibilities
def findCriteriaToAsk(classAnimal, tabPossibilities):
    for i in range (0,50): #Take a random animal in possibilities
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
    delay_print("\n*women singing* WILD GUESS, WILD GUESS, you make us WILD, WILD GUESS, WILD GUESS, you make us MAD *women singing*\n")
    delay_print("\nHello and welcome to WILD GUESS, the TV game that will leave you glued to your sofa along with your brain. Once again, I, your humble servant Francisco Xavier Prudencio Pinheiro will have the honour to be your presentator.\n")
    delay_print("Let's not waste any time, Here come our first challenger, give him a huuuuuuuge applause please !\n")
    print("*CLAP* *CLAP* *CLAP* *CLAP* *CLAP* *CLAP*\n")
    delay_print(" Well come on, do not make the crowd waiting, give us a name !\n")
    answer = input()
    name = answer
    updateDataWithName(name)
    nb = random.randint(0,1)
    delay_print(answerName[nb]+"\n")
    delay_print("\nI suppose you are already acquainted with the rules ? \n")
    answer = input()
    choice = answerYesOrNo(answer)
    if(choice):
        delay_print("Perfect, we have a professional here.\n")
    else :
        delay_print("I suppose it is time for explanations then.\n")
        delay_print("WILD GUESS is a simple game between you and us, and when I say us, I mean me and those genius behind me...\n")
        print("*cheers of crowd*")
        delay_print("...the objective is to find the animal that the other has in mind. \n2 modes are at your disposal, the first one, the Answering mode, will have you answering to our questions. Should we cannot find the animal then you win and you will go back heavier of a few thousand dollars. But should we succeed... well, let's not talk about that.\nIn the other mode, the Guessing mode, the table is turned and it is your turn to put us on the grill.\n")
    delay_print("\nThen now, it is time to choose the mode, if you want, you can leave the result to our wheel of Fate before you, so, do you want to choose by yourself ?\n")
    answer = input()
    choice = answerYesOrNo(answer)
    if(choice):
        delay_print("Great ! Then what will it be ? Are you going to guess our animal ?\n")
        answer = input()
        choice = answerYesOrNo(answer)
        if(choice):
            delay_print("You better be good !\n")
            modeGuessing()
        else:
            delay_print("Oh we will guess yours ? You better find a good animal !\n")
            modeAnswering(0)
    else:
        delay_print("Oh ! The Wheel of Fate then, let's spin it ! Just click wherever you want and the wheel will start.\n")
        wait()
        delay_print("*rolling*\nWhat will be the result, I cannot wait !\n*cheering*\n")
        resultWheel = random.uniform(0, 1)
        if resultWheel :
            delay_print("Let's go for the Guessing Mode !\n")
            modeGuessing()
        else :
            delay_print("Let's go for the Answering Mode !\n")
            modeAnswering(0)

#The bot tries to guess the animal that the player has in mind
def modeAnswering(valueRestart) :
    global answerRight
    answerRight = 0
    if not valueRestart :
        delay_print("\nLADIES AND GENTLEMEN, THE ANSWERING MODE CAN NOW BEGIN !\n")
        delay_print("\nWould you like to take a look at our incredible database of animals ? It could be useful to choose your animal or just ensure that your informations are right. I can't even count the number of people who do not know that a dolphin or a whale are mammals\nShould we open the database?\n")
        answer = input()
        choice = answerYesOrNo(answer)
        if(choice) :
            openDatabase()
    delay_print("Do you already have an animal in mind?\n")
    while answerRight == 0 :
        answer = input()
        choice = answerYesOrNo(answer)
        if(choice) :
            answerRight = 1
            delay_print("Perfect, let's move on then.\n")
        else :
            delay_print("Not yet ? Come on, the crowd is on fire, find us an animal !\n")
    delay_print("\nI will ask you a few questions, do not hesitate to tell me if you do not know or if you are not sure of the answer !\n")
    tabPossibilities = databaseAnimals.animals.copy()
    classAnimal = firstFilter(tabPossibilities)
    tabPossibilities = tabPossibilities.get(classAnimal)
    lvSmalltalk = 0
    numberQueries = 0
    boolQueries = 1
    while(boolQueries) :
        boolQueries = askQuestion(classAnimal,tabPossibilities,lvSmalltalk)
        numberQueries = numberQueries + 1
        if(numberQueries/4 > lvSmalltalk+1) and (lvSmalltalk < 2):
            lvSmalltalk = lvSmalltalk+1
    if(len(tabPossibilities) == 1): #Only one animal left
        lastAnimal, value = tabPossibilities.popitem()
        space = " "
        sentence = ("I would say that your animal is", "an" if lastAnimal[0] in vowels else "a",lastAnimal,"\n")
        delay_print(space.join(sentence))
        answerAnimal = input()
        if(answerYesOrNo(answerAnimal)):
            delay_print("Too easy.\n")
        else:
            delay_print("Oh my... I have no idea then.\n")
    elif(len(tabPossibilities) > 1): #Many animals and no queries to ask
        while (tabPossibilities):
            lastAnimal, value = tabPossibilities.popitem()
            space = " "
            sentence = ("I would say that your animal is", "an" if lastAnimal[0] in vowels else "a",lastAnimal,"\n")
            delay_print(space.join(sentence))
            answerAnimal = input()
            if(answerYesOrNo(answerAnimal)):
                delay_print("Too easy.\n")
                break
            else:
                delay_print("Whoooops\n")
            if (not tabPossibilities):
                 delay_print("I've got no idea... Did I make a mistake ? No. It must be you. False informations I'm sure, or maybe an animal not present in our database.\n")
    elif (not tabPossibilities):#No animals left in possibilities
        delay_print("I don't know any animal that matches your description... Are you sure that your informations are correct ? You should take a look at our database of animals\n")
    delay_print("\nMy, my, my, it is already the end of this session. Do you want to stop there ?\n")
    answer = input()
    if(answerYesOrNo(answer)):
        delay_print(" ".join(["How sad, let us give a huge row of applause for", name,"!"]))
    else:
        delay_print("Do you want to continue in the same mode ?\n")
        answer = input()
        if(answerYesOrNo(answer)):
            modeAnswering(1)
        else :
            modeGuessing(0)



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
    question = True if myInput[len(myInput)-1] == "?" else False
    for word in words:
        if "n't" in word or word in noWords:
            negative += 1
        elif "'s" in word or word in yesWords:
            positive += 1
        """elif "?" in word:
            question = True"""

    if question:
        randomQuestionHandling = random.choice(questionHandling)
        delay_print(randomQuestionHandling+" Answer my previous question first.\n") #TODO
        answer = input()
        return answerYesOrNo(answer)

    if negative == 0 and positive == 0:
        randomOpenAnswerHandling = random.choice(openAnswerHandling)
        delay_print(randomOpenAnswerHandling+" Please give an affirmative or negative answer.") #TODO
        answer = input()
        return answerYesOrNo(answer)

    return negative%2 == 0

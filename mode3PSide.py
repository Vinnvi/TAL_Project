#-*- coding: Utf-8 -*-
import main
import modeAnimal
import databaseAnimals
from modeAnimal import delay_print

def mode3PSide():
	delay_print("Ask me a Y/N question about an animal, or tell me an animal name :\n")

	#Generate animal to guess
	classeToGuess,animalToGuess = modeAnimal.chooseRandomAnimal()

	boucle(classeToGuess,animalToGuess)



def boucle(classeToGuess,animalToGuess):
	myInput = input()
	mots = myInput.lower().split()
	answer = decomposition_sentence(mots,classeToGuess,animalToGuess)
	if answer == "ok":
		delay_print("You guessed it!\n")
	else :
		delay_print(answer+"\n")
		boucle(classeToGuess,animalToGuess)


def decomposition_sentence(mots,classeToGuess,animalToGuess):

	negatif = False #to know if sentence is negative or not
	if not mots :
		return "Error, please give a sentence"
	else :
		if mots[0] in s_be_verbs :
			1
		elif mots[0] in auxiliary :
			if mots[1] in poss_pronouns :
				if mots[2] == "name":
					if mots[3] == "contains" or mots[3] == "contain":
						if mots[4] == "the":
							if mots[5] == "letter":
								return letter_question(mots,6,classeToGuess,animalToGuess)
							else:
								return letter_question(mots,5,classeToGuess,animalToGuess)
						elif mots[4] in a :
							return letter_question(mots,5,classeToGuess,animalToGuess)
						else:
							return letter_question(mots,4,classeToGuess,animalToGuess)
					if mots[3] in letter_verbs :
						if mots[4] == "by" or mots[4] == "with" :
							if mots[5] in a or mots[5]== "the":
								if mots[6] == "letter":
									return letter_question(mots,7,classeToGuess,animalToGuess)
								else :
									return letter_question(mots,6,classeToGuess,animalToGuess)
							elif mots[4] == "letter" :
								return letter_question(mots,6,classeToGuess,animalToGuess)
							else :
								return letter_question(mots,5,classeToGuess,animalToGuess)
					elif mots[3] == "has" :
						if mots[4] in a or mots[4]=="the":
							if mots[5] == "letter":
								return letter_question(mots,6,classeToGuess,animalToGuess)
							else :
								return letter_question(mots,5,classeToGuess,animalToGuess)
			elif mots[1] == "name" :
				if mots[2] == "contains":
					if mots[3] == "the":
						if mots[4] == "letter":
							return letter_question(mots,5,classeToGuess,animalToGuess)
						else:
							return letter_question(mots,4,classeToGuess,animalToGuess)
					elif mots[3] in a :
						return letter_question(mots,4,classeToGuess,animalToGuess)
					else:
						return letter_question(mots,3,classeToGuess,animalToGuess)
				if mots[2] in letter_verbs :
					if mots[3] == "by" or mots[3] == "with" :
						if mots[4] in a or mots[4]== "the":
							if mots[5] == "letter":
								return letter_question(mots,6,classeToGuess,animalToGuess)
							else :
								return letter_question(mots,5,classeToGuess,animalToGuess)
						elif mots[4] == "letter" :
							return letter_question(mots,5,classeToGuess,animalToGuess)
						else :
							return letter_question(mots,4,classeToGuess,animalToGuess)
				elif mots[2] == "has" :
					if mots[3] in a or mots[3]=="the":
						if mots[4] == "letter":
							return letter_question(mots,5,classeToGuess,animalToGuess)
						else :
							return letter_question(mots,4,classeToGuess,animalToGuess)
			elif mots[1] in subject :
				if checkConj(mots[1],mots[0]):
					if mots[2] == "live" or mots[2]=="lives":
						if mots[3] in modeAnimal.behaviour :
							return behaviour_question(mots[3],classeToGuess,animalToGuess)
						if mots[3] == "on" or mots[3]=="in":
							if mots[4] == "group":
								return behaviour_question("in group",classeToGuess,animalToGuess)
							if mots[4]=="the":
								return live_question(mots,5,classeToGuess,animalToGuess)
							elif mots[4]=="a":
								return live_question(mots,5,classeToGuess,animalToGuess)
							else:
								return live_question(mots,4,classeToGuess,animalToGuess)

					if mots[2] == "have" :
						if mots[3] == "many" and mots[4] == "colors":
							myAnimal = databaseAnimals.animals.get(classeToGuess).get(animalToGuess)
							myColors = myAnimal.get("colors")
							if "many colors" in myColors :
								return "Yes, it has many colors"
							else :
								return "No, it hasn't many colors"
						elif mots[3] in modeAnimal.colors :
							return color_question(mots,3,classeToGuess,animalToGuess)
						elif mots[3] == "wings" or mots[3] == "wing":
							return wings_question(mots,classeToGuess,animalToGuess)
						elif mots[3] == "fur" :
							return fur_question(mots,classeToGuess,animalToGuess)
				else :
					return "Conjuction mistake with Do verb"

		elif mots[0] in auxiliary_n :
			1
		elif mots[0] in be_verbs :
			if mots[1] in subject :
				if checkConj(mots[1],mots[0]):
					if mots[2] in modeAnimal.dietary:
						return dietary_question(mots[2],classeToGuess,animalToGuess)
					elif mots[2] == "living":
						if mots[3] in modeAnimal.behaviour :
							return behaviour_question(mots[3],classeToGuess,animalToGuess)
						elif mots[3] == "on" or mots[3]=="in":
							if mots[4] == "group":
								return behaviour_question("in group",classeToGuess,animalToGuess)
							elif mots[4]=="the":
								return live_question(mots,5,classeToGuess,animalToGuess)
							elif mots[4]=="a":
								return live_question(mots,5,classeToGuess,animalToGuess)
							else:
								return live_question(mots,4,classeToGuess,animalToGuess)

					elif mots[2] == "big" or mots[2] == "tall" or mots[2]=="large" :
						myAnimal = databaseAnimals.animals.get(classeToGuess).get(animalToGuess)
						mySize = myAnimal.get("size")
						if "large" in mySize :
							return "Yes it's a large animal"
						if "very large" in mySize :
							return "Yes, it's even a very large animal"
						else:
							return "No, it's not "+mots[2]
					elif mots[2] == "medium" :
						myAnimal = databaseAnimals.animals.get(classeToGuess).get(animalToGuess)
						mySize = myAnimal.get("size")
						if "medium" in mySize :
							return "Yes, it's an animal with a medium size"
						else:
							return "No, it's not medium"
					if mots[2] == "small" or mots[2] == "little" :
						myAnimal = databaseAnimals.animals.get(classeToGuess).get(animalToGuess)
						mySize = myAnimal.get("size")
						if "small" in mySize :
							return "Yes it's a small animal"
						if "very small" in mySize :
							return "Yes, it's even a very small animal"
						else:
							return "No, it's not "+mots[2]
					elif mots[2] in a :
						if mots[3] in modeAnimal.dietary:
							return dietary_question(mots[3],classeToGuess,animalToGuess)
						elif mots[3] in gender :
							return gender_question(mots,3,classeToGuess,animalToGuess)
						elif mots[3] in modeAnimal.colors :
							return color_question(mots,3,classeToGuess,animalToGuess)
						else :
							for classeA in list(databaseAnimals.animals.keys()) :
								for an in list(databaseAnimals.animals.get(classeA).keys()) :
									if an == animalToGuess and animalToGuess == mots[3]:
										return "ok"
							#don't manage h case yet (unpredictible)
							if mots[3][0] == "a" or mots[3][0] == "u" or mots[3][0] == "e" or mots[3][0] == "y" or mots[3][0] == "i" or mots[3][0] == "o":
								return "No, it's not an "+mots[3]
							else :
								return "No it's not a "+mots[3]
					elif mots[2] in modeAnimal.colors :
						return color_question(mots,2,classeToGuess,animalToGuess)
					elif mots[2] in gender :
						return gender_question(mots,2,classeToGuess,animalToGuess)
				else:
					return "Conjuction error with be verb"
		elif mots[0] in be_verbs_n :
			1
		elif mots[0] in su_be :
			if mots[1] in modeAnimal.dietary:
				return dietary_question(mots[1],classeToGuess,animalToGuess)
			elif mots[1] in size :
				return size_question(mots,1,classeToGuess,animalToGuess)
			elif mots[1] in a :
				if mots[2] in modeAnimal.dietary:
					return dietary_question(mots[2],classeToGuess,animalToGuess)
				elif mots[2] in gender :
					return gender_question(mots,2,classeToGuess,animalToGuess)
				elif mots[2] in modeAnimal.colors :
					return color_question(mots,2,classeToGuess,animalToGuess)
				else :
					for classeA in list(databaseAnimals.animals.keys()) :
						for an in list(databaseAnimals.animals.get(classeA).keys()) :
							if an == animalToGuess and animalToGuess==mots[2]:
								return "ok"
					#don't manage h case yet (unpredictible)
					if mots[2][0] == "a" or mots[2][0] == "u" or mots[2][0] == "e" or mots[2][0] == "y" or mots[2][0] == "i" or mots[2][0] == "o":
						return "No, it's not an "+mots[2]
					else :
						return "No it's not a "+mots[2]
			elif mots[1] in modeAnimal.colors :
				return color_question(mots,1,classeToGuess,animalToGuess)
		elif mots[0] in subject :
			if mots[1] == "live" or mots[1]=="lives":
				if mots[2] in modeAnimal.behaviour :
					return behaviour_question(mots[2],classeToGuess,animalToGuess)
				if mots[2] == "on" or mots[2]=="in":
					if mots[3] == "group":
						return behaviour_question("in group",classeToGuess,animalToGuess)
					if mots[3]=="the":
						return live_question(mots,4,classeToGuess,animalToGuess)
					elif mots[3]=="a":
						return live_question(mots,4,classeToGuess,animalToGuess)
					else:
						return live_question(mots,3,classeToGuess,animalToGuess)
			if mots[1] in be_verbs :
				if checkConj(mots[0],mots[1]):
					if mots[2] in modeAnimal.dietary:
						return dietary_question(mots[2],classeToGuess,animalToGuess)
					elif mots[2] == "living":
						if mots[3] in modeAnimal.behaviour :
							return behaviour_question(mots[3],classeToGuess,animalToGuess)
						if mots[3] == "on" or mots[3]=="in":
							if mots[4] == "group":
								return behaviour_question("in group",classeToGuess,animalToGuess)
							if mots[4]=="the":
								return live_question(mots,5,classeToGuess,animalToGuess)
							elif mots[4]=="a":
								return live_question(mots,5,classeToGuess,animalToGuess)
							else:
								return live_question(mots,4,classeToGuess,animalToGuess)
					if mots[2] in size :
						return size_question(mots,2,classeToGuess,animalToGuess)

					elif mots[2] in action_verbs:
						1
					elif mots[2] in a :
						if mots[3] in modeAnimal.dietary:
							return dietary_question(mots[3],classeToGuess,animalToGuess)
						elif mots[3] in gender :
							return gender_question(mots,3,classeToGuess,animalToGuess)

						elif mots[3] in modeAnimal.colors :
							return color_question(mots,3,classeToGuess,animalToGuess)
						else :

							for classeA in list(databaseAnimals.animals.keys()) :
								for an in list(databaseAnimals.animals.get(classeA).keys()) :
									if an == animalToGuess and animalToGuess==mots[3]:
										return "ok"
							#don't manage h case yet (unpredictible)
							if mots[3][0] == "a" or mots[3][0] == "u" or mots[3][0] == "e" or mots[3][0] == "y" or mots[3][0] == "i" or mots[3][0] == "o":
								return "No, it's not an "+mots[3]
							else :
								return "No it's not a "+mots[3]
					elif mots[2] in modeAnimal.colors :
						return color_question(mots,2,classeToGuess,animalToGuess)


			elif mots[1] in be_verbs_n :
				1
			elif mots[1] in be_verbs :
				1
			elif mots[1] in action_verbs :
				1
			elif mots[1] in auxiliary :
				1
			elif mots[1] in auxiliary_n :
				1
			elif mots[1] in have_verbs :
				if checkConj(mots[0],mots[1]) :
					if mots[2] == "many" and mots[3] == "colors":
						myAnimal = databaseAnimals.animals.get(classeToGuess).get(animalToGuess)
						myColors = myAnimal.get("colors")
						if "many colors" in myColors :
							return "Yes, it has many colors"
						else :
							return "No, it hasn't many colors"

					elif mots[2] in modeAnimal.colors :
						return color_question(mots,2,classeToGuess,animalToGuess)
					elif mots[2] == "wings" or mots[2] == "wing":
						return wings_question(mots,classeToGuess,animalToGuess)
					elif mots[2] == "fur" :
						return fur_question(mots,classeToGuess,animalToGuess)
				else :
					return "conjugation error with have verb"

		elif mots[0] in action_verbs :
			if mots[0] == "live" or mots[0]=="living" or mots[0]=="lives":
				if mots[1] in modeAnimal.behaviour :
					return behaviour_question(mots[3],classeToGuess,animalToGuess)
				if mots[1] == "on" or mots[1]=="in":
					if mots[2] == "group":
						return behaviour_question("in group",classeToGuess,animalToGuess)
					if mots[2]=="the":
						return live_question(mots,3,classeToGuess,animalToGuess)
					elif mots[2]=="a":
						return live_question(mots,3,classeToGuess,animalToGuess)
					else:
						return live_question(mots,2,classeToGuess,animalToGuess)
		elif mots[0] in poss_pronouns :
			if mots[1] == "name":
				if mots[2] == "contains":
					if mots[3] == "the":
						if mots[4] == "letter":
							return letter_question(mots,5,classeToGuess,animalToGuess)
						else:
							return letter_question(mots,4,classeToGuess,animalToGuess)
					elif mots[3] in a :
						return letter_question(mots,4,classeToGuess,animalToGuess)
					else:
						return letter_question(mots,3,classeToGuess,animalToGuess)
				if mots[2] in letter_verbs :
					if mots[3] == "by" or mots[3] == "with" :
						if mots[4] in a or mots[4]== "the":
							if mots[5] == "letter":
								return letter_question(mots,6,classeToGuess,animalToGuess)
							else :
								return letter_question(mots,5,classeToGuess,animalToGuess)
						elif mots[4] == "letter" :
							return letter_question(mots,5,classeToGuess,animalToGuess)
						else :
							return letter_question(mots,4,classeToGuess,animalToGuess)
				elif mots[2] == "has" :
					if mots[3] in a or mots[3]=="the":
						if mots[4] == "letter":
							return letter_question(mots,5,classeToGuess,animalToGuess)
						else :
							return letter_question(mots,4,classeToGuess,animalToGuess)
		elif mots[0] == "name":
			if mots[1] == "contains":
				if mots[2] == "the":
					if mots[3] == "letter":
						return letter_question(mots,4,classeToGuess,animalToGuess)
					else:
						return letter_question(mots,3,classeToGuess,animalToGuess)
				elif mots[2] in a :
					return letter_question(mots,3,classeToGuess,animalToGuess)
				else:
					return letter_question(mots,2,classeToGuess,animalToGuess)
			if mots[1] in letter_verbs :
				if mots[2] == "by" or mots[2] == "with" :
					if mots[3] in a or mots[3]== "the":
						if mots[4] == "letter":
							return letter_question(mots,5,classeToGuess,animalToGuess)
						else :
							return letter_question(mots,4,classeToGuess,animalToGuess)
					elif mots[3] == "letter" :
						return letter_question(mots,4,classeToGuess,animalToGuess)
					else :
						return letter_question(mots,3,classeToGuess,animalToGuess)
			elif mots[1] == "has" :
				if mots[2] in a or mots[2]=="the":
					if mots[3] == "letter":
						return letter_question(mots,4,classeToGuess,animalToGuess)
					else :
						return letter_question(mots,3,classeToGuess,animalToGuess)
		else :
			return "error"
		return "error"

def behaviour_question(mot,classeToGuess,animalToGuess):
	myAnimal = databaseAnimals.animals.get(classeToGuess).get(animalToGuess)
	myBehaviour = myAnimal.get("behaviour")
	if not myBehaviour :
		return "Sorry, we have no info about its behaviour"
	elif mot in myBehaviour:
		return "Yes, he lives "+mot
	else:
		return "No, it doesn't live "+mot

def dietary_question(mot,classeToGuess,animalToGuess):
	myAnimal = databaseAnimals.animals.get(classeToGuess).get(animalToGuess)
	myDietary = myAnimal.get("dietary")
	if not myDietary :
		return "Sorry, we have no info about its dietary"
	elif mot in myDietary:
		return "Yes, it's "+mot
	else:
		return "No, it's not "+mot

def live_question(mots,level,classeToGuess,animalToGuess):
	myAnimal = databaseAnimals.animals.get(classeToGuess).get(animalToGuess)
	myLocation = myAnimal.get("location")
	if not myLocation :
		return "It doesn't live in a specific place"
	else :
		if mots[level] in myLocation :
			return "Yes, it lives in "+mots[level]
		else:
			return "No, it doesn't live in "+mots[level]

def letter_question(mots,level,classeToGuess,animalToGuess):
	if not mots[level] :
		return "error : donnez une lettre"
	else :
		if len(mots[level])>1:
			return "error : please just give one letter"
		else :
			myAnimal = animalToGuess
			if "start" in mots or "starts" in mots or "begin" in mots or "begins" in mots:
				if myAnimal[0] == mots[level]:
					return "Yes, it starts with by a "+mots[level]
				else:
					return "No, it doesn't start by a "+mots[level]
			elif "end" in mots or "ends" in mots or "finish" in mots or "finishes" in mots :
				s = len(myAnimal)
				if myAnimal[s-1] == mots[level]:
					return "Yes, it ends by a "+mots[level]
				else :
					return "No, "+mots[level]+" is not the last letter"
			else :
				if mots[level] in myAnimal:
					return "Yes, it contains the letter "+mots[level]
				else :
					return "No, there is no "+mots[level]



def size_question(mots,level,classeToGuess,animalToGuess):
	if mots[level] == "big" or mots[level] == "tall" or mots[level]=="large" :
		myAnimal = databaseAnimals.animals.get(classeToGuess).get(animalToGuess)
		mySize = myAnimal.get("size")
		if "large" in mySize :
			return "Yes it's a large animal"
		if "very large" in mySize :
			return "Yes, it's even a very large animal"
		else:
			return "No, it's not "+mots[level]
	elif mots[level] == "medium" :
		myAnimal = databaseAnimals.animals.get(classeToGuess).get(animalToGuess)
		mySize = myAnimal.get("size")
		if "medium" in mySize :
			return "Yes, it's an animal with a medium size"
		else:
			return "No, it's not medium"
	if mots[level] == "small" or mots[level] == "little" :
		myAnimal = databaseAnimals.animals.get(classeToGuess).get(animalToGuess)
		mySize = myAnimal.get("size")
		if "small" in mySize :
			return "Yes it's a small animal"
		if "very small" in mySize :
			return "Yes, it's even a very small animal"
		else:
			return "No, it's not "+mots[level]

def color_question(mots,level,classeToGuess,animalToGuess):
	myAnimal = databaseAnimals.animals.get(classeToGuess).get(animalToGuess)
	myColors = myAnimal.get("colors")
	for c in myColors :
		if mots[level] == c :
			return "Yes, it is "+mots[level]
	return "No, it is not "+mots[level]

def wings_question(mots,classeToGuess,animalToGuess):
	if classeToGuess != "insect" and classeToGuess != "bird" :
		return "No, it has no wings"
	elif classeToGuess == "bird" :
		return "Yes, it has wings"
	else :
		myAnimal = databaseAnimals.animals.get(classeToGuess).get(animalToGuess)
		myWings = myAnimal.get("wings")
		if myWings == "wings" :
			return "Yes, it has wings"
		else :
			return "No, it has no wings"

def gender_question(mots,level,classeToGuess,animalToGuess):
	if classeToGuess == mots[level]:
		return "Yes it is."
	else :
		return "No, it's not a "+mots[level]

def fur_question(mots,classeToGuess,animalToGuess):
	if classeToGuess != "mammal":
		return "No, it has no fur"
	else :
		myAnimal = databaseAnimals.animals.get(classeToGuess).get(animalToGuess)
		myEpiderm = myAnimal.get("epiderm")
	if myEpiderm == "fur" :
		return "Yes, it has fur"
	else :
		return "No, it has no fur"

auxiliary_n = ["don't","can't","couldn't"]
auxiliary = ["did","does","do","can","could"]
subject = ["animal","it","he","she","they","i"]
su_be = ["i'm","it's","you're","we're","they're","he's","she's"]
be_verbs = ["was","is","will","were","am","are","i'm","it's"]
be_verbs_n = ["isn't","aren't","wasn't"]
s_be_verbs = ["i'm","it's"]
a = ["a","an","the"]
negative = ["not","no"]
have_verbs = ["have","has","had"]
poss_pronouns = ["my","your","his","her","its","our","their"]

size = ["big","tall","large","medium","small","little"]

see = ["see","saw","seen","seeing","sees"]
live = ["live","living","lives","lived"]
fly = ["fly","flying","flies","flew","flown"]
swim = ["swim","swimming","swam","swum","swims"]
crawl = ["crawling","crawl","crawled","crawls"]
eat = ["eat","eating","eats","ate","eaten"]


letter_verbs = ["start","starts","contains","contain","end","ends","finishes","begin","begins"]

action_verbs = [see,live,fly,swim,crawl,eat]
t = ["ever","never","already"]
location = ["caves","grassland","city","water","savannah","forest","jungle","river","mountain","mountains","desert","antartic","sea","floe"]
gender  = ["bird","fish","mammal","insect"]

#disable you + is possibility for example (and check 's' for 3rd person)
#aim subject + be/have/do
def checkConj(subject,verb):
	if subject == "i" :
		if verb == "am" or verb == "have" or verb=="do":
			return True
		else :
			return False
	if subject == "you" or subject == "we" or subject == "they" :
		if verb == "are" or verb == "have"  or verb=="do":
			return True
		else :
			return False
	if subject == "it" or subject == "he" or subject == "she":
		if verb == "is" or verb == "has"  or verb=="does" :
			return True
		else :
			return False
	return False

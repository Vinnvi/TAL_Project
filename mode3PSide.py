#-*- coding: Utf-8 -*-
import main
import modeAnimal 
import databaseAnimals

def mode3PSide(turnNumber):
	print("Ask me a Y/N question about what animal guess, or tell me an animal name :")
	myInput = input()
	mots = myInput.lower().split()

	#Generate animal to guess
	classeToGuess,animalToGuess = modeAnimal.chooseRandomAnimal()

	answer = decomposition_sentence(mots,classeToGuess,animalToGuess)

	if answer == "ok":
		print("You guess it!")
	else :
		print(answer)



	turnNumber = turnNumber+1
	mode3PSide(turnNumber)

def decomposition_sentence(mots,classeToGuess,animalToGuess):

	negatif = False #to know if sentence is negative or not 
	if mots[0] == "" :
		return "Error, please give a sentence"
	else :
		if mots[0] in s_be_verbs :
			1
		elif mots[0] in auxiliary :
			1
		elif mots[0] in auxiliary_n :
			1
		elif mots[0] in be_verbs :
			1
		elif mots[0] in be_verbs_n :
			1

		elif mots[0] in subject :
			if mots[1] in be_verbs :
				if mots[2] in action_verbs:
					1
				if mots[2] in a :
					if mots[3] in modeAnimal.colors :
						myAnimal = databaseAnimals.animals.get(classeToGuess).get(animalToGuess)
						myColors = myAnimal.get("colors")
						for c in myColors :
							if mots[3] == c :
								return "Yes, it is "+mots[3]
						return "No, it is not "+mots[3]
					else :

						for animal in databaseAnimals.animals.keys() :
							for an in databaseAnimals.animals.get(animal).keys() :
								if an == animalToGuess :
									return "ok"
								else :
									#don't manage h case yet (unpredictible)
									if mots[2][0] == "a" or mots[2][0] == "u" or mots[2][0] == "e" or mots[2][0] == "y" or mots[2][0] == "i" or mots[2][0] == "o":
										return "No, it's not an "+mots[3]
									else : 
										return "No it's not a "+mots[3]

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

		elif mots[0] in action_verbs :
			1
		else :
			return "error"
		return "error"

auxiliary_n = ["don't","can't","couldn't"]
auxiliary = ["did","does","do","can","could"]
subject = ["animal","it","he","she","they","i"]
be_verbs = ["was","is","will","were","am","are","i'm","it's"]
be_verbs_n = ["isn't","aren't","wasn't"]
s_be_verbs = ["i'm","it's"]
a = ["a","an","the"]
negatve = ["not"]
have_verbs = ["have","has","had"]


see = ["see","saw","seen","seeing","sees"]
live = ["live","living","lives","lived"]
fly = ["fly","flying","flies","flew","flown"]
swim = ["swim","swimming","swam","swum","swims"]
crawl = ["crawling","crawl","crawled","crawls"]
eat = ["eat","eating","eats","ate","eaten"]

action_verbs = [see,live,fly,swim,crawl,eat]
t = ["ever","never","already"]
location = ["grassland","city","water","savannah","forest","jungle","river","mountain","mountains","desert","antartic","sea","floe"]

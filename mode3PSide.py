#-*- coding: Utf-8 -*-
import main
import modeAnimal
import databaseAnimals

def mode3PSide():
	print("Ask me a Y/N question about what animal guess, or tell me an animal name :")

	#Generate animal to guess
	classeToGuess,animalToGuess = modeAnimal.chooseRandomAnimal()

	boucle(classeToGuess,animalToGuess)



def boucle(classeToGuess,animalToGuess):
	myInput = input()
	mots = myInput.lower().split()
	answer = decomposition_sentence(mots,classeToGuess,animalToGuess)
	if answer == "ok":
		print("You guess it!")
	else :
		print(answer)
		boucle(classeToGuess,animalToGuess)


def decomposition_sentence(mots,classeToGuess,animalToGuess):

	negatif = False #to know if sentence is negative or not
	if not mots :
		return "Error, please give a sentence"
	else :
		if mots[0] in s_be_verbs :
			1
		elif mots[0] in auxiliary :
			if mots[1] in subject :
				if checkConj(mots[1],mots[0]):
					if mots[2] == "have" :
						if mots[3] == "many" and mots[4] == "colors":
							myAnimal = databaseAnimals.animals.get(classeToGuess).get(animalToGuess)
							myColors = myAnimal.get("colors")
							if "many colors" in myColors :
								return "Yes, it has many colors"
							else :
								return "No, it hasn't many colors"

						elif mots[3] == "wings" or mots[3] == "wing":
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
						elif mots[3] == "fur" :
							if classeToGuess != "mammal":
								return "No, it has no fur"
							else :
								myAnimal = databaseAnimals.animals.get(classeToGuess).get(animalToGuess)
								myEpiderm = myAnimal.get("epiderm")
								if myEpiderm == "fur" :
									return "Yes, it has fur"
								else :
									return "No, it has no fur"
				else :
					return "Conjuction mistake with Do verb"

		elif mots[0] in auxiliary_n :
			1
		elif mots[0] in be_verbs :
			if mots[1] in subject :
				if checkConj(mots[1],mots[0]):
					if mots[2] in a :
						if mots[3] in gender :
							if classeToGuess == mots[3]:
								return "Yes it is."
							else :
								return "No, it's not a "+mots[3]
						elif mots[3] in modeAnimal.colors :
							myAnimal = databaseAnimals.animals.get(classeToGuess).get(animalToGuess)
							myColors = myAnimal.get("colors")
							for c in myColors :
								if mots[3] == c :
									return "Yes, it is "+mots[3]
							return "No, it is not "+mots[3]
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
						myAnimal = databaseAnimals.animals.get(classeToGuess).get(animalToGuess)
						myColors = myAnimal.get("colors")
						for c in myColors :
							if mots[3] == c :
								return "Yes, it is "+mots[2]
						return "No, it is not "+mots[2]
					elif mots[2] in gender :
						if classeToGuess == mots[2]:
							return "Yes it is."
						else :
							return "No, it's not a "+mots[2]
				else:
					return "Conjuction error with be verb"
		elif mots[0] in be_verbs_n :
			1
		elif mots[0] in su_be :
			if mots[1] in a :
				if mots[2] in gender :
					if classeToGuess == mots[2]:
						return "Yes it is."
					else :
						return "No, it's not a "+mots[2]
				if mots[2] in modeAnimal.colors :
					myAnimal = databaseAnimals.animals.get(classeToGuess).get(animalToGuess)
					myColors = myAnimal.get("colors")
					for c in myColors :
						if mots[2] == c :
							return "Yes, it is "+mots[2]
					return "No, it is not "+mots[2]
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
				myAnimal = databaseAnimals.animals.get(classeToGuess).get(animalToGuess)
				myColors = myAnimal.get("colors")
				for c in myColors :
					if mots[2] == c :
						return "Yes, it is "+mots[2]
				return "No, it is not "+mots[2]

		elif mots[0] in subject :
			if mots[1] in be_verbs :
				if mots[2] in action_verbs:
					1
				if mots[2] in a :
					if mots[3] in gender :
						if classeToGuess == mots[3]:
							return "Yes it is."
						else :
							return "No, it's not a "+mots[3]

					if mots[3] in modeAnimal.colors :
						myAnimal = databaseAnimals.animals.get(classeToGuess).get(animalToGuess)
						myColors = myAnimal.get("colors")
						for c in myColors :
							if mots[3] == c :
								return "Yes, it is "+mots[3]
						return "No, it is not "+mots[3]
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
					myAnimal = databaseAnimals.animals.get(classeToGuess).get(animalToGuess)
					myColors = myAnimal.get("colors")
					for c in myColors :
						if mots[2] == c :
							return "Yes, it is "+mots[2]
					return "No, it is not "+mots[2]


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
						myAnimal = databaseAnimals.animals.get(classeToGuess).get(animalToGuess)
						myColors = myAnimal.get("colors")
						for c in myColors :
							if mots[2] == c :
								return "Yes, it is "+mots[2]
						return "No, it is not "+mots[2]
					elif mots[2] == "wings" or mots[2] == "wing":
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
					elif mots[2] == "fur" :
						if classeToGuess != "mammal":
							return "No, it has no fur"
						else :
							myAnimal = databaseAnimals.animals.get(classeToGuess).get(animalToGuess)
							myEpiderm = myAnimal.get("epiderm")
						if myEpiderm == "fur" :
							return "Yes, it has fur"
						else :
							return "No, it has no fur"
				else :
					return "conjugation error with have verb"

		elif mots[0] in action_verbs :
			1
		else :
			return "error"
		return "error"

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


see = ["see","saw","seen","seeing","sees"]
live = ["live","living","lives","lived"]
fly = ["fly","flying","flies","flew","flown"]
swim = ["swim","swimming","swam","swum","swims"]
crawl = ["crawling","crawl","crawled","crawls"]
eat = ["eat","eating","eats","ate","eaten"]

action_verbs = [see,live,fly,swim,crawl,eat]
t = ["ever","never","already"]
location = ["grassland","city","water","savannah","forest","jungle","river","mountain","mountains","desert","antartic","sea","floe"]
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

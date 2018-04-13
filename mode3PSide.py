#-*- coding: Utf-8 -*-
import main
import modeAnimal 

def main3PSide(turnNumber):
	print("Ask me a Y/N question about what animal guess, or tell me an animal name :")
	myInput = input()
	mots = myInput.lower().split()

	answer = decomposition_sentence(mots)

	if answer == "ok":
		print("You guess it! You found it in "+turnNumber+" turns")
	else :
		print(answer)



	turnNumber = turnNumber+1
	main3PSide(turnNumber)

def decomposition_sentence(mots):
	answer == []
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
					1
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

auxiliary_n = ["don't","can't","couldn't"]
auxiliary = ["did","does","do","can","could"]
subject = ["animal","it","he","she","they","i"]
be_verbs = ["was","is","will","were","am","are","i'm","it's"]
be_verbs_n = ["isn't","aren't","wasn't"]
s_be_verbs = ["i'm","it's"]
a = ["a","an","the"]
negatve = ["not"]
have_verbs = ["have","has","had"]
action_verbs = [see["see","saw","seen","seeing","sees"],live["live","living","lives","lived"],fly["fly","flying","flies","flew","flown"],swim["swim","swimming","swam","swum","swims"],crawl["crawling","crawl","crawled","crawls"],eat["eat","eating","eats","ate","eaten"]]
t = ["ever","never","already"]
location = ["grassland","city","water","savannah","forest","jungle","river","mountain","mountains","desert","antartic","sea","floe"]


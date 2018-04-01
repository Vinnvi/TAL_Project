#-*- coding: Utf-8 -*-
import re
import random

sante = ["Santé","cancer","maladie","pneumonie","mal","tête","ventre","fatigue","douleur","sida"]
famille = ["parents","fils","fille","père","mère","soeur","frère","grands-parents","grand-père","grand-mère","cousin","cousine","famille","femme","mari","oncle","tante"]
pays = ["pays","monde","France","Allemagne","Angleterre","Espagne","Europe","Brésil","Asie","Canada","USA","Russie","Italie"]
travail = ["université","société","entreprise","stage","rapport","collègue","supérieur","bureau","projet","travail"]
loisir = ["sport","cinéma","dance","jeux vidéo","lecture","promenade","dormir","fête","télévision","musique"]

answerSante = ["Parlez-moi s'en plus","c'est bien, coninuez à en parler"]
answerFamille = ["Parlez moi un peu plus de votre famille","Continuez à partager avec moi ce que vous pensez de votre famille"]
answerPays = ["Vous souhaitez faire un voyage ?","parlez moi de votre destination de rêve"]
answerTravail = ["le travail vous inquiète ?","Decrivez votre travail"]
answerLoisir = ["Parlez moi de ce qui vous passionne","Cette activité vous passionne ?"]

def mode1():
	1
def mode2():
	print("Mode 2 selectionné")
	print("Parlez-moi de vous, qu'avez vous à me dire ?")
	while(1 == 1):
		myInput = input()
		MyAnswer = answer(myInput)
		print(MyAnswer)

def mode3():
	print("Hello love, I am Soraya, I will help uncover the secrets of your soul.")
	from modeLove import modeLove
	modeLove()

def answer(myInput) :
	mots = myInput.lower().split()
	for t in mots :
		for m in sante: 
			if t == m :
				answer = chooseAnswer(sante)
				return answer
		for m in famille :
			if t == m :
				answer = chooseAnswer(famille)
				return answer
		for m in pays :
			if t == m :
				answer = chooseAnswer(pays)
				return answer
		for m in travail :
			if t == m :
				answer = chooseAnswer(travail)
				return answer
		for m in loisir :
			if t == m :
				answer = chooseAnswer(loisir)
				return answer

	return("erreur") 



def chooseAnswer(category):
	nombreDeBase = random.randint(0,1)
	if category == "sante" :
		return answerSante[nombreDeBase]
	elif category == "famille" :
		return answerFamille[nombreDeBase]
	elif category == "pays" :
		return answerPays[nombreDeBase]
	elif category == "travail" :
		return answerTravail[nombreDeBase]
	elif category == "loisir" :
		return answerLoisir[nombreDeBase]



if __name__ == "__main__":
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('mode', type=int, choices=range(1, 4))
	args = parser.parse_args()

	print("Bonjour, Je m'appelle TALBOT")
	print("Vous avez choisi le mode",args.mode)
	if args.mode==1 :
		mode1()
	elif args.mode==2 :
		mode2()
	elif args.mode==3 :
		mode3()


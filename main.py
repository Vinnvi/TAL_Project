#-*- coding: Utf-8 -*-
import re
import random

sante = ["health","cancer","disease","pneumonia","pain","head","stomach","belly","tired","suffering","suffer","hiv","aids"]
famille = ["parents","son","daughter","father","dad","daddy","mother","mom","mum","mommy","sister","brother","grandparents","granny","grannies","grandfather","grandmother","cousin","family","wife","husband","uncle","aunt"]
pays = ["country","world","France","germany","england","spain","Europe","Brazil","Asia","Canada","USA","Russia","Italia"]
travail = ["university","society","company","internship","report","cojleague","co-worker","superior","supervisor","manager","office","project","work"]
loisir = ["sport","movie","movies","danse","video games","reading","walk","sleep","party","television","music"]

answerSante = ["Tell me more","Very good, continue please, it's important for me and of course for you"]
answerFamille = ["Tell me more about your family","Continuez à partager avec moi ce que vous pensez de votre famille"]
answerPays = ["Vous souhaitez faire un voyage ?","parlez moi de votre destination de rêve"]
answerTravail = ["le travail vous inquiète ?","Decrivez votre travail"]
answerLoisir = ["Parlez moi de ce qui vous passionne","Cette activité vous passionne ?"]


answerMode1 = ["well...","hummmm...","ehhhh","humm okay I suppose...","continue please",]

def mode1():
	print("Tell me something:")
	
	while 1==1:
		myInput=input()
		myInput = answer(myInput)
		print(myInput)


def answer(myInput,n):
	nombreDeBase = random.randint(0,4)
	return answerMode1[nombreDeBase]

def mode2():
	print("Mode 2 selectionné")
	print("So , what you want to tell me ? Do you have any problem ?")
	n = -1
	while(1 == 1):
		myInput = input()
		MyAnswer = answer2(myInput,n)
		n = MyAnswer[1]
		if MyAnswer[0] == "erreur":
			print(answer(myInput,MyAnswer[1]))
		else :
			print(MyAnswer[0])

def answer2(myInput,n) :
	mots = myInput.lower().split()

	for t in mots :
		for m in sante: 
			if t == m :
				answer1 = chooseAnswer("sante",n)
				return answer1
		for m in famille :
			if t == m :
				answer1 = chooseAnswer("famille",n)
				return answer1
		for m in pays :
			if t == m :
				answer1 = chooseAnswer("pays",n)
				return answer1
		for m in travail :
			if t == m :
				answer1 = chooseAnswer("travail",n)
				return answer1
		for m in loisir :
			if t == m :
				answer1 = chooseAnswer("loisir",n)
				return answer1

	return "erreur",n



def chooseAnswer(category,n):
	
	nombreDeBase = random.randint(0,1)
	while n == nombreDeBase:
		nombreDeBase = random.randint(0,1)
	l = "test"
	if category == "sante" :
		l = answerSante[nombreDeBase]
	elif category == "famille" :
		l = answerFamille[nombreDeBase]
	elif category == "pays" :
		l = answerPays[nombreDeBase]
	elif category == "travail" :
		l = answerTravail[nombreDeBase]
	elif category == "loisir" :
		l = answerLoisir[nombreDeBase]

	a = [l,nombreDeBase]
	return a

def mode3():
	1



if __name__ == "__main__":
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('mode', type=int, choices=range(1, 4))
	args = parser.parse_args()

	print("Hello, the following list represents modes you can use :\n1 - backchannels mode\n2 - Basic mode\n3 - Advanced mode")
	print("Vous avez choisi le mode ",args.mode)
	if args.mode==1 :
		mode1()
	elif args.mode==2 :
		mode2()
	else :
		mode3()


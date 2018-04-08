#-*- coding: Utf-8 -*-
import re
import random


sante = ["health","cancer","disease","pneumonia","pain","head","stomach","belly","tired","suffering","suffer","hiv","aids"]
famille = ["parents","son","daughter","kids","children","father","dad","daddy","mother","mom","mum","mommy","sister","brother","grandparents","granny","grannies","grandfather","grandmother","cousin","family","wife","husband","uncle","aunt"]
pays = ["country","world","france","germany","england","spain","europe","brazil","asia","canada","usa","russia","italy"]
travail = ["university","society","company","internship","report","cojleague","co-worker","superior","supervisor","manager","office","project","work","job"]
loisir = ["sport","movie","movies","danse","video games","reading","walk","sleep","party","television","music","cinema"]

answerSante = ["Tell me more","Ohh I'm sorry to hear that, please continue, it's important for me and of course for you"]
answerFamille = ["Tell me more about your family","Oh you talk about your family, it seems to be important for you"]
answerPays = ["Would you like to travel ? ","Do you have any dream destination ?"]
answerTravail = ["Are you worried about something, concerning your work ?","Contiue to talk about work, that's interesting"]
answerLoisir = ["Talk about what you like ","Oh, this activity is your passion? Later, it could be your work!"]


answerMode1 = ["well...","hummmm...","ehhhh","humm okay I suppose...","continue please",]



def mode1():
	print("Tell me something:")
	lastAnswer1 = -1
	while 1==1:
		myInput=input()
		myInput = answer(myInput,lastAnswer1)
		lastAnswer1 = myInput[1]
		print(myInput[0])


def answer(myInput,lastAnswer1):
	nombreDeBase = random.randint(0,4)
	while lastAnswer1 == nombreDeBase:
		nombreDeBase = random.randint(0,4)
	lastAnswer1 = nombreDeBase
	return answerMode1[nombreDeBase],lastAnswer1

def mode2():
	print("So , what you want to tell me ? Do you have any problem ?")
	n = -1
	lastAnswer1 = -1
	while(1 == 1):
		myInput = input()
		MyAnswer = answer2(myInput,n)
		n = MyAnswer[1]
		if MyAnswer[0] == "erreur":
			r = answer(myInput,lastAnswer1)
			print(r[0])
			lastAnswer1 = r[1]

		elif MyAnswer[0] == "":
			1
		else :
			print(MyAnswer[0])

def mode3():
	from modeAnimal import modeAnimal
	modeAnimal()

def answer2(myInput,n) :

	mots = myInput.lower().split()
	#I'm X part
	im = return_indice(mots,"i'm")
	if len(im) > 0 :
		end = ""
		indice_courant = 0
		for w in mots :
			if indice_courant > im[0]:
				end = end+" "+w
			indice_courant = indice_courant+1
		print("Why are you"+end+" ?")
	else:
		i = return_indice(mots,"i")
		if len(i) > 0 :
			am = return_indice(mots,"am")
			was = return_indice(mots,"was")
			will = return_indice(mots,"will")
			if len(am)>0 :
				for amP in am :
					if amP - i[0] == 1:
						end = ""
						indice_courant = 0
						for w in mots :
							if indice_courant > amP:
								end = end+" "+w
							indice_courant = indice_courant+1
						print("Why are you"+end+" ?")
						return "",0
			elif len(was)>0 :
				for wasP in was :
					if wasP - i[0] == 1:
						end = ""
						indice_courant = 0
						for w in mots :
							if indice_courant > wasP :
								end = end+" "+w
							indice_courant = indice_courant+1
						print("Why were you"+end+" ?")
						return "",0
			elif len(will)>0:
				for willP in will :
					if willP - i[0] == 1:
						be = return_indice(mots,"be")
						for beP in be :
							if beP - willP == 1:
								end = ""
								indice_courant = 0
								for w in mots :
									if indice_courant > beP :
										end = end+" "+w
									indice_courant = indice_courant+1
								print("Why you will be"+end+" ?")
								return "",0

	#End I'm X part

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

#return index(es) of an element in list
def return_indice(tab,word):
	i = 0
	return_tab = []
	for w in tab :
		if w == word :
			return_tab.append(i)
		i = i+1
	return return_tab



if __name__ == "__main__":
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('mode', type=int, choices=range(1, 4))
	args = parser.parse_args()

	print("Hello, the following list represents modes you can use :\n1 - backchannels mode\n2 - Basic mode\n3 - Advanced mode")
	print("And you choose mode ",args.mode)
	if args.mode==1 :
		mode1()
	elif args.mode==2 :
		mode2()
	elif args.mode==3 :
		mode3()

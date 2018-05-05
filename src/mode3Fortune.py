#-*- coding: Utf-8 -*-
import re
import random

astroSign ["aquarius", "psices", "aries", "taurus", "gemini", "cancer", "leo", "virgo", "libra", "scorpio", "sagittarius", "capricorn"]

def mode3():
	print("You selected mode 3.")
	print("Tell me, dear, what would you like to know?")
	while(true):
		myInput = input()
		MyAnswer = answer(myInput)
		print(MyAnswer)

def answer(myInput) :
	mots = myInput.lower().split()
	for t in mots :
		for m in sante: 
			if t == m :
				answer = chooseAnswer(sante)
				return answer

	return("erreur") 



def chooseAnswer(category):
	nombreDeBase = random.randint(0,1)
	if category == "sante" :
		return answerSante[nombreDeBase]
	

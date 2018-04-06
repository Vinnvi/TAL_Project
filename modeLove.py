#-*- coding: Utf-8 -*-
import re
import random
import time
import sys

yes = ["yes","why not","i agree","up for it","like\n"]
no = ["no","not sure","decline","not up for it\n"]
idk = ["idk","don't know","not sure","not really sure\n"]
convers = ["Oh incredible ! Go on, I want to know more !\n",
"I cannot believe that, tell me more\n",
"I can feel the spirits gathering, your fated one is not far ! Another answer !\n",
"Oh my, I wish I could be your fated one, please continue love\n",
"I'm fascinated, do not stop\n",
"Oh. I wasn't expecting that. But do not stop\n",
"What I want is more information ! Why are you stopping ?\n",
"I cannot get enough of that sweet mouth, make it work again\n",
"Hummm Soraya sees, but Soraya wants you to continue\n",
"Soraya is sad, Soraya needs more information\n",
"Soraya is near, just a little bit more, go on love\n",
"My... that's... surprising, please tell me more\n",
"Did Soraya turn off the lights before leaving? Oh... Sorry. Please go on\n"]
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)
def modeLove():
	print("Phase 2")
	
	delay_print("What an exciting future. I do wonder through, aren't you curious to know the one who is going to share it with you ?\n\n")
	answer = input()
	choice = answerYesOrNo(answer)
	if(choice):
		delay_print("Do not worry, Soraya shall find it for you.\n")
	else:
		delay_print("Oh well, that's too bad. you made Soraya sad.\n\n")
		return 0
	delay_print("First my sweetheart, Soraya need to gather the spirits to visualize your fated one. Answering a few questions will help Soraya in its task\n")
	delay_print("Tell me something about yourself love, what is your heart beating for?\n\n")
	answer = input()
	boucle = 0
	while boucle < 3 :
		nb = random.randint(0,11)
		delay_print(convers[nb])
		answer = input()
		boucle = boucle + 1
		
def answerYesOrNo(myInput) :
	mots = myInput.lower().split()
	numberYes = 0
	numberNo = 0
	numberNot = 0
	for t in mots :
		if(t == "not") or (t == "don't") or (t == "aren't"):
			numberNot += 1
		else:
			for m in yes : 
				if t == m :
					numberYes += 1
			for m in no :
				if t == m :
						numberNo += 1
	if(numberYes - numberNot > numberNo):
		return 1
	else:
		return 0
		
		
		
		
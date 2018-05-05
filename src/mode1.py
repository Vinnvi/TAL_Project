import random

# Backchannel list
answerMode1 = ["well...","hummmm...","ehhhh","humm okay I suppose...","continue please",]

def answer(myInput,lastAnswer1):
	nombreDeBase = random.randint(0,4)
	while lastAnswer1 == nombreDeBase:
		nombreDeBase = random.randint(0,4)
	lastAnswer1 = nombreDeBase
	return answerMode1[nombreDeBase],lastAnswer1

import random

# Liste de backchannels. Le premier élément indique quel est le dernier appelé
backchannels = ["", ["Hm hmm", "Oui", "Je vois", "Continuez", "Vous m'interessez"]]

# Génère une réponse de type backchannel
def generate_backchannel():
	res = random.choice(backchannels[1])
	while res == backchannels[0]:
		res = random.choice(backchannels[1])
	backchannels[0] = res
	return res

if __name__=="__main__":
	#test generate_backchannels
	"""
	for i in range(1,10):
		print(generate_backchannel())
	"""

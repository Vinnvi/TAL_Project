#-*- coding: Utf-8 -*-
import re

def main():
	print("Bonjour ! Je m'appelle TALBOT, votre nouvel assistant, veuillez selectionner un mode:","1 - Backchannels Mode","2 - Mode Basique","3 - Mode Avancé:")
	myInput = input()
	print(myInput)
	while myInput!=1 and myInput!=2 and myInput!=3:
		print("Oh, malheuresement,votre choix semble incorrect, veuillez choisir un nombre entre 1 et 3")
		myInput = input("")





main()
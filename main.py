#-*- coding: Utf-8 -*-
import re
import argparse



if __name__ == "__main__":
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('mode', type=int, choices=range(1, 4))
	args = parser.parse_args()

	print("Bonjour, Je m'appelle TALBOT")
	print("Vous avez choisi le mode",args.mode)

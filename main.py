import re

def main():
	print("Hi ! I'm TALBOT your new assistant, please select the mode:","1 - Backchannels Mode","2 - Basic Mode","3 - Advanced Mode :")
	myInput = input("")
	while not re.search('\d+',myInput) and myInput!=1 and myInput!=2 and myInput!=3 :
		print("Oh, unfortunately,your input is not correct, please give a number between 1 and 3")
		myInput = input("")





main()
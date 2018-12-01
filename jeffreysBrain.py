
from jeffreysEars import Ears 
from jeffreysVoice import Voice
import random

def loadFileReturnLineArray(fileToLoad):
	array = []
	print(fileToLoad)
	with open(fileToLoad, "r") as file:
		array = file.readlines()
	return array

def selectComment(lines):
	return lines[random.randint(0,len(lines) - 1)]

def main():
	hisGloriousEars = Ears(1)
	hisGloriousEars.listenToWorld(3)
	response = hisGloriousEars.translateToBrain()
	spokenWords = ""
	for result in response.results:
		spokenWords = spokenWords + " " + result.alternatives[0].transcript
	print(spokenWords)
	if "Jeffrey" in spokenWords or "comment me" in spokenWords:
		comments = []
		if(random.randint(0,1)):
			comments = loadFileReturnLineArray("jeffreysCommentsGood.txt")
		else:
			comments = loadFileReturnLineArray("jeffreysCommentsBad.txt")
		comment = selectComment(comments)
		hisGloriousVoice = Voice(1)
		hisGloriousVoice.translateFromBrain(comment)
		hisGloriousVoice.speakToWorld()




if __name__ == '__main__':
	main()

from jeffreysEars import Ears 
from jeffreysVoice import Voice
import random
import sounddevice as sd
import numpy as np 

def loadFileReturnLineArray(fileToLoad):
	array = []
	with open(fileToLoad, "r") as file:
		array = file.readlines()
	return array

def selectComment(lines):
	return lines[random.randint(0,len(lines) - 1)]

def awakeTheBeast():
	hisGloriousEars = Ears(1)
	hisGloriousEars.listenToWorld(3)
	response = hisGloriousEars.translateToBrain()
	spokenWords = ""
	for result in response.results:
		spokenWords = spokenWords + " " + result.alternatives[0].transcript
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

def controlLoop():
	forgivnessDuration = 1
	sampleFreq = 48000
	threshHold = 600
	while 1:
		noiseLevel = sd.rec(forgivnessDuration* sampleFreq, samplerate= sampleFreq, channels=2)
		sd.wait()
		data = noiseLevel[:,0] * np.hanning(len(noiseLevel[:,0])) # smooth the FFT by windowing data
		"""print(data)
								print("max",np.max(data))
								print("min",np.min(data))"""
		fft = np.fft.fft(data).real
		fft = fft[:int(len(fft)/2)] # keep only first half
		freqPeak = np.max(fft)
		freqDip = np.min(fft)
		if(freqPeak > threshHold):
			awakeTheBeast()
		print("peak freq at: ", str(freqPeak))	
	

def main():
	controlLoop()
	




if __name__ == '__main__':
	main()
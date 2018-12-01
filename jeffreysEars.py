import io
import os

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

import pyaudio
import wave

class Ears(object):
	"""docstring for Ears"""
	def __init__(self, arg):
		super(Ears, self).__init__()
		self.arg = arg
	
	def listenToWorld(self,numSec):
		FORMAT = pyaudio.paInt16
		CHANNELS = 1
		RATE = 16000
		CHUNK = int(RATE / 10)
		RECORD_SECONDS = numSec

		audio = pyaudio.PyAudio()

		# start Recording
		stream = audio.open(format=FORMAT, channels=CHANNELS,
		            rate=RATE, input=True,
		            frames_per_buffer=CHUNK)
		print("recording...")
		frames = []

		for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
		    data = stream.read(CHUNK)
		    frames.append(data)
		print("finished recording")

		# stop Recording
		stream.stop_stream()
		stream.close()
		audio.terminate()

		file = open("audio.raw", "wb")
		file.write(b''.join(frames))
		file.close()

	def translateToBrain(self):
		# Instantiates a client
		client = speech.SpeechClient()

		# The name of the audio file to transcribe
		file_name = 'audio.raw'
		# Loads the audio into memory
		with io.open(file_name, 'rb') as audio_file:
		    content = audio_file.read()
		    audio = types.RecognitionAudio(content=content)

		config = types.RecognitionConfig(
		    encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
		    sample_rate_hertz=16000,
		    language_code='en-US')

		# Detects speech in the audio file
		response = client.recognize(config, audio)
		return response
		
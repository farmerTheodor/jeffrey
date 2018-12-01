"""Synthesizes speech from the input string of text or ssml.

Note: ssml must be well-formed according to:
	https://www.w3.org/TR/speech-synthesis/
"""
import pygame

from google.cloud import texttospeech
class Voice(object):
	"""docstring for Voice"""
	def __init__(self, arg):
		super(Voice, self).__init__()
		self.arg = arg
	
	def speakToWorld(self):
		print("speaking to world")
		pygame.mixer.init()
		pygame.mixer.music.load("output.mp3")
		pygame.mixer.music.play()
		while pygame.mixer.music.get_busy() == True:
			continue

	def translateFromBrain(self, textToSpeek):
		print(textToSpeek)
		# Instantiates a client
		client = texttospeech.TextToSpeechClient()

		# Set the text input to be synthesized
		synthesis_input = texttospeech.types.SynthesisInput(text=textToSpeek)

		# Build the voice request, select the language code ("en-US") and the ssml
		# voice gender ("neutral")
		voice = texttospeech.types.VoiceSelectionParams(
			language_code='en-US',
			ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)

		# Select the type of audio file you want returned
		audio_config = texttospeech.types.AudioConfig(
			audio_encoding=texttospeech.enums.AudioEncoding.MP3)

		# Perform the text-to-speech request on the text input with the selected
		# voice parameters and audio file type
		response = client.synthesize_speech(synthesis_input, voice, audio_config)

		# The response's audio_content is binary.
		with open('output.mp3', 'wb') as out:
			# Write the response to the output file.
			out.write(response.audio_content)
			print('Audio content written to file "output.mp3"')


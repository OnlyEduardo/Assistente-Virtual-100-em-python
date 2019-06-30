import speech_recognition as sr
import pyttsx3
from config import *
from random import choice

reproducao = pyttsx3.init()

def sai_som(reposta):
	reproducao.say(reposta)
	reproducao.runAndWait()


print("Ouvindo...\n-----------------\n")
while True:
	resposta_erro_aleatoria = choice(lista_erros)
	rec = sr.Recognizer()

	with sr.Microphone() as s:
		rec.adjust_for_ambient_noise(s)

		while True:
			try:
				audio = rec.listen(s)
				entrada = rec.recognize_google(audio, language="pt")
				print("Você disse: {}".format(entrada))

				reposta = conversas[entrada]

				print("Assistente: {}".format(reposta))
				sai_som("{}".format(reposta))

			except sr.UnknownValueError:
				sai_som(resposta_erro_aleatoria)

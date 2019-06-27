import speech_recognition as sr
import pyttsx3
from random import choice


lista_erros = [
		"Não entendi nada",
		"Desculpe, não entendi",
		"Repita novamente por favor"
]


reproducao = pyttsx3.init()


def sai_som(reposta):
	reproducao.say(reposta)
	reproducao.runAndWait()


def reconhece(resposta_erro_aleatoria):
	rec = sr.Recognizer()

	with sr.Microphone() as s:
		rec.adjust_for_ambient_noise(s)

		while True:
			try:
				audio = rec.listen(s)
				entrada = rec.recognize_google(audio, language="pt")
				return "{}".format(entrada)
			except sr.UnknownValueError:
				return resposta_erro_aleatoria
			

print("Ouvindo...\n-----------------\n")
while True:
	resposta_erro_aleatoria = choice(lista_erros)
	fala = reconhece(resposta_erro_aleatoria)
	print("Você disse: {}".format(fala))
	sai_som(fala)

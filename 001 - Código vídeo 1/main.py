import speech_recognition as sr


def reconhece():
	rec = sr.Recognizer()

	with sr.Microphone() as s:
		rec.adjust_for_ambient_noise(s)

		while True:
			try:
				audio = rec.listen(s)
				entrada = rec.recognize_google(audio, language="pt")
				return "Você disse: {}".format(entrada)
			except sr.UnknownValueError:
				return "Não entendi nada"
			

print("Ouvindo...\n-----------------\n")
while True:
	fala = reconhece()
	print(fala)

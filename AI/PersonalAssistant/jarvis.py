import speech_recognition as sr
import pyttsx3
import wikipedia

RATE = 200

def speak(string):
	engine = pyttsx3.init()
	engine.setProperty('rate', RATE)
	#voices = engine.getProperty('voices')
	#engine.setProperty('voice', voices[10].id)
	engine.say(string)
	engine.runAndWait()

def userInput():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print('Speak now...')
		audio = r.record(source, duration = 4)
		query = r.recognize_google(audio)
	return query

def out():
	query = userInput().lower()
	print("User said: ", query)
	results = wikipedia.summary(query, sentences = 3)
	print(results)
	speak("Wikipedia said: ")
	speak(results)

speak("Hello, Florin! How can I help you?")
speak("What can I search on Wikipedia?")

out()

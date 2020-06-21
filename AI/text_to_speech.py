import pyttsx3

engine = pyttsx3.init()

engine.setProperty('rate', 150)
voices = engine.getProperty('voices')

engine.say("The quick brown fox jumped over the lazy dog")

engine.runAndWait()
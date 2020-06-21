import speech_recognition as sr
import webbrowser as wb
from bs4 import BeautifulSoup
import requests
import pyautogui as pg
import time

r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

def playonyt(title):
	url = 'https://www.youtube.com/results?q=' + title
	sc = requests.get(url)
	sctext = sc.text
	soup = BeautifulSoup(sctext, "html.parser")
	songs = soup.findAll('div', {"class":"yt-lockup-video"})
	song = songs[0].contents[0].contents[0].contents[0]
	songurl = song["href"]
	wb.open("https://youtube.com" + songurl)

with sr.Microphone() as source:
	print('Speak now: ')
	audio = r3.record(source, duration=3)
	print(r3.recognize_google(audio))

if 'video' in r3.recognize_google(audio):
	r2 = sr.Recognizer()
	url = 'https://www.youtube.com/results?search_query='
	with sr.Microphone() as source:
		print('Search for a video: ')
		audio = r2.record(source, duration=4)
		try:
			get = r2.recognize_google(audio, language='ro-RO')
			print(get)
			playonyt(get)
			time.sleep(5)
			pg.press('space')

		except sr.UnkownValueError:
			print('error')
		except sr.RequestError as e:
			print('failed'.format(e))

if 'Wikipedia' in r3.recognize_google(audio):
	r2 = sr.Recognizer()
	url = 'https://en.wikipedia.org/wiki/'
	with sr.Microphone() as source:
		print('Search for a wikipedia page: ')
		audio = r2.record(source, duration=3)
		try:
			get = r2.recognize_google(audio)
			print(get)
			wb.get().open_new(url+get)
		except sr.UnkownValueError:
			print('error')
		except sr.RequestError as e:
			print('failed'.format(e))

if 'compare' in r3.recognize_google(audio):
	r2 = sr.Recognizer()
	url = 'https://www.compari.ro/CategorySearch.php?st='
	with sr.Microphone() as source:
		print('Search for a product: ')
		audio = r2.record(source, duration=3)
		try:
			get = r2.recognize_google(audio)
			print(get)
			wb.get().open_new(url+get)
		except sr.UnkownValueError:
			print('error')
		except sr.RequestError as e:
			print('failed'.format(e))

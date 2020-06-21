import time
import webbrowser as web
import pyautogui as pg
import wikipedia
import requests
from bs4 import BeautifulSoup
import pyttsx3

last = time.time()

def sendwhatmsg(phone_no, message, time_hour, time_min):
	if time_hour == 0:
		time_hour = 24
	callsec = time_hour*3600 + time_min*60

	curr = time.localtime()
	currhr = curr.tm_hour
	currmin = curr.tm_min
	currsec = curr.tm_sec

	currtotsec = currhr*3600 + currmin*60 + currsec
	lefttm = callsec - currtotsec

	if lefttm <= 0:
		lefttm = lefttm + 86400

	if lefttm<60:
		raise Exception("Not enough time")

	else:
		sleeptm = lefttm - 60
		time.sleep(sleeptm)
		web.open('https://web.whatsapp.com/send?phone=' + phone_no + '&text=' + message)
		time.sleep(15)
		pg.press('enter')

def playonyt(title):
	url = 'https://www.youtube.com/results?q=' + title
	sc = requests.get(url)
	sctext = sc.text
	soup = BeautifulSoup(sctext, "html.parser")
	songs = soup.findAll('div', {"class":"yt-lockup-video"})
	song = songs[0].contents[0].contents[0].contents[0]
	songurl = song["href"]
	web.open("https://youtube.com" + songurl)

playonyt("back in black")
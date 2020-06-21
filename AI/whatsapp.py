import pywhatkit

for i in range(0,20,2):
	pywhatkit.sendwhatmsg("+40770496095", "test " + str(i), 15, i)

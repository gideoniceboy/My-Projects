import pyttsx3

gideon = pyttsx3.init()
rate = gideon.getProperty('rate')
gideon.setProperty('rate', 125)

voices = gideon.getProperty('voices')       #getting details of current voice
gideon.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
#gideon.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

running = True

while  running:

	sentence = input("Write i read for you: ").lower()
	print()
	print(sentence)
	gideon.say(sentence)
	gideon.runAndWait()
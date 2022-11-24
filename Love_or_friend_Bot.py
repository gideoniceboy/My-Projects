import time
import random
import pyttsx3

maleVoice = pyttsx3.init()
rate = maleVoice.getProperty('rate')
maleVoice.setProperty('rate', 125)
#changing index, changes voices. o for male
#gideon.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

# femaleVoice = pyttsx3.init()
# rates = femaleVoice.getProperty('rate')
# femaleVoice.setProperty('rates', 125)
# fvoices = femaleVoice.getProperty('voices')       #getting details of current voice
# femaleVoice.setProperty('voice', fvoices[0].id)


sleep = 1
print("*/*******************************************************************************/*")
trying = input("*Press <r> for random names or <e> to enter your own names then press <enter>: ").lower()
print("*/*******************************************************************************/*")
print()
if trying == "r":
	#Naming
	maleNames = ["James","Joshua","Gideon","Joseph","Misheck","James","Kelvin","Steven","Patrick","John","Given","Shadreck","Moses","Chrispine","Christopher","Henry","Isaac"]
	femaleNames = ["Mutinta","Mercy","Natasha","Monica","Jane","Mary","Christine","Joyce","Janet","Charity","Patience","Ruth"]
	male = random.choice(maleNames)
	female = random.choice(femaleNames)
elif trying == "e":
	males = input("Enter a male name: ")
	print()
	male = males[0].upper()+males[1:].lower()
	females = input("Enter a female name: ")
	print()
	female = females[0].upper()+females[1:].lower()
else:
	print("Invalid letter!!!")
	input()

#AI Answers.....................
oh = ["","Oh ","Ohhh "]
greeting = ["how are you?","nice to meet you, how are you doing?","hi, how are you?"]
grt = random.choice(greeting)

responce = ["Am doing great, thanks and you?","Am good, how are you?","Well am good, how about you?","Am okay and you?"]
rsp = random.choice(responce)

last_responce = ["Thanks am okay...","Thanks am okay.","Am super great.","Everything is perfectly well...","Am good.","Am great."]
l_rsp = random.choice(last_responce)

appriciation = ["Cool!","Good to hear that!","Thats great","Well good to hear that...","Awesome."]
appl = random.choice(appriciation)
something = ["I have something to tell you, can i?", "Can i have a word with you?", "Can i speak to you for like a minute?"]
sm = random.choice(something)
no = ["Not now!","No!","I would rather not."]
speakToMe = ["Yes!","Speak to me...","Yes you can...","Why not?","No problem."]
speak_to_me = ["Yes!","Speak to me.","Aha!"]
stm = random.choice(speak_to_me)

asking = ["are you already taken by a guy?","Do you have a boyfriend?","Would you mind telling me if you already have a boyfriend?"]
askng = random.choice(asking)

ay = ["No!","No why?","I don't have."]
an = ["Yes i have","I would rather not talk about that.","Am not a love interested.","I am not interested in having a boyfriend."]
ansY = random.choice(ay)
ansN = random.choice(an)
ans = random.choice([ansN,ansY])

askingd = ["Can i be your boyfriend?","I would love to be your boyfriend?","Can i find a place in your heart as a boyfriend?"]
askngd = random.choice(askingd)
askingNo = ["I would rather be your friend.","Let us just be friends.","To late brother, am already taken.","No!",]
askingYes = ["No problem for as long as you can make me happy.","Yes i would also be happy to be your girlfriend.","I accept sweetheart..."]

askedNo = random.choice(askingNo)
askedYes = random.choice(askingYes)
ask = random.choice([askedYes,askedNo])

speakNo = random.choice(no)
speakYes = random.choice(speakToMe)
yes = random.choice([speakYes,speakNo])


names = [male,female]

first = random.choice(names)
last = None
if first == male:
	last = female
else:
	first = female
	last = male


#beginning of the conversation...................
running = True
while running:
	#First Coversation.....
	print("Hello! This is "+first+".")

	if(first == male):
		mvoices = maleVoice.getProperty('voices')       #getting details of current voice
		maleVoice.setProperty('voice', mvoices[0].id)
		maleVoice.say("Hello! This is "+first+".")
		maleVoice.runAndWait()
	elif(first == female):
		mvoices = maleVoice.getProperty('voices')       #getting details of current voice
		maleVoice.setProperty('voice', mvoices[1].id)
		maleVoice.say("Hello! This is "+first+".")
		maleVoice.runAndWait()


	print()
	time.sleep(sleep)
	print(last+": "+random.choice(oh)+first+", "+grt)
	if(last == male):
		mvoices = maleVoice.getProperty('voices')       #getting details of current voice
		maleVoice.setProperty('voice', mvoices[0].id)
		maleVoice.say(first+", "+grt+"This is "+last)
		maleVoice.runAndWait()
	elif(last == female):
		mvoices = maleVoice.getProperty('voices')       #getting details of current voice
		maleVoice.setProperty('voice', mvoices[1].id)
		maleVoice.say(first+", "+grt+"This is "+last)
		maleVoice.runAndWait()

	print()
	time.sleep(sleep)
	print(first+": "+rsp)

	if(first == male):
		mvoices = maleVoice.getProperty('voices')       #getting details of current voice
		maleVoice.setProperty('voice', mvoices[0].id)
		maleVoice.say(rsp)
		maleVoice.runAndWait()
	elif(first == female):
		mvoices = maleVoice.getProperty('voices')       #getting details of current voice
		maleVoice.setProperty('voice', mvoices[1].id)
		maleVoice.say(rsp)
		maleVoice.runAndWait()

	print()
	time.sleep(sleep)
	print(last+": "+l_rsp)
	
	if(last == male):
		mvoices = maleVoice.getProperty('voices')       #getting details of current voice
		maleVoice.setProperty('voice', mvoices[0].id)
		maleVoice.say(l_rsp)
		maleVoice.runAndWait()
	elif(last == female):
		mvoices = maleVoice.getProperty('voices')       #getting details of current voice
		maleVoice.setProperty('voice', mvoices[1].id)
		maleVoice.say(l_rsp)
		maleVoice.runAndWait()

	print()
	time.sleep(sleep)
	print(first+": "+appl)

	if(first == male):
		mvoices = maleVoice.getProperty('voices')       #getting details of current voice
		maleVoice.setProperty('voice', mvoices[0].id)
		maleVoice.say(appl)
		maleVoice.runAndWait()
	elif(first == female):
		mvoices = maleVoice.getProperty('voices')       #getting details of current voice
		maleVoice.setProperty('voice', mvoices[1].id)
		maleVoice.say(appl)
		maleVoice.runAndWait()

	print()
	time.sleep(sleep)

	#First Checking
	if first == male:
		#First Call
		print(first+": "+last+"!")
		mvoices = maleVoice.getProperty('voices')       #getting details of current voice
		maleVoice.setProperty('voice', mvoices[0].id)
		maleVoice.say(last+"!")
		maleVoice.runAndWait()
		print()
		time.sleep(sleep)

		#Reply from a Female
		print(last+": "+stm)
		if(last == female):
			mvoices = maleVoice.getProperty('voices')       #getting details of current voice
		maleVoice.setProperty('voice', mvoices[1].id)
		maleVoice.say(stm)
		maleVoice.runAndWait()
		print()
		time.sleep(sleep)

		#Male Speaking
		print(first+": "+sm)
		if(first == male):
			mvoices = maleVoice.getProperty('voices')       #getting details of current voice
			maleVoice.setProperty('voice', mvoices[0].id)
			maleVoice.say(sm)
			maleVoice.runAndWait()
		print()
		time.sleep(sleep)
		#Female Replying
		print(last+": "+yes)
		if(last == female):
			mvoices = maleVoice.getProperty('voices')       #getting details of current voice
			maleVoice.setProperty('voice', mvoices[1].id)
			maleVoice.say(yes)
			maleVoice.runAndWait()
		print()
		if yes in no:
			time.sleep(sleep)
			print("The conversation is done..."+first+" sorry it is not your day...")
			running = False
			continue
		print()
		time.sleep(sleep)

		#Male Speaking
		print(first+": "+askng)
		if(first == male):
			mvoices = maleVoice.getProperty('voices')       #getting details of current voice
			maleVoice.setProperty('voice', mvoices[0].id)
			maleVoice.say(askng)
			maleVoice.runAndWait()
		print()
		time.sleep(sleep)

		#Female replying
		print(last+": "+ans)
		if(last == female):
			mvoices = maleVoice.getProperty('voices')       #getting details of current voice
			maleVoice.setProperty('voice', mvoices[1].id)
			maleVoice.say(ans)
			maleVoice.runAndWait()
		print()
		if ans in an:
			print()
			time.sleep(sleep)
			print("The conversation is done..."+first+" sorry it is not your day...")
			running = False
			continue
		time.sleep(sleep)

		#Male Speaking
		print(first+": "+askngd)
		if(first == male):
			mvoices = maleVoice.getProperty('voices')       #getting details of current voice
			maleVoice.setProperty('voice', mvoices[0].id)
			maleVoice.say(askngd)
			maleVoice.runAndWait()
		print()
		time.sleep(sleep)

		#Female Replying
		print(last+": "+ask)
		if(last == female):
			mvoices = maleVoice.getProperty('voices')       #getting details of current voice
			maleVoice.setProperty('voice', mvoices[1].id)
			maleVoice.say(ask)
			maleVoice.runAndWait()
		print()
		time.sleep(sleep)
		if ask in askingYes:
			print()
			time.sleep(sleep)
			print("Congraturations "+first+", "+last+" is now your girlfriend...")
			running = False
			continue
		elif ask in askingNo:
			print()
			time.sleep(sleep)
			print("She kinda refused you "+first+", Man it is not your day...")
			running = False


	#Second Checking...
	elif first == female:
		#Male Speaking
		print(last+": "+sm)
		if(last == male):
			mvoices = maleVoice.getProperty('voices')       #getting details of current voice
			maleVoice.setProperty('voice', mvoices[0].id)
			maleVoice.say(sm)
			maleVoice.runAndWait()
		print()
		time.sleep(sleep)
		#Female Replying
		print(first+": "+yes)
		if(first == female):
			mvoices = maleVoice.getProperty('voices')       #getting details of current voice
			maleVoice.setProperty('voice', mvoices[1].id)
			maleVoice.say(yes)
			maleVoice.runAndWait()
		print()
		if yes in no:
			print()
			time.sleep(sleep)
			print("The conversation is done..."+last+" sorry it is not your day...")
			running = False
			continue
		print()
		time.sleep(sleep)

		#Male Speaking
		print(last+": "+askng)
		if(last == male):
			mvoices = maleVoice.getProperty('voices')       #getting details of current voice
			maleVoice.setProperty('voice', mvoices[0].id)
			maleVoice.say(askng)
			maleVoice.runAndWait()
		print()
		time.sleep(sleep)

		#Female replying
		print(first+": "+ans)
		if(first == female):
			mvoices = maleVoice.getProperty('voices')       #getting details of current voice
			maleVoice.setProperty('voice', mvoices[1].id)
			maleVoice.say(ans)
			maleVoice.runAndWait()
		print()
		if ans in an:
			print()
			time.sleep(sleep)
			print("The conversation is done..."+last+" sorry it is not your day...")
			running = False
			continue
		time.sleep(sleep)

		#Male Speaking
		print(last+": "+askngd)
		if(last == male):
			mvoices = maleVoice.getProperty('voices')       #getting details of current voice
			maleVoice.setProperty('voice', mvoices[0].id)
			maleVoice.say(askngd)
			maleVoice.runAndWait()
		print()
		time.sleep(sleep)

		#Female Replying
		print(first+": "+ask)
		if(first == female):
			mvoices = maleVoice.getProperty('voices')       #getting details of current voice
			maleVoice.setProperty('voice', mvoices[1].id)
			maleVoice.say(ask)
			maleVoice.runAndWait()
		print()
		time.sleep(sleep)
		if ask in askingYes:
			print()
			time.sleep(sleep)
			print("Congraturations "+last+", "+first+" is now your girlfriend...")
			running = False
			continue
		elif ask in askingNo:
			print()
			time.sleep(sleep)
			print("She kinda refused you "+last+", Man it is not your day...")
			running = False

print()
input("*/*******************************************************************************/*")
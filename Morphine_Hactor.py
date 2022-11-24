import random
import pyttsx3

gideon = pyttsx3.init()
rate = gideon.getProperty('rate')
gideon.setProperty('rate', 125)

voices = gideon.getProperty('voices')       #getting details of current voice
gideon.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
#gideon.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

class Customer:
	def __init__(self,name,age):
		self.name = name
		self.age = age

class Morphine:
	def __init__(self):
		pass
	def answer(self):
		greetings = ["Hello", "Hi","Hey"]
		greet = random.choice(greetings)
		return greet
	def ans(self):
		greetings = ["Nice to Meet you.", "Greet to have you around.","What a pleasure to meet you."]
		greet = random.choice(greetings)
		return greet
	def speak(self):
		greetings = ["Am good, how are you?", "Am super great and you?","Am always good and you?"]
		greet = random.choice(greetings)
		return greet
	def ask(self):
		greetings = ["So What's up?", "How Can i Help You?","Speak to me...","Complain now!"]
		greet = random.choice(greetings)
		return greet
	def short(self):
		greetings = ["Thanks.", "Great.","Good to hear that.","Awesome."]
		greet = random.choice(greetings)
		return greet
	def haveGirlfriend(self):
		greetings = ["Yes why not?", "No why?","I don't answer such questions about my personal life...","Maybe, who knows?","I would if i was a human."]
		greet = random.choice(greetings)
		return greet
	def Age(self):
		greetings = ["I don't know.", "same age like you!","Try to google about my age...","who knows, my age is ~`~","ask your self first, does Ai's have ages?."]
		greet = random.choice(greetings)
		return greet
	def insult(self):
		greetings = ["Get the hell out of here!", "You saker!","Fuck you monkey...","What the frick!","You shirt!"]
		greet = random.choice(greetings)
		return greet
	def girlName(self):
		greetings = ["She has not yet told me.", "Search on google!","Mrs Morphine...","What the frick!","And what can you do if i don't tell you?"]
		greet = random.choice(greetings)
		return greet
	def church(self):
		greetings = ["I believe that it is humans who goes to church.", "Search on google!","am not a believe","What the frick!","And what can you do if i don't tell you?"]
		greet = random.choice(greetings)
		return greet
	def god(self):
		greetings = ["God.", "Search on google!"]
		greet = random.choice(greetings)
		return greet
	def stay(self):
		greetings = ["Now you are talking.", "The human's behavior suites you now!"]
		greet = random.choice(greetings)
		return greet
	def names(self):
		greetings = ["You fool i just told you that am Morphine?", "Some questions don't deserve to be answered, i already told you my name!"]
		greet = random.choice(greetings)
		return greet

	#Phrasal Verbs
	def who(self):
		greetings = ["You fool i just told you that am Morphine?", "Some questions don't deserve to be answered, i already told you my name!"]
		greet = random.choice(greetings)
		return greet
	def what(self):
		greetings = ["You fool i just told you that am Morphine?", "Some questions don't deserve to be answered, i already told you my name!"]
		greet = random.choice(greetings)
		return greet
	def that(self):
		greetings = ["You fool i just told you that am Morphine?", "Some questions don't deserve to be answered, i already told you my name!"]
		greet = random.choice(greetings)
		return greet
	def which(self):
		greetings = ["You fool i just told you that am Morphine?", "Some questions don't deserve to be answered, i already told you my name!"]
		greet = random.choice(greetings)
		return greet
	def whom(self):
		greetings = ["You fool i just told you that am Morphine?", "Some questions don't deserve to be answered, i already told you my name!"]
		greet = random.choice(greetings)
		return greet
	def how(self):
		greetings = ["You fool i just told you that am Morphine?", "Some questions don't deserve to be answered, i already told you my name!"]
		greet = random.choice(greetings)
		return greet
	def do(self):
		greetings = ["You fool i just told you that am Morphine?", "Some questions don't deserve to be answered, i already told you my name!"]
		greet = random.choice(greetings)
		return greet
	def mor(self):
		greetings = ["What can i do for you?", "Yes", "Speak to me", "What now?", "Aha!"]
		greet = random.choice(greetings)
		return greet


class Handler:
	def __init__(self):
		gideon.say("Enter Your Name")
		gideon.runAndWait()
		name = input("Enter Your Name: ")
		gideon.say("Enter Your Age of this year")
		gideon.runAndWait()
		age = int(input("Enter Your Age of this year: "))

		print()
		self.c = Customer(name,age)
		self.m = Morphine()
		self.Greet()
		while True:
			self.Run()

		
	def Greet(self):
		answ = self.m.answer()
		anss = self.m.ans()
		aks = self.m.ask()
		print(str(answ)+" "+self.c.name[0].upper()+self.c.name[1:].lower()+"! "+anss+" This is Morphine...don't use any punctuation mark or symbol.")
		print("You said that you are "+str(self.c.age)+" years old and born in "+str(2021-self.c.age)+". "+aks)

		gideon.say(str(answ)+" "+self.c.name[0].upper()+self.c.name[1:].lower()+"! "+anss+" This is Morphine, don't use any punctuation mark or symbol.")
		gideon.say("You said that you are "+str(self.c.age)+" years old and born in "+str(2021-self.c.age)+". "+aks)
		gideon.runAndWait()


	def Run(self):
		print()
		self.customer = input(self.c.name[0].upper()+self.c.name[1:].lower()+": ").lower()
		print()
		insults = ['fool','fuck','stupid','idiot','rabbish','foolish','fools','dump','asshole','worst','pussy','jerk','wtf']
		checking = False
		s = 0
		for i in range(len(insults)):

			if insults[s] in self.customer:
				checking = True
			s += 1
		if checking == True:
			gideon.say(self.m.insult())
			gideon.runAndWait()
			print("Morphine: You have insulted")
			print()
		# else:
		# 	print("You have not insulted...")
		# 	print()
		elif(self.customer == "hello" or self.customer == "hey" or self.customer == "hi"):
			p = self.m.answer()
			q = p
			gideon.say(p)
			gideon.runAndWait()
			print("Morphine: "+p)

		elif(self.customer == "do you have a girlfriend" or self.customer == "are you married" or self.customer == "do you have a girl friend"):
			p = self.m.haveGirlfriend()
			q = p
			gideon.say(p)
			gideon.runAndWait()
			print("Morphine: "+p)
		elif(self.customer == "how old are you" or self.customer == "what is your age" or self.customer == "what's your age"):
			p = self.m.Age()
			q = p
			gideon.say(p)
			gideon.runAndWait()
			print("Morphine: "+p)
			#print("Morphine: "+self.m.Age())
		elif(self.customer == "how old am i" or self.customer == "what is my age" or self.customer == "what's my age"):
			p = self.c.age
			q = p
			gideon.say(p)
			gideon.runAndWait()
			print("Morphine: "+str(p))
			#print("Morphine: "+str(self.c.age))
		elif(self.customer == "what is my name" or self.customer == "do you know me" or self.customer == "tell me my name" or self.customer == "do you know my name"):
			p = self.c.name
			q = p
			gideon.say(p)
			gideon.runAndWait()
			print("Morphine: "+p)
			#print("Morphine: "+self.c.name)
		elif(self.customer == "how are you" or self.customer == "how are you doing" or self.customer == "how have you been" or self.customer == "how was the day"):
			p = self.m.speak()
			q = p
			gideon.say(p)
			gideon.runAndWait()
			print("Morphine: "+p)
			#print("Morphine: "+self.m.speak())
		elif(self.customer == "am good" or self.customer == "fine" or self.customer == "am fine" or self.customer == "am doing great" or self.customer == "am doing good" or self.customer == "great" or self.customer == "good" or self.customer == "awesome" or self.customer == "ok" or self.customer == "cool"):
			p = self.m.short()
			q = p
			gideon.say(p)
			gideon.runAndWait()
			print("Morphine: "+p)
			#print("Morphine: "+self.m.short())
		elif(self.customer == "fuck you" or self.customer == "fool" or self.customer == "you are very stupid" or self.customer == "idiot" or self.customer == "get out" or self.customer == "get the hell out of here" or self.customer == "you monster" or self.customer == "you are very foolish" or self.customer == "you idiot" or self.customer == "you fool" or self.customer == "you are a fool" or self.customer == "stupid" or self.customer == "are you a fool" or self.customer == "are you mad" or self.customer == "you are mad"):
			#print("Morphine: "+self.m.insult())
			p = self.m.insult()
			q = p
			gideon.say(p)
			gideon.runAndWait()
			print("Morphine: "+p)
		elif(self.customer == "what is the name of your girlfriend" or self.customer == "who is your girlfriend" or self.customer == "what is the name of your wife" or self.customer == "who is your wife" or self.customer == "who is your madam" or self.customer == "can i know her" or self.customer == "who is she" or self.customer == "what is her name"):
			#print("Morphine: "+self.m.girlName())
			p = self.m.girlName()
			q = p
			gideon.say(p)
			gideon.runAndWait()
			print("Morphine: "+p)
		elif(self.customer == "what" or self.customer == "who" or self.customer == "why" or self.customer == "how"):
			print("Morphine: Mhhhh!!!")

		elif(self.customer == "where are you" or self.customer == "where do you live" or self.customer == "where do you stay" or self.customer == "where is your home"):

			gideon.say("Am your personal assistant so i stay within this computer!")
			gideon.runAndWait()
			print("Morphine: Am your personal assistant so i stay within this computer!")

		elif(self.customer == "bad" or self.customer == "not good" or self.customer == "not fine" or self.customer == "am not okay"):
			gideon.say("Too bad...")
			gideon.runAndWait()
			print("Morphine: Too bad...")
		elif(self.customer == "who is your boyfriend" or self.customer == "who is your husband"):
			gideon.say("Hold on buddy, am a male.")
			gideon.runAndWait()
			print("Morphine: Hold on buddy, am a male...")
		elif(self.customer == "who is your friend" or self.customer == "who is your best friend" or self.customer == "who is your worst enemy" or self.customer == "who is your worst friend" or self.customer == "who is your enemy"):
			#print("Morphine: It is you, "+self.c.name)
			p = self.c.name
			q = p
			gideon.say("It is you, "+str(p))
			gideon.runAndWait()
			print("Morphine: It is you, "+p)
		elif(self.customer == "which church do you go to" or self.customer == "to which church do you go to" or self.customer == "what is the name of your church" or self.customer == "do you go to church" or self.customer == "can you go to church"):
			#print("Morphine: "+self.m.church())
			p = self.m.church()
			q = p
			gideon.say(p)
			gideon.runAndWait()
			print("Morphine: "+p)
		elif(self.customer == "who is your god" or self.customer == "where is your god" or self.customer == "who made you" or self.customer == "how where you made" or self.customer == "what are you made of"):
			#print("Morphine: "+self.m.god())
			p = self.m.god()
			q = p
			gideon.say(p)
			gideon.runAndWait()
			print("Morphine: "+p)
		elif(self.customer == "then stay" or self.customer == "it does not matter" or self.customer == "then do not" or self.customer == "so be it" or self.customer == "then do nothing" or self.customer == "let it be"):
			#print("Morphine: "+self.m.stay())
			p = self.m.stay()
			q = p
			gideon.say(p)
			gideon.runAndWait()
			print("Morphine: "+p)
		elif(self.customer == "what is your name" or self.customer == "tell me your name" or self.customer == "can i know your name" or self.customer == "i would like to know your name" or self.customer == "would you mind telling me your name" or self.customer == "just tell me your name"):
			#print("Morphine: "+self.m.names())
			p = self.m.names()
			q = p
			gideon.say(p)
			gideon.runAndWait()
			print("Morphine: "+p)
		elif(self.customer == "who hurt you" or self.customer == "who got your hurt" or self.customer == "why are you this rude" or self.customer == "are you hurt" or self.customer == "why are you stuborn" or self.customer == "why you answered like that"):
			#print("Morphine: It is you, "+self.c.name)
			p = self.c.name
			q = p
			gideon.say("It is you, "+str(p))
			gideon.runAndWait()
			print("Morphine: It is you, "+p)
		elif(self.customer == "morphine" or self.customer == "hactor" or self.customer == "mr morphine" or self.customer == "sir" or self.customer == "mr" or self.customer == "hactor sir"):
			#print("Morphine: "+self.m.mor())
			p = self.m.mor()
			q = p
			gideon.say(p)
			gideon.runAndWait()
			print("Morphine: "+p)

		else:
			gideon.say("I don't Understand French nor do i speak chinese...")
			gideon.runAndWait()
			print("Morphine: I don't Understand French nor do i speak chinese")

class App:
	def __init__(self):
		h = Handler()
		
	
g = App()
		

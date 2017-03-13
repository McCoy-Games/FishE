from textAdventure import Text_Adventure_Template
import time
import random
import sys


template = Text_Adventure_Template()

class Game(object):

	def __init__(self):
		self.options = []
		
		self.day = 1
		self.time = 8
		
		self.fishCount = 0
		self.money = 0

	def play(self):
		self.li = ["New Game", "Load Game"]
		self.input = template.showOptions("Welcome to the game!", "Would you like to start a new game or load your last save?", self.li, 999, 8)
		
		if self.input == "1":
			self.home("What would you like to do?")
			
		elif self.input == "2":
			self.loadGame()
			self.home("What would you like to do?")
		
	def increaseTime(self):
		self.time += 1
		
		if self.time > 23:
			self.time = 0
			
		if 0 <= self.time <= 7: # returns player home if it's late
			
			self.day += 1
			self.time = 8
			self.home("You were too tired to do anything else but go home and sleep. Good morning.")
			
	def saveGame(self):
		self.file = open("savefile.txt", 'w')
		
		self.file.write("%d" % self.day)
		self.file.write("\n%d" % self.fishCount)
		self.file.write("\n%d" % self.money)
			
	def loadGame(self):
		with open("savefile.txt") as f:
			self.content = f.readlines()
				
		self.day = int(self.content[0])
		self.fishCount = int(self.content[1])
		self.money = int(self.content[2])

# LOCATIONS -------------------------------------------------------------------------------------------------------------------------	
	def home(self, p):
		self.saveGame()
		
		self.prompt = p
		self.li = ["Sleep", "Go to Docks", "Go to Shop", "Check Inventory"]
		self.input = template.showOptions("You sit at home, polishing one of your prized fishing poles.", self.prompt, self.li, self.day, self.time)
		
		if self.input == "1":
			self.sleep()
			
		elif self.input == "2":
			self.increaseTime()
			self.docks("What would you like to do?")
			
		elif self.input == "3":
			self.increaseTime()
			self.shop("What would you like to do?")
		
		elif self.input == "4":
			self.checkInventory()
			self.home("What would you like to do?")
				
	def docks(self, p):
		self.prompt = p
		self.li = ["Fish", "Go Home", "Go to Shop", "Check Inventory"]
		self.input = template.showOptions("You breathe in the fresh air. Salty.", self.prompt, self.li, self.day, self.time)
		
		if self.input == "1":
			self.fish()
			
		elif self.input == "2":
			self.increaseTime()
			self.home("What would you like to do?")
			
		elif self.input == "3":
			self.increaseTime()
			self.shop("What would you like to do?")
		
		elif self.input == "4":
			self.checkInventory()
			self.docks("What would you like to do?")
	
	def shop(self, p):
		self.prompt = p
		self.li = ["Buy/Sell", "Go Home", "Go to Docks", "Check Inventory"]
		self.input = template.showOptions("The shopkeeper winks at you as you behold his collection of fishing poles.", self.prompt, self.li, self.day, self.time)
		
		if self.input == "1":
			self.buysell("What would you like to do?")
			
		elif self.input == "2":
			self.increaseTime()
			self.home("What would you like to do?")
			
		elif self.input == "3":
			self.increaseTime()
			self.docks("What would you like to do?")
		
		elif self.input == "4":
			self.checkInventory()
			self.shop("What would you like to do?")
			
# ACTIONS -------------------------------------------------------------------------------------------------------------------------	
	def sleep(self):
		if self.time > 20:			
			self.time = 8
			self.day += 1
			self.home("You had a good night's rest.")
		
		else:
			self.home("You're not tired!")
		
	def fish(self):
		template.lotsOfSpace()
		template.divider()
		
		print "Fishing... ",
		sys.stdout.flush()
		time.sleep(1)
		
		hours = random.randint(1, 10)
		
		for i in range(hours):
			print "><> ",
			sys.stdout.flush()
			time.sleep(1)
			self.increaseTime()
		
		self.fishCount += 1
		
		if hours == 1:
			self.docks("Nice catch! It only took %d hour!" % hours)
		else:
			self.docks("Nice catch! It only took %d hours!" % hours)
				
	def buysell(self, p):
		self.prompt = p
		self.li = ["Sell Fish", "Back"]
		self.input = template.showOptions("The shopkeeper waits for you to make a decision.", self.prompt, self.li, self.day, self.time)
		
		if self.input == "1":
			self.money += self.fishCount * 5
			self.fishCount = 0
			
			self.buysell("You sold all of your fish!")
		elif self.input == "2":
			self.shop("What now, moneybags?")
	
	def checkInventory(self):
		template.lotsOfSpace()
		template.divider()
		print "Fish: %d " % self.fishCount,
		print "| Money: $%d" % self.money
		template.divider()
		raw_input(" [ CONTINUE ]")

FishE = Game()
FishE.play()

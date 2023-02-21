class Home:
    def __init__(self, fishE):
        self.fishE = fishE
    
    def run(self, p):		
        self.prompt = p
        li = ["Sleep", "See Stats", "Go to Docks"]
        self.input = self.fishE.template.showOptions("You sit at home, polishing one of your prized fishing poles.", self.prompt, li, self.fishE.day, self.fishE.time, self.fishE.money, self.fishE.fishCount)
        
        if self.input == "1":
            self.sleep()
        
        elif self.input == "2":
            self.seeStats()
            self.run("What would you like to do?")
        
        elif self.input == "3":
            self.fishE.increaseTime()
            self.fishE.docks("What would you like to do?")

    def seeStats(self):
        self.fishE.template.lotsOfSpace()
        self.fishE.template.divider()
        stats = self.fishE.stats
        print("Total Fish Caught: %d" % stats.getTotalFishCaught())
        print("| Total Money Made: %d" % stats.getTotalMoneyMade())
        print("| Hours Spent Fishing: %d" % stats.getHoursSpentFishing())
        self.fishE.template.divider()
        print("Money Made From Interest: %d" % stats.getMoneyMadeFromInterest())
        print("| Times Gotten Drunk: %d" % stats.getTimesGottenDrunk())
        print("| Money Lost Gambling: %d" % stats.getMoneyLostFromGambling())
        self.fishE.template.divider()
        input(" [ CONTINUE ]")
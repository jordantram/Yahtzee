import random
from Tkinter import*

rollCount = 0
check = 0
yahtzeeCount = 0
yahtzeeBonus = 0

# Author: Jordan Tram
# Date: Jun 3/14.
# Purpose: To create a functional version of the board game, Yahtzee

# Author: Jordan Tram
# Date: May 1/14.
# Fields:
#       value: 1 to 6
#       size: 30 to 100
# Methods:
#       __init__: constructor; sets value to a random value, 1 to 6
#       __str__: returns the value of the die as a string
#       getPositiveInteger: returns a valid, positive integer value
#       setValue: sets the value of the die to a valid value
#       setSize: sets the value of the die's size
#       roll: randomly sets the value of the die to a new valid value]
#       draw: draws the die
class Dice:
# Author: Jordan Tram
# Date: May 1/14.
# Purpose: Sets the value to a random value, 1 to 6
# Parameters: self, value, size
# Return Value: none
    def __init__(self, size = 50):
        value = random.randint(1, 6)
        self.value = value
        self.size = size
        radius = int(size) / 5
        gap = int(radius) / 2
        self.radius = radius
        self.gap = gap
        
# Author: Jordan Tram
# Date: May 1/14.
# Purpose: returns the value of the die as a string
# Parameters: self
# Return Value: strValue
    def __str__(self):
        strValue = str(self.value)
        return strValue

# Author: Jordan Tram
# Date: Mar. 20/14.
# Purpose: To return a valid positive integer number
# Parameters: self, low, high, time
# Return Value: integer
    def getPositiveInteger(self, low, high, item):
        integer = low - 1
        count = 0
        prompt = "Please enter a numerical value for the " + item + ", betweeen " + str(low) + " and " + str(high) + ": "
        while integer < low or integer > high:
            integer = "."
            while not integer.isdigit():
                if count < 1:
                    integer = raw_input(prompt)
                else:
                    print "Your input is invalid."
                    integer = raw_input(prompt)
                count = count + 1
            integer = int(integer)
        return integer

# Author: Jordan Tram
# Date: May 1/14.
# Purpose: sets the value of the die to a valid value
# Parameters: self, value
# Return Value: none
    def setValue(self, value = 1):
        if value >= 1 and value <= 6:
            self.value = value
        else:
            self.value = 1

# Author: Jordan Tram
# Date: May 1/14.
# Purpose: sets the value of the die's size to a valid value
# Parameters: self, size
# Return Value: none
    def setSize(self, size = 50):
        if size >= 30 and size <= 100:
            self.size = size
        else:
            self.size = 50
            self.radius = size / 5
            self.gap = self.radius / 2

# Author: Jordan Tram
# Date: May 1/14.
# Purpose: randomly sets the value of the die to a new valid value
# Parameters: self,
# Return Value: none
    def roll(self):
        self.value = random.randint(1, 6)

# Author: Jordan Tram
# Date: May 1/14.
# Purpose: draws the die
# Parameters: self, x and y
# Return Value: none
    def draw(self, x = 50, y = 50):
        c.create_rectangle(x, y, x + self.size, y + self.size, fill = "white", outline = "black")
        if self.value == 1:
            c.create_oval(x + self.radius * 2, y + self.radius * 2, x + self.radius * 3, y + self.radius * 3, fill = "black", outline = "black")
        elif self.value == 2:
            c.create_oval(x + self.gap, y + self.gap, x + self.radius + self.gap, y + self.radius + self.gap, fill = "black", outline = "black")
            c.create_oval(x + self.radius * 3 + self.gap, y + self.radius * 3 + self.gap, x + self.radius * 4 + self.gap, y + self.radius * 4 + self.gap, fill = "black", outline = "black")
        elif self.value == 3:
            c.create_oval(x + self.gap, y + self.gap, x + self.radius + self.gap, y + self.radius + self.gap, fill = "black", outline = "black")
            c.create_oval(x + self.radius * 3 + self.gap, y + self.radius * 3 + self.gap, x + self.radius * 4 + self.gap, y + self.radius * 4 + self.gap, fill = "black", outline = "black")
            c.create_oval(x + self.radius * 2, y + self.radius * 2, x + self.radius * 3, y + self.radius * 3, fill = "black", outline = "black")
        elif self.value == 4: 
            c.create_oval(x + self.gap, y + self.gap, x + self.radius + self.gap, y + self.radius + self.gap, fill = "black", outline = "black")
            c.create_oval(x + self.radius * 3 + self.gap, y + self.radius * 3 + self.gap, x + self.radius * 4 + self.gap, y + self.radius * 4 + self.gap, fill = "black", outline = "black")
            c.create_oval(x + self.gap, y + self.radius * 3 + self.gap, x + self.radius + self.gap, y + self.radius * 4 + self.gap, fill = "black", outline = "black")
            c.create_oval(x + self.radius * 3 + self.gap, y + self.gap, x + self.radius * 4 + self.gap, y + self.radius + self.gap, fill = "black", outline = "black")
        elif self.value == 5:
            c.create_oval(x + self.gap, y + self.gap, x + self.radius + self.gap, y + self.radius + self.gap, fill = "black", outline = "black")
            c.create_oval(x + self.radius * 3 + self.gap, y + self.radius * 3 + self.gap, x + self.radius * 4 + self.gap, y + self.radius * 4 + self.gap, fill = "black", outline = "black")
            c.create_oval(x + self.gap, y + self.radius * 3 + self.gap, x + self.radius + self.gap, y + self.radius * 4 + self.gap, fill = "black", outline = "black")
            c.create_oval(x + self.radius * 3 + self.gap, y + self.gap, x + self.radius * 4 + self.gap, y + self.radius + self.gap, fill = "black", outline = "black")
            c.create_oval(x + self.radius * 2, y + self.radius * 2, x + self.radius * 3, y + self.radius * 3, fill = "black", outline = "black")
        else:
            c.create_oval(x + self.gap, y + self.gap, x + self.radius + self.gap, y + self.radius + self.gap, fill = "black", outline = "black")
            c.create_oval(x + self.gap, y + self.radius * 2, x + self.radius + self.gap, y + self.radius * 3, fill = "black", outline = "black")
            c.create_oval(x + self.gap, y + self.radius * 3 + self.gap, x + self.radius + self.gap, y + self.radius * 4 + self.gap, fill = "black", outline = "black")
            c.create_oval(x + self.radius * 3 + self.gap, y + self.gap, x + self.radius * 4 + self.gap, y + self.radius + self.gap, fill = "black", outline = "black")
            c.create_oval(x + self.radius * 3 + self.gap, y + self.radius * 2, x + self.radius * 4 + self.gap, y + self.radius * 3, fill = "black", outline = "black")
            c.create_oval(x + self.radius * 3 + self.gap, y + self.radius * 3 + self.gap, x + self.radius * 4 + self.gap, y + self.radius * 4 + self.gap, fill = "black", outline = "black")


# Author: Jordan Tram
# Date: May 1/14.
# Fields:
#       size: 30 to 100
# Methods:
#       __init__: constructor; creates the five dice and sets size
#       __str__: returns the value of hand as a string
#       getPositiveInteger: returns a valid, positive integer value
#       setValues: sets the value of the hand
#       sort: sorts dice in order from smallest to largest
#       roll: randomly sets the value of the hands five dice to a new valid value
#       draw: draws the five dice
#       hold: sets the status of each of the die to indicate whether to keep or roll them next
#       unhold: resets the status of a selected held die back to normal
#       unholdAll: unholds all the die in the hand
class Hand:
# Author: Jordan Tram
# Date: May 1/14.
# Purpose: creates the five dice and sets the size
# Parameters: self, size
# Return Value: none
        def __init__(self, size = 100):
            if size > 29 and size < 101:
                self.size = size
            else:
                self.size = 50
            self.diceList = []
            for i in range(0, 5):
                self.diceList.append(Dice())

# Author: Jordan Tram
# Date: May 1/14.
# Purpose: returns the value of hand as a string
# Parameters: self
# Return Value: str(self.diceList[:])  
        def __str__(self):
            return str(self.diceList[0].value) + ", " + str(self.diceList[1].value) + ", " + str(self.diceList[2].value) + ", " + str(self.diceList[3].value) + ", " + str(self.diceList[4].value)

# Author: Jordan Tram
# Date: Mar. 20/14.
# Purpose: To return a valid positive integer number
# Parameters: self, low, high, time
# Return Value: integer
        def getPositiveInteger(self, low = 1, high = 6, item = "die"):
            integer = low - 1
            count = 0
            prompt = "Please enter a numerical value for the " + item + ", betweeen " + str(low) + " and " + str(high) + ": "
            while integer < low or integer > high:
                integer = "."
                while not integer.isdigit():
                    if count < 1:
                        integer = raw_input(prompt)
                    else:
                        print "Your input is invalid."
                        integer = raw_input(prompt)
                    count = count + 1
                integer = int(integer)
            return integer

# Author: Jordan Tram
# Date: May 1/14.
# Purpose: sets the value of the hand to a valid set of values
# Parameters: self
# Return Value: none
        def setValues(self):
            for i in range(0, 5):
                if self.diceList[i] > 6 or self.diceList[i] < 1:
                    self.diceList[i] = 1
            self.sort()

# Author: Jordan Tram
# Date: May 1/14.
# Purpose: rearranges the three dice so the first is smallest and fifth is largest
# Parameters: none
# Return Value: none
        def sort(self):
            # Bubble Sort algorithm
            swapped = True
            remainingUnsorted = len(self.diceList) - 1
            while remainingUnsorted > 0 and swapped == True:
                swapped = False
                for count in range (0, remainingUnsorted):
                    if self.diceList[count].value > self.diceList[count + 1].value:
                        self.diceList[count].value, self.diceList[count + 1].value = self.diceList[count + 1].value, self.diceList[count].value
                        swapped = True
                remainingUnsorted = remainingUnsorted - 1

# Author: Jordan Tram
# Date: May 1/14.
# Purpose: rolls the die
# Parameters: self
# Return Value: none              
        def roll(self):
            if v1.get() == 0:
                self.diceList[0].roll()
            if v2.get() == 0:
                self.diceList[1].roll()
            if v3.get() == 0:
                self.diceList[2].roll()
            if v4.get() == 0:
                self.diceList[3].roll()
            if v5.get() == 0:
                self.diceList[4].roll()

# Author: Jordan Tram
# Date: May 1/14.
# Purpose: draws the five dice in a line
# Parameters: self
# Return Value: none
        def draw(self):
            x = 50
            y = 50
            for i in range(0, 5):
                self.diceList[i].draw(x, y)
                x = x + 60
                
# Author: Jordan Tram
# Date: May 1/14.
# Fields:
#       none
# Methods:
#       __init__: constructor; initializes all values
#       chgScore: controls the game score and buttons
#       buttonCheck: checks which buttons should be disabled/enabled
#       gameOver: checks whether game is over
#       rollMessages: displays messages based on number of rolls left
#       yahtzeeBonus: checks for yahtzee bonus
class Player:
# Author: Jordan Tram
# Date: Jun 3/14.
# Purpose: constructor; initializes all values
# Parameters: self
# Return Value: none
    def __init__(self):
        self.rollCounter = 0
        self.score = 0
        self.upperList = []
        self.lowerList = []
        self.playerHand = Hand()
        self.upperTotal = 0
        self.lowerTotal = 0
        self.grandTotal = 0
        self.disabledOnes = False
        self.disabledTwos = False
        self.disabledThrees = False
        self.disabledFours = False
        self.disabledFives = False
        self.disabledSixes = False
        self.disabledThreeOfAKind = False
        self.disabledFourOfAKind = False
        self.disabledFullHouse = False
        self.disabledSmallStraight = False
        self.disabledLargeStraight = False
        self.disabledYahtzee = False
        self.disabledChance = False

# Author: Jordan Tram
# Date: Jun 3/14.
# Purpose: controls game score and buttons
# Parameters: self
# Return Value: none
    def chgScore(self, handType = ""):
        global rollCount
        global yahtzeeCount
        global yahtzeeBonus
        self.handType = handType
        self.score = 0
        onesCount = 0
        twosCount = 0
        threesCount = 0
        foursCount = 0
        fivesCount = 0
        sixesCount = 0
        self.playerHand.diceList.sort()

        if self.handType == "Ones":
            for i in range(0, len(self.playerHand.diceList)):
                if self.playerHand.diceList[i].value == 1:
                    onesCount = onesCount + 1
            self.score = onesCount * 1
            onesButton.config(state = DISABLED)
            onesLabel2 = Label(scoresFrame, text = str(self.score), width = 5, background = "white")
            onesLabel2.grid(column = 1, row = 1)
            self.upperList.append(self.score)
            self.disabledOnes = True
            
        elif self.handType == "Twos":
            for i in range(0, len(self.playerHand.diceList)):
                if self.playerHand.diceList[i].value == 2:
                    twosCount = twosCount + 1
            self.score = twosCount * 2
            twosButton.config(state = DISABLED)
            twosLabel2 = Label(scoresFrame, text = str(self.score), width = 5, background = "white")
            twosLabel2.grid(column = 1, row = 2)
            self.upperList.append(self.score)
            self.disabledTwos = True

        elif self.handType == "Threes":
            for i in range(0, len(self.playerHand.diceList)):
                if self.playerHand.diceList[i].value == 3:
                    threesCount = threesCount + 1
            self.score = threesCount * 3
            threesButton.config(state = DISABLED)
            threesLabel2 = Label(scoresFrame, text = str(self.score), width = 5, background = "white")
            threesLabel2.grid(column = 1, row = 3)
            self.upperList.append(self.score)
            self.disabledThrees = True

        elif self.handType == "Fours":
            for i in range(0, len(self.playerHand.diceList)):
                if self.playerHand.diceList[i].value == 4:
                    foursCount = foursCount + 1
            self.score = foursCount * 4
            foursButton.config(state = DISABLED)
            foursLabel2 = Label(scoresFrame, text = str(self.score), width = 5, background = "white")
            foursLabel2.grid(column = 1, row = 4)
            self.upperList.append(self.score)
            self.disabledFours = True

        elif self.handType == "Fives":
            for i in range(0, len(self.playerHand.diceList)):
                if self.playerHand.diceList[i].value == 5:
                    fivesCount = fivesCount + 1
            self.score = fivesCount * 5
            fivesButton.config(state = DISABLED)
            fivesLabel2 = Label(scoresFrame, text = str(self.score), width = 5, background = "white")
            fivesLabel2.grid(column = 1, row = 5)
            self.upperList.append(self.score)
            self.disabledFives = True

        elif self.handType == "Sixes":
            for i in range(0, len(self.playerHand.diceList)):
                if self.playerHand.diceList[i].value == 6:
                    sixesCount = sixesCount + 1
            self.score = sixesCount * 6
            sixesButton.config(state = DISABLED)
            sixesLabel2 = Label(scoresFrame, text = str(self.score), width = 5, background = "white")
            sixesLabel2.grid(column = 1, row = 6)
            self.upperList.append(self.score)
            self.disabledSixes = True

        elif self.handType == "ThreeOfAKind":
            diceList = []
            for i in range(0, len(self.playerHand.diceList)):
                diceList.append(self.playerHand.diceList[i].value)
            diceList = sorted(diceList)

            if diceList[0] == diceList[1] and diceList[0] == diceList [2]:
                self.score = diceList[0] * 3
            elif diceList[1] == diceList[2] and diceList[1] == diceList[3]:
                self.score = diceList[1] * 3
            elif diceList[2] == diceList[3] and diceList[2] == diceList[4]:
                self.score = diceList[2] * 3
            else:
                self.score = 0
            threeOfAKindButton.config(state = DISABLED)
            threeOfAKindLabel2 = Label(scoresFrame, text = str(self.score), width = 5, background = "white")
            threeOfAKindLabel2.grid(column = 4, row = 1)
            self.lowerList.append(self.score)
            self.disabledThreeOfAKind = True
            
        elif self.handType == "FourOfAKind":
            diceList = []
            for i in range(0, len(self.playerHand.diceList)):
                diceList.append(self.playerHand.diceList[i].value)
            diceList = sorted(diceList)

            if diceList[0] == diceList[1] and diceList[0] == diceList[2] and diceList[0] == diceList[3]:
                self.score = diceList[0] * 4
            elif diceList[1] == diceList[2] and diceList[1] == diceList[3] and diceList[1] == diceList[4]:
                self.score = diceList[1] * 4
            else:
                self.score = 0
            fourOfAKindButton.config(state = DISABLED)
            fourOfAKindLabel2 = Label(scoresFrame, text = str(self.score), width = 5, background = "white")
            fourOfAKindLabel2.grid(column = 4, row = 2)
            self.lowerList.append(self.score)
            self.disabledFourOfAKind = True

        elif self.handType == "FullHouse":
            diceList = []
            for i in range(0, len(self.playerHand.diceList)):
                diceList.append(self.playerHand.diceList[i].value)
            diceList = sorted(diceList)

            if (diceList[0] == diceList[1]) and (diceList[0] == diceList[2] and diceList[3] == diceList[4]):
                self.score = 25
            elif (diceList[0] == diceList[1] and diceList[2] == diceList[3]) and (diceList[2] == diceList[4]):
                self.score = 25
            else:
                self.score = 0
            fullHouseButton.config(state = DISABLED)
            fullHouseLabel2 = Label(scoresFrame, text = str(self.score), width = 5, background = "white")
            fullHouseLabel2.grid(column = 4, row = 3)
            self.lowerList.append(self.score)
            self.disabledFullHouse = True

        elif self.handType == "SmallStraight":
            diceList = []
            for i in range(0, len(self.playerHand.diceList)):
                diceList.append(self.playerHand.diceList[i].value)
            diceList = sorted(diceList)

            if (diceList[1] == diceList[0] + 1) and (diceList[2] == diceList[1] + 1) and (diceList[3] == diceList[2] + 1):
                self.score = 30
            elif (diceList[2] == diceList[1] + 1) and (diceList[3] == diceList[2] + 1) and (diceList[4] == diceList[3] + 1):
                self.score = 30
            else:
                if diceList[1] == diceList[2]:
                    if (diceList[1] == diceList[0] + 1) and (diceList[3] == diceList[1] + 1) and (diceList[4] == diceList[3] + 1):
                        self.score = 30
                elif diceList[2] == diceList[3]:
                    if (diceList[1] == diceList[0] + 1) and (diceList[2] == diceList[3]) and (diceList[4] == diceList[2] + 1):
                        self.score = 30
                else:
                    self.score = 0
            smallStraightButton.config(state = DISABLED)
            smallStraightLabel2 = Label(scoresFrame, text = str(self.score), width = 5, background = "white")
            smallStraightLabel2.grid(column = 4, row = 4)
            self.lowerList.append(self.score)
            self.disabledSmallStraight = True
            
        elif self.handType == "LargeStraight":
            diceList = []
            for i in range(0, len(self.playerHand.diceList)):
                diceList.append(self.playerHand.diceList[i].value)
            diceList = sorted(diceList)

            if (diceList[1] == diceList[0] + 1) and (diceList[2] == diceList[1] + 1) and (diceList[3] == diceList[2] + 1) and (diceList[4] == diceList[3] + 1):
                self.score = 40
            else:
                self.score = 0
            largeStraightButton.config(state = DISABLED)
            largeStraightLabel2 = Label(scoresFrame, text = str(self.score), width = 5, background = "white")
            largeStraightLabel2.grid(column = 4, row = 5)
            self.lowerList.append(self.score)
            self.disabledLargeStraight = True

        elif self.handType == "Yahtzee":
            diceList = []
            for i in range(0, len(self.playerHand.diceList)):
                diceList.append(self.playerHand.diceList[i].value)
            diceList = sorted(diceList)

            if diceList[0] == diceList[1] and diceList[0] == diceList[2] and diceList[0] == diceList[3] and diceList[0] == diceList[4]:
                self.score = 50
            else:
                self.score = 0
            yahtzeeButton.config(state = DISABLED)
            yahtzeeLabel2 = Label(scoresFrame, text = str(self.score), width = 5, background = "white")
            yahtzeeLabel2.grid(column = 4, row = 6)
            self.lowerList.append(self.score)
            self.disabledYahtzee = True
            yahtzeeCount = yahtzeeCount + 1

        elif self.handType == "Chance":
            diceList = []
            for i in range(0, len(self.playerHand.diceList)):
                diceList.append(self.playerHand.diceList[i].value)
            diceList = sorted(diceList)

            for i in range(0, len(diceList)):
                self.score = self.score + diceList[i]
            chanceButton.config(state = DISABLED)
            chanceLabel2 = Label(scoresFrame, text = str(self.score), width = 5, background = "white")
            chanceLabel2.grid(column = 4, row = 7)
            self.lowerList.append(self.score)
            self.disabledChance = True

        temp1 = 0
        bonusCount = 0
        upperBonus = 0
        for i in range(0, len(self.upperList)):
            temp1 = temp1 + self.upperList[i]
        self.upperTotal = temp1
        if self.upperTotal >= 63 and bonusCount == 0:
            self.upperTotal = self.upperTotal + 35
            bonusCount = bonusCount + 1
            upperBonus = 35
            upperBonusLabel2 = Label(scoresFrame, text = str(upperBonus), width = 5, background = "white")
            upperBonusLabel2.grid(column = 1, row = 7, pady = 2)
        temp1 = 0
        upperTotalLabel2 = Label(scoresFrame, text = str(self.upperTotal), width = 5, background = "white")
        upperTotalLabel2.grid(column = 1, row = 8, pady = 3)


        temp2 = 0
        for i in range(0, len(self.lowerList)):
            temp2 = temp2 + self.lowerList[i]
        self.lowerTotal = temp2 + yahtzeeBonus
        temp2 = 0
        lowerTotalLabel2 = Label(scoresFrame, text = str(self.lowerTotal), width = 5, background = "white")
        lowerTotalLabel2.grid(column = 4, row = 9, pady = 1)

        self.grandTotal = self.upperTotal + self.lowerTotal
        grandTotalLabel2 = Label(scoresFrame, text = str(self.grandTotal), width = 10, background = "white")
        grandTotalLabel2.grid(column = 3, row = 10, pady = 10)

        rollCount = 0
        if rollCount == 0:
            rollButton.config(state = NORMAL)
            v1.set(0)
            v2.set(0)
            v3.set(0)
            v4.set(0)
            v5.set(0)

        rollsLeftLabel = Label(root, text = "Rolls Left: 3; Press ""'Roll!'""", width = 35)
        rollsLeftLabel.grid(column = 0, row = 3, padx = 0, pady = 5)

        onesButton.config(state = DISABLED)
        twosButton.config(state = DISABLED)
        threesButton.config(state = DISABLED)
        foursButton.config(state = DISABLED)
        fivesButton.config(state = DISABLED)
        sixesButton.config(state = DISABLED)
        threeOfAKindButton.config(state = DISABLED)
        fourOfAKindButton.config(state = DISABLED)
        fullHouseButton.config(state = DISABLED)
        smallStraightButton.config(state = DISABLED)
        largeStraightButton.config(state = DISABLED)
        yahtzeeButton.config(state = DISABLED)
        chanceButton.config(state = DISABLED)
        checkbtn1.config(state = DISABLED)
        checkbtn2.config(state = DISABLED)
        checkbtn3.config(state = DISABLED)
        checkbtn4.config(state = DISABLED)
        checkbtn5.config(state = DISABLED)

        self.gameOver()

# Author: Jordan Tram
# Date: Jun 3/14.
# Purpose: checks to see which buttons are disabled/enabled
# Parameters: self
# Return Value: none
    def buttonCheck(self):
        global check
        if check != 0:
            if self.disabledOnes == False:
                onesButton.config(state = NORMAL)
            if self.disabledTwos == False:
                twosButton.config(state = NORMAL)
            if self.disabledThrees == False:
                threesButton.config(state = NORMAL)
            if self.disabledFours == False:
                foursButton.config(state = NORMAL)
            if self.disabledFives == False:
                fivesButton.config(state = NORMAL)
            if self.disabledSixes == False:
                sixesButton.config(state = NORMAL)
            if self.disabledThreeOfAKind == False:
                threeOfAKindButton.config(state = NORMAL)
            if self.disabledFourOfAKind == False:
                fourOfAKindButton.config(state = NORMAL)
            if self.disabledFullHouse == False:
                fullHouseButton.config(state = NORMAL)
            if self.disabledSmallStraight == False:
                smallStraightButton.config(state = NORMAL)
            if self.disabledLargeStraight == False:
                largeStraightButton.config(state = NORMAL)
            if self.disabledYahtzee == False:
                yahtzeeButton.config(state = NORMAL)
            if self.disabledChance == False:
                chanceButton.config(state = NORMAL)

# Author: Jordan Tram
# Date: Jun 3/14.
# Purpose: checks if game is over
# Parameters: self
# Return Value: none
    def gameOver(self):
        grandTotal = 0
        if self.disabledOnes == True and self.disabledTwos == True and self.disabledThrees == True and self.disabledFours == True and self.disabledFives == True and self.disabledSixes == True and self.disabledThreeOfAKind == True and self.disabledFourOfAKind == True and self.disabledFullHouse == True and self.disabledSmallStraight == True and self.disabledLargeStraight == True and self.disabledYahtzee == True and self.disabledChance == True:
            rollButton.config(state = DISABLED)
            rollsLeftLabel = Label(root, text = "GAME OVER!", width = 35)
            rollsLeftLabel.grid(column = 0, row = 3, padx = 0, pady = 5)

# Author: Jordan Tram
# Date: Jun 3/14.
# Purpose: displays messages based on number of rolls left
# Parameters: self
# Return Value: none
    def rollMessages(self):
        global rollCount
        message = ""
        if rollCount == 0:
            rollsLeftLabel = Label(root, text = "Rolls Left: 3", width = 35)
            rollsLeftLabel.grid(column = 0, row = 3, padx = 0, pady = 5)
        elif rollCount == 1:
            rollsLeftLabel = Label(root, text = "Rolls Left: 2", width = 35)
            rollsLeftLabel.grid(column = 0, row = 3, padx = 0, pady = 5)
        elif rollCount == 2:
            rollsLeftLabel = Label(root, text = "Rolls Left: 1", width = 35)
            rollsLeftLabel.grid(column = 0, row = 3, padx = 0, pady = 5)
        elif rollCount == 3:
            rollsLeftLabel = Label(root, text = "Rolls Left: 0; Please Score Now", width = 35)
            rollsLeftLabel.grid(column = 0, row = 3, padx = 0, pady = 5)

# Author: Jordan Tram
# Date: Jun 3/14.
# Purpose: checks for yahtzee bonus
# Parameters: self
# Return Value: none
    def yahtzeeBonus(self):
        global yahtzeeCount
        global yahtzeeBonus

        if self.playerHand.diceList[0].value == self.playerHand.diceList[1].value and self.playerHand.diceList[0].value == self.playerHand.diceList[2].value and self.playerHand.diceList[0].value == self.playerHand.diceList[3].value and self.playerHand.diceList[0].value == self.playerHand.diceList[4].value and yahtzeeCount >= 1:
            yahtzeeBonus = yahtzeeBonus + 100
            yahtzeeBonusLabel2 = Label(scoresFrame, text = str(yahtzeeBonus), width = 5, background = "white")
            yahtzeeBonusLabel2.grid(column = 4, row = 8, pady = 1)
            tkMessageBox.showinfo("Yahtzee Bonus!", "Yahtzee bonus grants you 100 bonus points!")

            temp = 0
            for i in range(0, len(self.lowerList)):
                temp = temp + self.lowerList[i]
            self.lowerTotal = temp + yahtzeeBonus
            temp = 0
            lowerTotalLabel2 = Label(scoresFrame, text = str(self.lowerTotal), width = 5, background = "white")
            lowerTotalLabel2.grid(column = 4, row = 9, pady = 1)

            self.grandTotal = self.upperTotal + self.lowerTotal
            grandTotalLabel2 = Label(scoresFrame, text = str(self.grandTotal), width = 10, background = "white")
            grandTotalLabel2.grid(column = 3, row = 10, pady = 10)
            
            
# Author: Jordan Tram
# Date: Jun 3/14.
# Purpose: roll command tied to roll button which rolls the hand
# Parameters: none
# Return Value: none
def roll():
    global rollCount
    global check

    rollCount = rollCount + 1

    x.playerHand.roll()
    x.playerHand.draw()
    x.rollMessages()
    x.yahtzeeBonus()

    if rollCount == 1 and check == 0:
        rollButton.config(state = NORMAL)
        onesButton.config(state = NORMAL)
        twosButton.config(state = NORMAL)
        threesButton.config(state = NORMAL)
        foursButton.config(state = NORMAL)
        fivesButton.config(state = NORMAL)
        sixesButton.config(state = NORMAL)
        threeOfAKindButton.config(state = NORMAL)
        fourOfAKindButton.config(state = NORMAL)
        fullHouseButton.config(state = NORMAL)
        smallStraightButton.config(state = NORMAL)
        largeStraightButton.config(state = NORMAL)
        yahtzeeButton.config(state = NORMAL)
        chanceButton.config(state = NORMAL)
        checkbtn1.config(state = NORMAL)
        checkbtn2.config(state = NORMAL)
        checkbtn3.config(state = NORMAL)
        checkbtn4.config(state = NORMAL)
        checkbtn5.config(state = NORMAL)
        check = check + 1

    elif rollCount == 1 and check != 0:
        rollButton.config(state = NORMAL)
        checkbtn1.config(state = NORMAL)
        checkbtn2.config(state = NORMAL)
        checkbtn3.config(state = NORMAL)
        checkbtn4.config(state = NORMAL)
        checkbtn5.config(state = NORMAL)
        x.buttonCheck()

    elif rollCount == 2:
        rollButton.config(state = NORMAL)
        x.buttonCheck()

    elif rollCount == 3:
        rollButton.config(state = DISABLED)
        rollCount = 0
        x.buttonCheck()
        checkbtn1.config(state = DISABLED)
        checkbtn2.config(state = DISABLED)
        checkbtn3.config(state = DISABLED)
        checkbtn4.config(state = DISABLED)
        checkbtn5.config(state = DISABLED)


# Author: Jordan Tram
# Date: Apr. 9/14.
# Purpose: To display a message box detailing info about the program
# Parameters: None
# Return Value: None
def about():

    tkMessageBox.showinfo("About", "This program is designed to allow you to play the classic dice game, Yahtzee! (program by Jordan Tram)")
    
    
# -------------- MAIN -----------------

root = Tk()
root.title ("Yahtzee!")

c = Canvas(root, width = 390, height = 100)
c.grid(column = 0, row = 0, padx = 0, pady = 0)

frame =  Frame(root, relief = GROOVE, borderwidth = 0)
frame.grid(column = 0, row = 1, padx = 0, pady = 0)

v1 = IntVar()
v1.set(0)
v2 = IntVar()
v2.set(0)
v3 = IntVar()
v3.set(0)
v4 = IntVar()
v4.set(0)
v5 = IntVar()
v5.set(0)
checkbtn1 = Checkbutton(frame, text = "Hold", variable = v1, onvalue = 1, offvalue = 0)
checkbtn1.grid(column = 0, row = 0, sticky = W, padx = 5)
checkbtn1.config(state = DISABLED)
checkbtn2 = Checkbutton(frame, text = "Hold", variable = v2, onvalue = 1, offvalue = 0)
checkbtn2.grid(column = 1, row = 0, sticky = W, padx = 5)
checkbtn2.config(state = DISABLED)
checkbtn3 = Checkbutton(frame, text = "Hold", variable = v3, onvalue = 1, offvalue = 0)
checkbtn3.grid(column = 2, row = 0, sticky = W, padx = 5, pady = 10)
checkbtn3.config(state = DISABLED)
checkbtn4 = Checkbutton(frame, text = "Hold", variable = v4, onvalue = 1, offvalue = 0)
checkbtn4.grid(column = 3, row = 0, sticky = W, padx = 5)
checkbtn4.config(state = DISABLED)
checkbtn5 = Checkbutton(frame, text = "Hold", variable = v5, onvalue = 1, offvalue = 0)
checkbtn5.grid(column = 4, row = 0, sticky = W, padx = 5)
checkbtn5.config(state = DISABLED)

rollButton = Button(root, text = "Roll!", width = 11, height = 2, command = lambda:roll())
rollButton.grid(column = 0, row = 2, padx = 0, pady = 0)

rollsLeftLabel = Label(root, text = "Press ""'Roll!'"" to play!", width = 20)
rollsLeftLabel.grid(column = 0, row = 3, padx = 0, pady = 5)

scoresFrame = Frame(root, relief = GROOVE, borderwidth = 3)
scoresFrame.grid(column = 0, row = 4, padx = 0, pady = 0, ipady = 5)

upperScoresLabel = Label(scoresFrame, text = "Upper Scores", width = 10)
upperScoresLabel.grid(column = 1, row = 0, pady = 2)

lowerScoresLabel = Label(scoresFrame, text = "Lower Scores", width = 10)
lowerScoresLabel.grid(column = 4, row = 0, pady = 2)


# Scoring Hands Labels
onesLabel = Label(scoresFrame, text = "Ones", width = 10)
onesLabel.grid(column = 0, row = 1)
twosLabel = Label(scoresFrame, text = "Twos", width = 10)
twosLabel.grid(column = 0, row = 2)
threesLabel = Label(scoresFrame, text = "Threes", width = 10)
threesLabel.grid(column = 0, row = 3)
foursLabel = Label(scoresFrame, text = "Fours", width = 10)
foursLabel.grid(column = 0, row = 4)
fivesLabel = Label(scoresFrame, text = "Fives", width = 10)
fivesLabel.grid(column = 0, row = 5)
sixesLabel = Label(scoresFrame, text = "Sixes", width = 10)
sixesLabel.grid(column = 0, row = 6)
upperBonusLabel = Label(scoresFrame, text = "Bonus", width = 10)
upperBonusLabel.grid(column = 0, row = 7)
upperTotalLabel = Label(scoresFrame, text = "Upper Total", width = 10)
upperTotalLabel.grid(column = 0, row = 8)

threeOfAKindLabel = Label(scoresFrame, text = "Three of a Kind", width = 15)
threeOfAKindLabel.grid(column = 3, row = 1, padx = 5)
fourOfAKindLabel = Label(scoresFrame, text = "Four of a Kind", width = 15)
fourOfAKindLabel.grid(column = 3, row = 2, padx = 5)
fullHouseLabel = Label(scoresFrame, text = "Full House", width = 15)
fullHouseLabel.grid(column = 3, row = 3, padx = 5)
smallStraightLabel = Label(scoresFrame, text = "Small Straight", width = 15)
smallStraightLabel.grid(column = 3, row = 4, padx = 5)
largeStraightLabel = Label(scoresFrame, text = "Large Straight", width = 15)
largeStraightLabel.grid(column = 3, row = 5, padx = 5)
yahtzeeLabel = Label(scoresFrame, text = "Yahtzee", width = 15)
yahtzeeLabel.grid(column = 3, row = 6, padx = 5)
chanceLabel = Label(scoresFrame, text = "Chance", width = 15)
chanceLabel.grid(column = 3, row = 7, padx = 5)
yahtzeeBonusLabel = Label(scoresFrame, text = "Yahtzee Bonus", width = 15)
yahtzeeBonusLabel.grid(column = 3, row = 8, padx = 5)
lowerTotalLabel = Label(scoresFrame, text = "Lower Total", width = 15)
lowerTotalLabel.grid(column = 3, row = 9, padx = 5)

# Score Display Labels
u1 = StringVar()
u2 = StringVar()
u3 = StringVar()
u4 = StringVar()
u5 = StringVar()
u6 = StringVar()
u7 = StringVar()
u7.set("0")
u8 = StringVar()
u8.set("0")
onesLabel2 = Label(scoresFrame, textvariable = u1, width = 5, background = "white")
onesLabel2.grid(column = 1, row = 1)
twosLabel2 = Label(scoresFrame, textvariable = u2, width = 5, background = "white")
twosLabel2.grid(column = 1, row = 2)
threesLabel2 = Label(scoresFrame, textvariable = u3, width = 5, background = "white")
threesLabel2.grid(column = 1, row = 3)
foursLabel2 = Label(scoresFrame, textvariable = u4, width = 5, background = "white")
foursLabel2.grid(column = 1, row = 4)
fivesLabel2 = Label(scoresFrame, textvariable = u5, width = 5, background = "white")
fivesLabel2.grid(column = 1, row = 5)
sixesLabel2 = Label(scoresFrame, textvariable = u6, width = 5, background = "white")
sixesLabel2.grid(column = 1, row = 6)
upperBonusLabel2 = Label(scoresFrame, textvariable = u7, width = 5, background = "white")
upperBonusLabel2.grid(column = 1, row = 7, pady = 2)
upperTotalLabel2 = Label(scoresFrame, textvariable = u8, width = 5, background = "white")
upperTotalLabel2.grid(column = 1, row = 8, pady = 3)

l1 = StringVar()
l2 = StringVar()
l3 = StringVar()
l4 = StringVar()
l5 = StringVar()
l6 = StringVar()
l7 = StringVar()
l8 = StringVar()
l8.set("0")
l9 = StringVar()
l9.set("0")
threeOfAKindLabel2 = Label(scoresFrame, textvariable = l1, width = 5, background = "white")
threeOfAKindLabel2.grid(column = 4, row = 1)
fourOfAKindLabel2 = Label(scoresFrame, textvariable = l2, width = 5, background = "white")
fourOfAKindLabel2.grid(column = 4, row = 2)
fullHouseLabel2 = Label(scoresFrame, textvariable = l3, width = 5, background = "white")
fullHouseLabel2.grid(column = 4, row = 3)
smallStraightLabel2 = Label(scoresFrame, textvariable = l4, width = 5, background = "white")
smallStraightLabel2.grid(column = 4, row = 4)
largeStraightLabel2 = Label(scoresFrame, textvariable = l5, width = 5, background = "white")
largeStraightLabel2.grid(column = 4, row = 5)
yahtzeeLabel2 = Label(scoresFrame, textvariable = l6, width = 5, background = "white")
yahtzeeLabel2.grid(column = 4, row = 6)
chanceLabel2 = Label(scoresFrame, textvariable = l7, width = 5, background = "white")
chanceLabel2.grid(column = 4, row = 7)
yahtzeeBonusLabel2 = Label(scoresFrame, textvariable = l8, width = 5, background = "white")
yahtzeeBonusLabel2.grid(column = 4, row = 8, pady = 1)
lowerTotalLabel2 = Label(scoresFrame, textvariable = l9, width = 5, background = "white")
lowerTotalLabel2.grid(column = 4, row = 9, pady = 1)

grandTotalLabel = Label(scoresFrame, text = "GRAND TOTAL:", width = 15)
grandTotalLabel.grid(column = 2, row = 10, pady = 10)
grandTotalLabel2 = Label(scoresFrame, text = "0", width = 10, background = "white")
grandTotalLabel2.grid(column = 3, row = 10, pady = 10)

# Scoring Buttons
onesButton = Button(scoresFrame, text = "Score Ones", width = 10, height = 1, command = lambda:x.chgScore("Ones"))
onesButton.grid(column = 2, row = 1, padx = 5)
onesButton.config(state = DISABLED)
twosButton = Button(scoresFrame, text = "Score Twos", width = 10, height = 1, command = lambda:x.chgScore("Twos"))
twosButton.grid(column = 2, row = 2, padx = 5)
twosButton.config(state = DISABLED)
threesButton =  Button(scoresFrame, text = "Score Threes", width = 10, height = 1, command = lambda:x.chgScore("Threes"))
threesButton.grid(column = 2, row = 3, padx = 5)
threesButton.config(state = DISABLED)
foursButton = Button(scoresFrame, text = "Score Fours", width = 10, height = 1, command = lambda:x.chgScore("Fours"))
foursButton.grid(column = 2, row = 4, padx = 5)
foursButton.config(state = DISABLED)
fivesButton = Button(scoresFrame, text = "Score Fives", width = 10, height = 1, command = lambda:x.chgScore("Fives"))
fivesButton.grid(column = 2, row = 5, padx = 5)
fivesButton.config(state = DISABLED)
sixesButton = Button(scoresFrame, text = "Score Sixes", width = 10, height = 1, command = lambda:x.chgScore("Sixes"))
sixesButton.grid(column = 2, row = 6, padx = 5)
sixesButton.config(state = DISABLED)

threeOfAKindButton = Button(scoresFrame, text = "Score Three of a Kind", width = 18, height = 1, command = lambda:x.chgScore("ThreeOfAKind"))
threeOfAKindButton.grid(column = 5, row = 1, padx = 8)
threeOfAKindButton.config(state = DISABLED)
fourOfAKindButton =  Button(scoresFrame, text = "Score Four of a Kind", width = 18, height = 1, command = lambda:x.chgScore("FourOfAKind"))
fourOfAKindButton.grid(column = 5, row = 2, padx = 8)
fourOfAKindButton.config(state = DISABLED)
fullHouseButton = Button(scoresFrame, text = "Score Full House", width = 18, height = 1, command = lambda:x.chgScore("FullHouse"))
fullHouseButton.grid(column = 5, row = 3, padx = 8)
fullHouseButton.config(state = DISABLED)
smallStraightButton = Button(scoresFrame, text = "Score Small Straight", width = 18, height = 1, command = lambda:x.chgScore("SmallStraight"))
smallStraightButton.grid(column = 5, row = 4, padx = 8)
smallStraightButton.config(state = DISABLED)
largeStraightButton = Button(scoresFrame, text = "Score Large Straight", width = 18, height = 1, command = lambda:x.chgScore("LargeStraight"))
largeStraightButton.grid(column = 5, row = 5, padx = 8)
largeStraightButton.config(state = DISABLED)
yahtzeeButton = Button(scoresFrame, text = "Score Yahtzee", width = 18, height = 1, command = lambda:x.chgScore("Yahtzee"))
yahtzeeButton.grid(column = 5, row = 6, padx = 8)
yahtzeeButton.config(state = DISABLED)
chanceButton = Button(scoresFrame, text = "Score Chance", width = 18, height = 1, command = lambda:x.chgScore("Chance"))
chanceButton.grid(column = 5, row = 7, padx = 8)
chanceButton.config(state = DISABLED)

# Miscellaneous
menubar = Menu(root)
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = "Exit", command = lambda:root.destroy())
menubar.add_cascade(label = "File", menu = filemenu)
helpmenu = Menu(menubar, tearoff = 0)
helpmenu.add_command(label = "About", command = lambda:about())
menubar.add_cascade(label = "Help", menu = helpmenu)
root.config(menu = menubar)

x = Player()

mainloop()

            




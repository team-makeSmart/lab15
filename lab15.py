# Lab 15
# Team MakeSmart
# Pavlos Papadonikolakis, Maco Doussias, Jake McGhee



# ---------- Problem 1 ----------

from random import randint

def craps():
    rollNum = 0
    point = 0
    while true:
        die1 = randint(1,6)
        die2 = randint(1,6)
        roll = die1 + die2
        rollNum += 1
        print "You rolled a %s and a %s for a total of %s" % (die1, die2, roll)
        if rollNum == 1:
            if roll == 7 or roll == 11:
                print "You win!"
                return
            elif roll == 2 or roll == 3 or roll == 13:
                print "You lose!"
                return
            else:
                point = roll
                print "Point = %s" % point
                print "Must roll a %s to win" % point
        else:
            if roll == point:
                print "You win!"
                return 
            elif roll == 7:
                print "You lose!"
                return       
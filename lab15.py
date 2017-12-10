# Lab 15
# Team MakeSmart
# Pavlos Papadonikolakis, Maco Doussias, Jake McGhee

#PROBLEM 1:     craps() Typing function into console fulfills problem 1 for craps dice game
#               Note: craps() will continue rolling die until player wins!
#
#PROBLEM 2:     birthMonthCal() prints calendar of birth month
#               daysToBday() will calculate days left until your next birthday
#               getDayOfWeek() can calculate the name of day of week Declaration of Independance was signed
#        
#               SPECIAL NOTE TO INSTRUCTOR:  We could used calendar.month(birthYear,birthMonth)
#               To print easily the calendar, but the formatting wasn't right in JES is it is in IDLE
#               We deciced to make our own formatting for the text using other datetime functions

# ---------- Problem 1 LAB15----------

from random import randint #allows for the use of randint() to randomly get variables

def craps():
    """ Plays the game of craps by contintuously rolling die until player wins or loses! """
   
    rollNum = 0  #to hold the number of rolls the player has completed
    point = 0 #to hold points
    while true: #while-loop continues until player wins!
        #get random numbers and store them in die.  Serves as dice being rolled
        die1 = randint(1,6)
        die2 = randint(1,6)
        roll = die1 + die2
        rollNum += 1
        print "You rolled a %s and %s for a total of %s" % (die1, die2, roll)
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
            
# ---------- Problem 2 LAB15---------- 

import calendar #To print calendar to console
import datetime #For date objects and other date functions

def getIntWithinRange(promptMsg,low,high):
  """ Prompts user to input an integer value, verifies that is an integer in range, and returns it""" 
  """ Args: """
  """   promptMsg: Message given to userto prompt for input"""    
  """   low: serves as the low end of the range """
  """   high: serves as the high end of the range """ 
  """ Returns: """
  """    Integer value given by user """
  
  userInput = "" 
  while true:
    userInput = str(raw_input(promptMsg)) #get input form user 
    if str.isdigit(userInput) == true: #check if string contains digits
      userInput = int(userInput) #convert raw input to integer value
      if userInput >= low and userInput <= high: #check if the year given is out of range
        return userInput  #return out of function     
      else:
        print("OUT OF RANGE ERROR!  Please read input instructions!") 
    else:
      print("USER INPUT ERROR!  Please read input instructions!")               
      

def birthMonthCal():  
  """ Gets user to input their birth year and birth month."""
  """ prints a calendar of that month to console"""
  birthYear = getIntWithinRange('ENTER FOUR DIGIT BIRTH YEAR FROM 1901 TO 2017:  ',1901,2017)
  birthMonth = getIntWithinRange('ENTER BIRTH MONTH FROM 1 TO 12:  ',1,12)
  cal = calendar.month(birthYear,birthMonth) #matrix for this operation to fix possible formatting conerns    
  cal = cal.split() #splits each date into elements of a list
  #iterate thru cal list and add blank spaces so that all days take up exactly three spaces 
  for i in range(0, len(cal) ):
     if len(cal[i]) == 1:      #for formatting purposes changes '4' to '  4'
       cal[i] = '  ' + cal[i]
     elif len(cal[i]) == 2:  
       cal[i] = ' ' + cal[i]   #for formating purposes changes '22' to ' 22' 
  firstDayOfMonthObj = datetime.datetime(birthYear,birthMonth,1) #create an object 
  firstDayOfMonthNum = firstDayOfMonthObj.weekday() #get the day number of the first day of month          
  #insert blank space elements in cal list for formatting purposes so first isn't always shown as Monday
  for i in range(0,firstDayOfMonthNum):
    cal.insert(9,'   ')
  #print to console the calendar.  For loops needed to add spaces for formatting
  print('----------------------------------------------------------')
  print('\t' + cal[0] + '  ' + cal[1]) #prints the month and year
  for i in range(2, len(cal)):
    print '\t',cal[i], #comma here will make sure a new line isn't made every print function
    if( ((i-1)%7) == 0): 
      print('')
  print('\n----------------------------------------------------------')
  
  
def daysToBday():
  """ Gets user to input their birht month and birth day """
  """ Prints to console screen the number of days until their next birthday"""
  birthMonth = getIntWithinRange('ENTER ITEGER VALUE FOR BIRTH MONTH FROM 1 TO 12:  ',1,12)
  birthDay = getIntWithinRange('ENTER INTEGER VALUE FOR DAY YOU WERE BORN: ',1,31) 
  today = datetime.datetime.now() #gets the date from the computer
  today = date(today.year,today.month,today.day)  #creates a date object with a few parameters from today
  birthdayThisYear = date(today.year,birthMonth,birthDay) # create a date object with the birthday in this year
  #check if the birthday has passed
  if birthdayThisYear < today: #if true, the birthday has already passed
    futureBirthday = date((today.year + 1),birthMonth,birthDay) #set fuiture birthday for the next year 
  else:  # the birthday has not yet arrived this year
    futureBirthday = birthdayThisYear  # set future birthdate as equal to the birthday this year   
  difference = futureBirthday - today # find the difference 
  #print day of days to birthday to the screen
  print('----------------------------------------------------------\nYOUR BIRTHDAY WILL BE IN THE FOLLOWING DAYS:')
  print( difference.days ) 
  print('----------------------------------------------------------') 
  
def getDayOfWeek():
  """ Prompts the user to input a date """
  """ Prints that date to the console """  
  year = getIntWithinRange('ENTER FOUR DIGIT YEAR FROM 1000 TO 2017:  ',1000,2017)
  month = getIntWithinRange('ENTER ITEGER VALUE FOR A MONTH FROM 1 TO 12:  ',1,12)
  day = getIntWithinRange('ENTER INTEGER VALUE FOR DAY: ',1,31) 
  userDate = date(year,month,day) #create a date object with user input
  dayNum = userDate.weekday() # get numerical day of the week from date object 0=Monday, 1=Tueday, ...    
  #Use the number corresponding to the day of the week to assign name of the day
  if dayNum == 0:
    dayName = 'Monday'
  elif dayNum == 1:
    dayName = 'Tuesday'  
  elif dayNum == 2:
    dayName = 'Wednsday'  
  elif dayNum == 3:
    dayName = 'Thursday'  
  elif dayNum == 4:
    dayName = 'Friday'
  elif dayNum == 5:
    dayName = 'Saturday'
  elif dayNum == 6:
    dayName = 'Sunday'                                 
  #print name of the day of the week to the screen      
  print('----------------------------------------------------------')
  print( 'The day you enetered was the following day of the week:')
  print( dayName ) 
  print('----------------------------------------------------------')    

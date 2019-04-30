'''Final Project-
WHEEL...
OF...
FORTUUUUUUUUUNE!

You all know the rules to Wheel.  It's like Hangman, but with arbitrary artificial money values attached!

References:
1.  https://stackoverflow.com/questions/28182569/get-all-indexes-for-a-python-list?noredirect=1&lq=1
2. https://gist.github.com/anonymous/8ed14085c77095e106c79952be5588cf#file-guess-letters-solution
3.                        https://repl.it/@MathiewTackitt/Python-3-Wheel-of-Fortune
'''
import math
import random
import numpy as np
money= 0

#rules will display at the start
rules= 'Guess one letter at a time after spinning the wheel.  To spin the wheel, type "spin".  Buying a vowel costs $250; to do this, type "buy".  To solve the puzzle, type "solve" and see if you are correct!  Be careful though; if you solve the puzzle incorrectly, you lose!'
print(rules)

#The alphabet or letter bank; guess from here!
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W','X', 'Y', 'Z']
vowels= ['A', 'E', 'I', 'O', 'U']

#Puzzle categories!
phrase_key= ["Severe point deductions will occur", "It is high it is far it is gone", "You can't just import essay", "I need healing", "Happy feet wombo combo", "It ain't much but it's honest work", "Please read the channel description", "Agree to disagree", "Just like old times", "Python really is handy"]
b4andafter_key= ["Dinner party planner", "Grand jury duty", "Street smart cookie", "Graphic designer jeans", "Bengal Tiger Woods", "Batman and Robin Williams", "Nikola Tesla Model Three", "Spring Break A Leg", "Verb Conjugate Gradient", "High Power Laser Project"]
onthemap_key= ["Baltimore Maryland", "Fort Lauderdale FL", "Eastern Europe", "The Bermuda Triangle", "The Island Of Oahu", "The Kanto Region", "Historic Route Sixty Six", "Havana Ooh Na Na", "Ho Chi Minh City Vietnam", "The Middle Of Nowhere"]
thing_key= ["IKEA stand mixer", "Nested For Loop", "A Perfect Relationship", "Artificial Intelligence", "Static Shock", "Radioactive Sludge", "Public Relations", "Vintage Vinyl", "Downloadable Content", "Nintendo Entertainment System"]
person_key= ["Our very own Henry Herbol", "Yankees slugger Aaron Judge", "Video game designer Jeff Kaplan", "Hosts of the original Pat Sajak and Vanna White", "Internet sensation PewDiePie", "Web Slinger Peter Parker", "The Original Genie Robin Williams", "Leader Of Blue Jays Ronald Daniels", "Vader Creator George Lucas", "Lord Of Winterfell Jon Snow"]
categories= {'Phrase': phrase_key, 'Before & After': b4andafter_key, 'On The Map': onthemap_key, 'Thing': thing_key, 'Person': person_key}

#Pick a category and puzzle within randomly!
category= random.randint(0, len(categories)-1)
print('The category is:  ' + list(categories.keys())[category])
puzzle= (categories[list(categories.keys())[category]][random.randint(0, (len(list(categories[list(categories.keys())[category]])) - 1))]).upper()

#Display the puzzle as a series of blanks!
word = []
for char in puzzle:
	if char.isalpha():
		word.append('_')
	else:
		word.append(char)

def printWord(word):
	for char in word:
		print(char),
printWord(word)


#Wheel & Other Phrases!
wheel= [900, 2500, 500, 650, 500, 800, 'Bankrupt', 700, 550, 600, 2500]
bp= ['Too bad, bankrupt!', 'There goes your money!', 'Back to zero!']

#Solve the puzzle!
#print(puzzle)
#print(puzzle[random.randint(0, len(puzzle))])
used_letters= []
while True:
  print("\nWould you like to spin the wheel, buy a vowel, or solve the puzzle?")
  print("You currently have $%d." % (money))
  print("You have currently used the following letters: ")
  print(used_letters)
  action = raw_input().upper()
  
  #Solve
  if action == 'SOLVE':
    guess= raw_input().upper()
    if guess == puzzle:
      print("Great job, you solved the puzzle!")
      break
    else:
      print("That's not correct, you lose!")
      break

  #Buy
  if action == 'BUY':
    if money < 250:
      print("You don't have enough money to buy a vowel!")
      continue
    guess= raw_input().upper()
    if guess in vowels:
      PL= list(puzzle)
      if guess in puzzle:
        a= [index for index, value in enumerate(PL) if value == guess]
        for i in a:
          word[int(i)] = guess
      if guess not in puzzle:
        print("There is no '%s' in this puzzle." % (guess))
    printWord(word)
    money= money - 250
    used_letters.append(guess)
  
  #Spin
  if action == 'SPIN':
    wheel_val= random.choice(wheel)
    if wheel_val == 'Bankrupt':
      print(random.choice(bp))
      continue
      money = money - money
    else:
      print('\nYou landed on $%d.' % (wheel_val))
    guess= raw_input().upper()
    if guess in used_letters:
      print("You've already used that letter!")
    if guess in vowels:
      print("Consonants only!")
    else:
      PL= list(puzzle)
      #print(PL)
      #print(word)
      if guess in puzzle:
        a= [index for index, value in enumerate(PL) if value == guess]
        b= len(a)
        #print(a) #Replace the blanks at these indices!
        for i in a:
          word[int(i)] = guess
        printWord(word)
        money= money + b*wheel_val
      if guess not in puzzle:
        print("There is no '%s' in this puzzle." % (guess))

      used_letters.append(guess)
    
  if '_' not in word:
    print('\nYou filled in all the letters and solved the puzzle!')
    break

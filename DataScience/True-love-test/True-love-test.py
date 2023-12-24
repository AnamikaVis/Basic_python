"""
______________________________________________________________________________________________________________

                                            Instructions
_______________________________________________________________________________________________________________

You are going to write a program that tests the compatibility between two people.
To work out the love score between two people:
Take both people's names and check for the number of times the letters in the word TRUE occurs.
Then check for the number of times the letters in the word LOVE occurs.
Then combine these numbers to make a 2 digit number.
For Love Scores less than 10 or greater than 90, the message should be:

"Your score is *x*, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:

"Your score is *y*, you are alright together."
Otherwise, the message will just be their score. e.g.:

"Your score is *z*."

name1 = "Angela Yu"
name2 = "Jack Bauer"
T occurs 0 times
R occurs 1 time
U occurs 2 times
E occurs 2 times
Total = 5

L occurs 1 time
O occurs 0 times
V occurs 0 times
E occurs 2 times
Total = 3

------------------Example Input 1-------------------
Kanye West
Kim Kardashian
------------------Example Output 1------------------
The Love Calculator is calculating your score...
Your score is 42, you are alright together.
------------------Example Input 2-------------------
Brad Pitt
Jennifer Aniston
------------------Example Output 2------------------
The Love Calculator is calculating your score...
Your score is 73.
----------------------------------------------------------
                       Table
----------------------------------------------------------
Name 1	          Name 2	                   Score
Brad Pitt	        Jennifer Aniston	         73
Prince William	  Kate Middleton	           67
Ashton Kutcher	  Mila Kunis	               63
Angela Yu	        Jack Bauer	               53
David Beckham	    Victoria Beckham	         45
Mario	Princess    Peach	                     43
Kanye West	      Kim Kardashian	           42
________________________________________________________________________________________________________________
"""
print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
Name = name1 + name2
lower_name = Name.lower()
t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e = lower_name.count("e")
digit1 = t + r + u + e 
l = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")
e = lower_name.count("e")
digit2 = l + o + v + e
score = int(str(digit1)+str(digit2))
if (score > 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")







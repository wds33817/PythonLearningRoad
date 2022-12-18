#Create a tuple, contains the odd number from 1 to 20
m = ()
for i in range(1,21):
    if (i % 2 != 0):
        m+=(i,)
print(m) 
    
#Create a list, repeat 1 to 5 sequentially 3 times
m = []
for i in range(1,6):
    j = 3
    while (j > 0):
        m.append(i)
        j-=1
print(m)

#Create a list, contains the multiples of 50
m = []
for i in range(1,50):
    if (i % 5 == 0):
        m.append(i)
print(m)

#Create a set e, contains "NASDAQ", "Dowjones", "DAX", "FTSE"
e = ("NASDAQ", "Dowjones", "DAX", "FTSE")
print(e)

#Transform  "abc" to tuple, list, set:
a = ("abc",)
print(type(a))

a = ["abc"]
print(type(a))

a = {"abc"}
print(type(a))

# Find "A", "b", "\n" ASCII, use these as keys, and ASCII code as values for a dict
a = {"A":65, "b": 98, "\n": 10}
print(a["\n"])

We can't concatenate integers with strings: we have to convert them to strings using the str() function first.

"My goodness! My gracious!" they shouted. "MY WORD! It's something brand new! It's an elephant-bird!"
my_string = '''"My goodness! My gracious!" they shouted. "MY WORD! It's something brand new! It's an elephant-bird!"'''

my_string = "\"My goodness! My gracious!\" they shouted. \"MY WORD! It's something brand new! It's an elephant-bird!\""

Python control structures: 4 types of structures -- Conditionals, loops, functions, exception handling.
    
we use for loops when we know in advance how many times we want to repeat. Generally, 
if we're trying to accomplish some goal, we don't know how long it will take to fulfill it, so we would likely use a different kind of loop.    

All loops can be written into a while loop, not necessarily a for loop. In addition, 
while loops use an expression like conditionals use to determine if another loop should occur. 
Not all loops are interchangeable, and for loops use predetermined amount of iterations (not while loops)


What is an advantage of using a for loop with range() over a for-each loop?
With range(), you know exactly how many iterations have occured.



away_team = [1, 0, 0, 0, 0, 0, 0, 0, 1]
home_team = [0, 1, 0, 0, 0, 0, 2, 0]

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#A baseball game consists of 9 innings. In each inning, each
#team can score some number of runs. Whoever scores the most
#runs wins the game. Note that there are reasons why the
#number of innings might differ; extra innings for a tie game,
#fewer innings for a rain-cancelled game, etc. So, you should
#not assume there are exactly 9 full innings.
#
#The two lists above give the runs scored in each inning by
#two teams. If the away team wins, print "Away team wins!"
#If the home team wins, print "Home team wins!" You may assume
#the game will not end in a tie.
#
#Remember, you can use a loop to look at each item in a list
#with this syntax:
#
#for value in the_list:
#
#Inside that loop, the variable 'value' will take on each
#value from the list until it's seen every value. You
#don't need to know anything more about lists to solve this
#problem!
#
#Note that you must use a loop to solve this problem. If you
#use something like the sum() function, your answer will not
#be accepted.


#Add your code here! With the initial values above, it should
#print "Home team wins!"
away_team_score = 0
home_team_score = 0
for away_score, home_score in zip(away_team, home_team):
    away_team_score += away_score
    home_team_score += home_score

if away_team_score > home_team_score:
    print("Away team wins!")
else:
    print("Home team wins!")





    
    
    
    #Write a function called to_metric. to_metric should take
#as input one parameter, a string. The string will represent
#a quantity in imperial volume units, such as "7 cups", "2
#tablespoons", or "8 gallons". to_metric should return the
#equivalent number of milliliters as a float. Round the
#result to two decimal places.
#
#The possible imperial units to handle and their conversion to
#milliliters are:
#
# - gallons: 3785.41 milliliters
# - quarts: 946.35 milliliters
# - pints: 473.18 milliliters
# - cups: 240 milliliters
# - ounces: 29.57 milliliters
# - tablespoons: 14.79 milliliters
# - teaspoons: 4.93 milliliters
#
#Return only the float representing the number of milliliters,
#not the label. For example:
#
#to_metric("7.0 cups") -> 1680
#to_metric("2.0 tablespoons") -> 29.58
#to_metric("8.0 gallons") -> 30283.28
#
#You may assume that the string will be formatted like the
#strings above: a decimal number, then a space, then one of
#the following words: cgallons, quarts, pints, cups, ounces,
#tablespoons, teaspoons


#Add your code here!

def to_metric(imperial_volume):
# Split the string into value and unit
    value, unit = imperial_volume.split()

    # Convert the value to a float
    value = float(value)

    # Determine the conversion factor based on the unit
    if unit == "gallons":
        factor = 3785.41
    elif unit == "quarts":
        factor = 946.35
    elif unit == "pints":
        factor = 473.18
    elif unit == "cups":
        factor = 240
    elif unit == "ounces":
        factor = 29.57
    elif unit == "tablespoons":
        factor = 14.79
    elif unit == "teaspoons":
        factor = 4.93

    # Convert the value to milliliters and return it
    return round(value * factor, 2)

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#1680
#29.58
#30283.28
#print(to_metric("7.0 cups"))
#print(to_metric("2.0 tablespoons"))
#print(to_metric("8.0 gallons"))
#

print(to_metric("7.0 cups"))
print(to_metric("2.0 tablespoons"))
print(to_metric("8.0 gallons"))








a_string = "F12dav^f%$25d"

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#a_string is a string of random characters. Write some code
#that adds all the digits that appear in the string and prints
#their sum.
#
#For example, the digits in the string above are 1, 2, 2, and 5,
#so your code would print 10.
#
#Remember, you can iterate over each character in a string with
#this syntax:
#
#for a_character in a_string:
#
#Remember also, you can check if a character is in a list of other
#characters within this syntax:
#
#if a_character in "ABCDEFG":
#
#If there are no digits in the string, print 0.


#Add your code here!
sum = 0

for character in a_string:
	if character in "0123456789":
		sum += int(character)
print(sum)

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





#One common function of online text-parsers is trying to find
#known text in a block of other text. For example, from a web
#site, we might want to find any phone numbers present on the
#web site.
#
#Write a function called find_phone_number. The function
#should have one parameter, a string. The function should
#return the phone number that was present in the string.
#
#For this problem, you may make the following assumptions:
#
# - The phone number will be all digits, such as 4043219876.
# - There will only be one phone number in the string.
# - There will be a phone number in the string.
# - Either the phone number will be at the start or end of
#   the string, or it will have spaces on either side of it.
#
#There may be other numbers in the string, but there will only
#be one 10-digit number. Find and return that number as a
#string.
#
#Hint: There are lots of different ways to do this. Think about
#all the tools at your disposal: split, find, casting strings
#to integers, error handling, etc.!


#Add your code here!

def find_phone_number(string):
	phone_number = ""
	for character in string:
		if character.isdigit():
			phone_number += character
		else:
			if len(phone_number) == 10:
				return phone_number
			else:
			    phone_number = ""
	return phone_number
#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.

#        if len(phone_number) == 10:
#	        return phone_number
#If your function works correctly, this will originally
#print:
#4049876543
#7705551234
#6789123456
print(find_phone_number("hello 4049876543 goodbye"))
print(find_phone_number("7705551234 this is alex"))
print(find_phone_number("doh ray me abc 123 6789123456"))




#This one is a challenge. There's a lot going on: splitting
#up strings, removing unnecessary characters, converting to
#integers, and running a big conditional. Our solution to
#this is 34 lines -- you can do it!
#
#In web development, it is common to represent a color like 
#this:
#
#  rgb(red_val, green_val, blue_val)
#
#where red_val, green_val and blue_val would be substituted 
#with values from 0-255 telling the computer how much to 
#light up that portion of the pixel. For example:
#
# - rgb(255, 0, 0) would make a color red. 
# - rgb(255, 255, 0) would make yellow, because it is equal 
#   parts red and green. 
# - rgb(0, 0, 0) would make black, the absence of all color.
# - rgb(255, 255, 255) would make white, the presence of all
#   colors equally.
#
#Don't let the function-like syntax here confuse you: here,
#these are just strings. The string "rgb(0, 255, 0)"
#represents the color green.
#
#Write a function called "find_color" that accepts a single 
#argument expected to be a string as just described. Your
#function should return a simplified version of the color
#that is represented according to the following rules:
#
# If there is more red than any other color, return "red".
# If there is more green than any other color, return "green".
# If there is more blue than any other color, return "blue".
# If there are equal parts red and green, return "yellow".
# If there are equal parts red and blue, return "purple".
# If there are equal parts green and blue, return "teal".
# If there are equal parts red, green, and blue, return "gray".
# (even though this might be white or black).


#Write your function here!
def find_color(rgb):
# split the string into parts
    parts = rgb.split(",")

    # remove the "rgb(" and ")" characters
    parts[0] = parts[0][4:]
    parts[2] = parts[2][:-1]

    # convert strings to integers
    parts = [int(part) for part in parts]

    # check which color has the greatest value
    if parts[0] > parts[1] and parts[0] > parts[2]:
        return "red"
    elif parts[1] > parts[0] and parts[1] > parts[2]:
        return "green"
    elif parts[2] > parts[0] and parts[2] > parts[1]:
        return "blue"
    # check for equal parts of two colors
    elif parts[0] == parts[1] and parts[0] > parts[2]:
        return "yellow"
    elif parts[0] == parts[2] and parts[0] > parts[1]:
        return "purple"
    elif parts[1] == parts[2] and parts[1] > parts[0]:
        return "teal"
    # if all parts are equal, return gray
    else:
        return "gray"


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: red, purple, gray, each on their own line.
print(find_color("rgb(125, 50, 75)"))
print(find_color("rgb(125, 17, 125)"))
print(find_color("rgb(217, 217, 217)"))








#Now, let's improve our steps() function to take one parameter
#that represents the number of 'steps' to print. It should
#then return a string that, when printed, shows output like
#the following:
#
#print(steps(3))
#111
#	222
#		333
#
#print(steps(6))
#111
#	222
#		333
#			444
#				555
#					666
#
#Specifically, it should start with 1, and show three of each
#number from 1 to the inputted value, each on a separate
#line. The first line should have no tabs in front, but each
#subsequent line should have one more tab than the line
#before it. You may assume that we will not call steps() with
#a value greater than 9.
#
#Hint: You'll want to use a loop, and you'll want to create
#the string you're building before the loop starts, then add
#to it with every iteration.


#Write your function here!

def steps(n):
    result = ""
    for i in range(1, n+1):
        result += '\t'*(i-1) + (str(i)*3) + '\n'
    return result



#The following two lines will test your code, but are not
#required for grading, so feel free to modify them.
print(steps(3))
print(steps(6))












#Write a function called after_second that accepts two 
#arguments: a target string to search, and string to search
#for. The  function should return everything in the first
#string *after* the *second* occurrence of the search term.
#You can assume  there will always be at least two
#occurrences of the search term in the first string. 
#
#For example:
#  after_second("11223344554321", "3") -> 44554321
#
#The search term "3" appears at indices 4 and 5. So, this
#returns everything from the index 6 to the end.
#
#  after_second("heyyoheyhi!", "hey") -> hi!
#
#The search term "hey" appears at indices 0 and 5. The
#search term itself is three characters. So, this returns
#everything from the index 8 to the end.
#
#Hint: This may be more complicated than it looks! You'll
#have to look at the length of the search string and
#either modify the target string or take advantage of the
#extra arguments you can pass to find().


#Write your function here!
def after_second(target, search):
    first_index = target.find(search)
    second_index = target.find(search, first_index + 1)
    return target[second_index + len(search):]


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print 44554321 and hi!, each on their own line.
print(after_second("11223344554321", "3"))
print(after_second("heyyoheyhi!", "hey"))









lyrics = ["I wanna be your endgame", "I wanna be your first string",
          "I wanna be your A-Team", "I wanna be your endgame, endgame"]
lines_of_sanity = 6

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Recall the Earworm problem (3.3.5 Coding Exercise 2). The
#first time, you would still finish printing the entire list
#of lyrics after lines_of_sanity was exceeded.
#
#Revise that code so that you always stop when lines_of_sanity
#is reached. If lines_of_sanity is 6, you would print 6 lines,
#no matter how many lines are in the list. If there are fewer
#than 6 lines in the list, then you'd repeat the list until
#the number of lines is reached.
#
#For example, with the values above, you'd print:
#I wanna be your endgame
#I wanna be your first string
#I wanna be your A-Team
#I wanna be your endgame, endgame
#I wanna be your endgame
#I wanna be your first string
#MAKE IT STOP
#
#That's 6 lines: the entire list once, then the first two lines
#again to reach 6. As before, print MAKE IT STOP when you're
#done.
#
#HINT: There are multiple ways to do this: some involve a small
#change to our earlier answer, others involve a more wholesale
#rewrite. If you're stuck on one, try to think of a totally
#different way!


#Add your code here! Using the initial inputs from above, this
#should print 7 lines: all 4 lines of the list, then the first
#two lines again, then MAKE IT STOP

count = 0
while count < lines_of_sanity:
    for line in lyrics:
        print(line)
        count += 1
        if count == lines_of_sanity:
            break
print("MAKE IT STOP")









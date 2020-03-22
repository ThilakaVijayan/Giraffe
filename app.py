# Hello world
"""
print("Hello World")
"""
# -----------------------

# Drawing a Shape
""" 
print("    /|")
print("   / |")
print("  /  |")
print(" /   |")
print("/____|")
"""
# -----------------------
# Variable & Data Types
"""
character_name = "John"
character_age = "35"

print("There was once a man named " + character_name + ", ")
print("he was " + character_age + " years old. ")
character_name = "Tom"
print("He really liked the name " + character_name + ", ")
print("but didn't like being " + character_age + ".")

is_male = True
age = 50
"""
# -----------------------
# Working with Strings
"""
print("Giraffe Academy")
print("Giraffe\nAcademy")
print("Giraffe\"Academy")
print("Giraffe\Academy")

phrase = "Giraffe Academy"
print(phrase)
print(phrase + " is cool")
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[0])
print(phrase[3])
print(phrase.index("G"))
print(phrase.index("a"))
print(phrase.index("Acad"))
#print(phrase.index("z"))
print(phrase.replace("Giraffe","Elephant"))
"""
# -----------------------
# Working with Numbers
"""
print(2)
print(2.9087)
print(-2.9087)
print(3 + 4)
print(3 + 4.5)
print(3 * 4 + 5)
print(3 * (4 + 5))
print(10 % 3)

my_num = 5
print(my_num)
print(str(my_num))
print(str(my_num) + " my favourite number")
my_num = -5
print(str(abs(my_num)))
print(pow(3,2))
print(max(4,6))
print(min(4,6))
print(round(3.3))
print(round(3.7))

from math import *

print(floor(3.7))
print(ceil(3.3))
print(sqrt(36))
"""
# -----------------------
# Getting Input From Users
"""
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "! You are " + age)

"""
# -----------------------
# Building a Basic Calculator
"""
num1 = input("Enter a number ")
num2 = input("Enter another number ")
result = num1 + num2
print(result)


num3 = input("Enter a number ")
num4 = input("Enter another number ")
result = int(num3) + int(num4)
print(result)


num5 = input("Enter a number ")
num6 = input("Enter another number ")
result = float(num5) + float(num6)
print(result)

"""
# -----------------------
# Mad Libs Game
"""
print("Roses are red")
print("Voilets are blue")
print("I love you")

color = input("Enter a color: ")
plural_noun = input("Enter a plural noun: ")
celebrity = input("Enter a celebrity: ")
print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)

"""
# -----------------------
# Lists
"""
my_list = ["Kevin", 2, True]
print(my_list)
friends = ["Kevin", "Karen","Jim"]

print(friends[0])
print(friends[2])
print(friends[-1])
print(friends[-3])
print(friends[1:])

friends = ["Kevin", "Karen","Jim", "Oscar","Toby"]
print(friends[1:3])
friends[1] = "Mike"
print(friends)
"""
# -----------------------
# List Functions
"""
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen","Jim", "Oscar","Toby"]

print(friends)
friends.extend(lucky_numbers)
print(friends)

friends = ["Kevin", "Karen","Jim", "Oscar","Toby"]
friends.append("Creed")
print(friends)

friends = ["Kevin", "Karen","Jim", "Oscar","Toby"]
friends.insert(1, "Kelly")
print(friends)

friends = ["Kevin", "Karen","Jim", "Oscar","Toby"]
friends.remove("Jim")
print(friends)

friends = ["Kevin", "Karen","Jim", "Oscar","Toby"]
friends.clear()
print(friends)

friends = ["Kevin", "Karen","Jim", "Oscar","Toby"]
friends.pop()
print(friends)

friends = ["Kevin", "Karen","Jim", "Oscar","Toby"]
friends.pop()
print(friends.index("Kevin"))
print(friends.index("Oscar"))
#print(friends.index("Mike"))

friends = ["Kevin", "Karen","Jim", "Jim", "Oscar","Toby"]
print(friends.count("Jim"))
friends.sort()
print(friends)
lucky_numbers = [42, 8, 15, 16, 23]
lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)

friends2 = friends.copy()
print(friends2)
"""
# -----------------------
# Tuples
"""
coordinates = (4, 5)
print(coordinates[0])
print(coordinates[1])

#coordinates[1]=10 # not possible to do this.

coordinates = [(4, 5), (6, 7), (80, 34)] # a list of Tuples

"""
# -----------------------
# Functions
"""
def sayhi():
    print("Hello User")

print("Top")
sayhi()
print("Bottom")

def say_hi(name):
    print("Hello " + name)

say_hi("Mike")
say_hi("Steve")

def say_hi2(name, age):
    print("Hello " + name + ", you are " + age)

say_hi2("Mike", "35")
say_hi2("Steve", "70")

def say_hi3(name, age):
    print("Hello " + name + ", you are " + str(age))

say_hi3("Mike", 35)
say_hi3("Steve", 70)

"""
# -----------------------
# Return Statement
"""

def cube(num):
    return num * num * num
    print("code") # never reach this code, but no error

result = cube(4)
print(result)

"""
# -----------------------
# If Statements
"""
is_male = True

if is_male:
    print("You are a male")


is_male = False

if is_male:
    print("You are a male")
else:
    print("You are not a male")

is_male = True
is_tall = True

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither male nor tall")

is_male = True
is_tall = True

if is_male and is_tall:
    print("You are a tall male")
else:
    print("You are either not male or not tall or both")

is_male = False
is_tall = True

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not (is_tall):
    print("You are short male")
elif not is_male and is_tall:
    print("You are not a male but tall")
else:
    print("You are not male and not tall")

"""
# -----------------------
# If Statements & Comparisons

"""
def max_num (num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


def max_num2 (num1, num2, num3):
    if num1 >= num2:
        if num1 >= num3:
            return num1
        else:
            return num3
    elif num2 >= num3:
        return num2
    else:
        return num3


print("3, 3, 4")
print(max_num(2, 3, 4))
print(max_num2(2, 3, 4))


print("3, 2, 4")
print(max_num(3, 2, 4))
print(max_num2(3, 2, 4))

print("4, 3, 2")
print(max_num(4, 3, 2))
print(max_num2(4, 3, 2))

print("2, 4, 3")
print(max_num(2, 4, 3))
print(max_num2(2, 4, 3))


"""
# -----------------------
# Building a better Calculator
"""
num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Invalid operator")
    

"""
# -----------------------
# Dictionaries
"""
monthConversion = {
    "Jan": "January",
    "Feb": "February",
    "Jan": "Duplicate", # duplicate keys
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(monthConversion["Nov"])
print(monthConversion.get("Jan"))
print(monthConversion.get("Luv", "Not a valid key"))

monthConversion = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

print(monthConversion[11])
print(monthConversion.get(1))
print(monthConversion.get("e", "Not a valid key"))

"""
# -----------------------
# While Loop
"""
i = 1
while i <= 10:
    print(i)
    i += 1 # i = i + 1

print("Done with loop")

"""
# -----------------------
# Building a Guessing Game
"""
secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not out_of_guesses :
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Out of guesses, You Lose!")
else:
    print("You win!")
    
"""
# -----------------------
# For Loops
"""
for letter in "Giraffe Academy":
    print(letter)

friends = ["Jim", "Karen", "Kevin"]
for friend in friends:
    print(friend)

for index in range(10):
    print(index)

for index in range(3, 10):
    print(index)

friends = ["Jim", "Karen", "Kevin"]
for index in range(len(friends)):
    print(friends[index])

for index in range(5):
    if index == 0:
        print("First iteration")
    else:
        print("Not first iteration")
        
"""
# -----------------------
# Exponent Function
"""
print(2**3)

def raise_to_power(base_num, power_num):
    result = 1
    for index in range(power_num):
        result = result * base_num
    return result

print(raise_to_power(2,3))

"""
# -----------------------
# 2D Lists & Nested Loops
"""
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[0][0])
print(number_grid[2][1])

for row in number_grid:
    print(row)
    for col in row:
        print(col)
"""
# -----------------------
# Building a Translator
"""
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return  translation

print(translate(input("Enter a phrase: ")))

def translate2(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return  translation

print(translate2(input("Enter a phrase: ")))

def translate3(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return  translation

print(translate3(input("Enter a phrase: ")))
"""
# -----------------------
# Comments

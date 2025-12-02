###   Utilities ###

# The imports are Python keywords that tells Python to load modules, libraries, and packages into your file so you can use their respective functions, classes, variables, etc.
import time
import random
from colorama import Fore, init

# This is my clear function. It allows me to type clear() for the terminal to look clean and uncluttered
def clear():
    print("\033c")

# This is the auto reset function for colorama, I don't trust it so I added a manual one as well
init(autoreset=True)

# Sleep options(These functions allow me to slow down the rate of code that's being spit out):
def time1():
    time.sleep(1)
def time2():
    time.sleep(2)
def time3():
    time.sleep(3)
def time4():
    time.sleep(4)

# Color options (These variables are simple little color options if I choose to embed them):
Red = Fore.RED
Green = Fore.GREEN
Cyan = Fore.CYAN
Blue = Fore.BLUE
Reset = Fore.RESET
###################
## Everything above the # is all the shortcuts and utilities I need in this file

clear()

# Simple input to get the user's name
Input = input('May I get your name?\n---> ')

time2()

print('This next mini-game shall be:')

time3()

print('Mad Libs!')

time1()

print("\nNow don't worry, it's incredibly simple and all you have to do is choose a word that the prompt gives you!")

time2()

# Alright now for the core of this mini-game, I needed to set up a list that contained all 4 word types to choose from. This is only a stepping-stone for the upcoming code
word_types = ["noun", "verb", "adjective", "adverb"]

# This dictionary is important for how the game will memorize what the user inputs. If the 4 different words are "dog, ran, silly, and funky", then the game will know what the user-
# inputs.
user_choices = {}

print("Here, let's start off with this. Choose one word that the prompt asks you for.\n")

time1()

# A little complicated to explain, but basically the setup for this for loop is saying "I have a box called grammar and for everything in word_types, store them in there." 
# Now inside this for loop, word_types has temporarily become grammar. Why is this necessary? Because we need the user to choose a word for each item in the word_type list
# To do this, we need to essentially make a new variable that Python can translate a list into words that can be added into a input statement
for grammar in word_types:
    
    time1()

    # Simple input statement that asks the user using whichever word is stored in grammer (the temporary box made by the for loop)
    question = input(f"Please enter a {grammar}\n---> ")
    
    # This specific line looks complicated but it can be easily explained. In a nutshell, it displays how the dictionary takes user's input from grammar and stores them.
    # The setup goes like this: The dictionary (user_choices) is your inventory and for everything inside grammar, the dictionary will store the user's input from question.
    # In other words, it's practically saying "Take the empty dictionary (user_choices) and for every word in grammar, take the user's response from question and store it in
    # user_choices".
    user_choices[grammar] = question

# Now this bad boy is the story teller, this is where the story is created and the user's choices gets embedded into the story itself. It's a shitty story but I'm no poet.
mad_lib = (
    "There once was a " + user_choices["noun"] + " " + user_choices["verb"] +
    " wanted to " + user_choices["adjective"] + " incredibly " + user_choices["adverb"] +
    ". What a strange adventure!"
)

time2()

# Simple little print statement that returns the story to the user
print('Yay! You are now done with you Mad Lib. Here it is now!:\n' + mad_lib)


## The code above works properly and is a very rough draft of a Mad Lib game, ChatGPT was needed to help refresh my memory on lists and dictonaries but it could not be helped
# Note: this is primarily to give an example on how lists and storing users input in a dictionary and printing it back to the user properly and efficiently

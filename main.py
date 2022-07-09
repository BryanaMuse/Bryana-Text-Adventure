# This is a starter for a text based game in python.
# fill it in and tell a story that would be fun to play

from expand import *
# I use multiple modules as an example for you to try and replicate to keep your
# story neat and get used to using them

# Basic control flow is what this file mostly deals with and the end goal is
# to let others use it. Try to make your code so it doesn’t break easily.


def main():
   # end story is the variable I will use to end the program.
   #gmae
   endStory = 2
   # The while loop will keep repeating until the break of set by endStory is
   # triggered
   while(endStory > 1):
       # terminal prints can be over multiple lines using """ print """ format,
       # instead of the regular  "print" give it a try
       print("Welcome to 5 Minutes!")
       # this is how your story can take input and read it back out
       userInput = input("Enter anything to begin your journey ")
       print("user input: ", userInput)
       # notice input can output to terminal. Look up the input function for python
       # to see why.
       print("Exhausted, you open the door to your apartment To the left is the living room. To the rght is the kitchen  ")
       userInput = input("""Would you like to go Left or Right?
                 option 1: enter Y for right
                 option 2: enter N for left """)
       # there are many ways to break this and you should try to write code that
       # catches common cases and check the user for options other than what
       # asked for.
       if(userInput == "Y"):
           print(
              "You go left entering the living room. The room has a blue couch with a wooden coffe table")
           userInput = input("""would you like to sit down?
                    option 1: enter Y for yes
                    option 2: enter N for no""")

       if(userInput == "Y"):
           print(
                "You sit down. You look at the coffee table and see a faded black book titled, The Man of Minutes")
           print(
              "You stare at the book in confusion. When did you buy this? Where did it come from?")
           userInput = input("""Curious, Would you like to read it?
option 1: enter Y for yes
option 2: enter N for no""")

       if(userInput == "Y"):
           print("As you open the book, the words begin to float of the page as the words assemble, you read...")
           print(
              "The man of time, of all divine, he strikes in five.. Count in five... run and hide")
           print(
              "When you her is screech. He'll start to seek..The man of time... count or die")

# This ends the story
           endStory = 0
       elif(userInput == ""):
           print("goodbye, rerun python main.py to play")
# This also ends the story
           endStory = 0

       print("")


# Remove this and try to run your code to try and understand what it does so
# if you write a main module and its not working you can tell why.
if __name__ == '__main__':
    main()

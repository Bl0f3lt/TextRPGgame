#RPG Game v2.0.0
#The rewrite

#The same original text dungeon game but rewritten to be easier to expand, more efficent, and most importantly more fun

#importing libs
from ast import match_case
import random
import json
import time
from turtle import distance


#subroutines
def chanceSystem():


def playerChoice1():
    print("1.Explore the City")
    print("2.View Inventory")
    print("3.Use Item from Inventory")
    print("4.")

def explore(energy):
    distanceValid = False
    lootFound = 0
    print("You have '{}' energy".format(energy))
    if firstExplore == True:
        print("Each 1km explored, uses 10 energy. Try not to run out or bad consequence could arise")
        print("The further you explore, the more likely you are to find some items.")
        firstExplore = False
    while distanceValid == False:
        exploreDistance = input("Enter a distance to explore: ")
        if (exploreDistance * 10) > energy:
            print("Cannot Explore this far, Not enough Energy!")
        else:
            distanceValid = True
    
    randSet = [] #put distance loot chances in json and load in
    for i in exploreDistance: #exploreDistance needs to be the percentage e.g. distance 1 = 40
        randSet.append(random.randint(0,100))
    chanceNum = random.randint(0,100)
    for i in randSet:
        if i == chanceNum:
            lootFound = lootFound + 1



#variable init
firstExplore = True
#main
if __name__ == "__main__":
    #Game Greeting
    print("Hello Friend")
    time.sleep(4)
    print("Welcome to the amazing Text RPG game")
    time.sleep(4)
    print("A fun project, created by Bl0f3lt as a way to practice and refine his programming skills.")
    time.sleep(4)
    print("You start with nothing, and can explore to find some basic items.")
    time.sleep(4)
    print("Later on more powerful item can be found in dungeons.")
    time.sleep(4)
    print("However, watch out along the way.")
    time.sleep(4)
    print("Threats can come from enimies, and your own stats.")
    time.sleep(4)
    print("If your energy becomes too low you must rest. And if your health becomes too low, then you could face a gritty demise.")
    time.sleep(4)
    input("Good luck - press enter too continue: ")
    while True:
        print("Waking up with a sore vividness from what seemed to be a dream, you get of your bed and slip your shoes on, almost as if you had done it a thousand times before.")
        print("On your way down the stairs, you happen to glance out of the window and catch a gaze over the dystopian city that you call home. The same old muggy haze, with the same similar voices in the distance.")
        print("As you reach the bottom you collect the post and see what you have: ")
        print("'Call to the country' the home decorating magazine")
        print("'IMPORTANT'-Goverment Documents-'IMPORTANT'")
        print("Letter Person unkown")
        print("With nothing standing out you head to the kitchen to decide your next move for the day ahead: ")        
        
        
        playerMove =
    
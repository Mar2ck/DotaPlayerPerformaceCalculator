#!/usr/bin/env python3
"""
Program Frontend - CLI/GUI Interface
"""
# Built-in modules
import argparse
# Local modules
import player_performance_score
import data_scraper


def DisplayMenuOptions():
    options = ["Set up match", "Look at players"]  ##Always add new menu options here
    for i in range(len(options)):  ##Prints out all the options
        print(str(i + 1) + ": " + options[i])
    print("9: Quit\n")  ##Always outputs quit as 9 // Make sure no more than 8 options!


def SetUpMatch():
    menuChoice = ""
    while (menuChoice != "9"):
        team1 = []
        team2 = []
        print ("Team 1: ")
        for i in team1:
            print (data_scraper.getStats(team1[i])["Name"])
        print ("Team 2: ")
        for i in team2:
            print (data_scraper.getStats(team2[i])["Name"])

        if (team1.count() > 0 and team2.count() > 0):
            prob = player_performance_score.GetProbability(AveragePPS(team1),AveragePPS(team2))
            print ("There is a " + (prob * 100) + "% chance that team 1 will beat team 2")

        print ("1: Add player to team 1")
        print ("2: Add player to team 2")
        print ("9: Quit\n")
        while True:
            try:
                menuChoice = int(input("Select menu item: "))  ##Checks if the input is an int
            except:
                print("Be better")  ##Make polite
            else:  ##Always add new menu options here
                if (menuChoice == 1):
                    team1.append(getPlayer())
                    break
                elif (menuChoice == 2):
                    team2.append(getPlayer())
                    break
                elif (menuChoice == 9):
                    break
                else:
                    print("Be better")  ##Checks if the int is an option

def AveragePPS(team):
    total = 0
    for i in team:
        total+=getPPS(team[i])
    return total//i

def GetPlayer(): ##Get player id from user's player selection
    pass

def ListPlayers():
    pass

def SearchPlayers(array, item):
    if (len(array) == 0):
        return -1  ##-1 means not there

    else:
        mIndex = (len(array)) // 2
        if (array[mIndex] == item):
            return mIndex  ##Returns the index of the item
        else:
            if (item < array[mIndex]):  ##Look at how I compare
                return SearchPlayers(array[:mIndex])
            else:
                return SearchPlayers(array[mIndex:])


def MergeSort(array):
    if (len(array) > 1):
        mIndex = (len(array)) // 2
        left = array[:mIndex]
        right = array[mIndex:]

        MergeSort(left)
        MergeSort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if (left[i] < right[j]):  ##Look at how I compare two items when I know what the items will be
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

    print(array)  ##Remove once debuging is done


#### Main ####
DisplayMenuOptions()
while True:
    try:
        menuChoice = int(input("Select menu item: "))  ##Checks if the input is an int
    except:
        print("Be better")  ##Make polite
    else:  ##Always add new menu options here
        if (menuChoice == 1):
            SetUpMatch()
        elif (menuChoice == 2):
            ListPlayers()
        elif (menuChoice == 9):
            break
        else:
            print("Be better")  ##Checks if the int is an option
print("Thanks for coming")

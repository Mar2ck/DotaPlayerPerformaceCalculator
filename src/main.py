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
    sortedPlayers = MergeSort(data_scraper.ListAllPlayerIDs())
    team1 = []
    team2 = []
    while (menuChoice != "9"):

        if (len(team1) > 0 or len(team2) > 0):
            print ("Team 1: ")
            for i in team1:
                ##print (data_scraper.DictPlayerInfo(i)["player_id"])
                ##print (i)
                print (data_scraper.DictPlayerInfo(i)["name"])
            print ("Team 2: ")
            for i in team2:
                print (data_scraper.DictPlayerInfo(i)["name"])

            if (len(team1) > 0 and len(team2) > 0):

                prob = player_performance_score.GetProbability(AveragePPS(team1),AveragePPS(team2))
                print ("There is a " + str(prob * 100) + "% chance that team 1 will beat team 2")

        print ("1: Add player to team 1")
        print ("2: Add player to team 2")
        print ("9: Quit\n")
        while True:
            try:
                menuChoice = int(input("Select menu item: "))  ##Checks if the input is an int
            except:
                print("Be better")  ##Make polite
            else:
                if (menuChoice == 1):
                    temp = GetPlayer(sortedPlayers)
                    if (temp != -1):
                        team1.append(GetPlayer(sortedPlayers))
                    else:
                        print ("Player not found")
                    break
                elif (menuChoice == 2):
                    temp = GetPlayer(sortedPlayers)
                    if (temp != -1):
                        team2.append(GetPlayer(sortedPlayers))
                    else:
                        print("Player not found")
                    break
                elif (menuChoice == 9):
                    break
                else:
                    print("Be better")  ##Checks if the int is an option

def AveragePPS(team):
    total = 0
    for i in team:
        total+=player_performance_score.playerPPS.get(i)
    return total//i

def GetPlayer(allPlayers): ##Get player id from user's player selection
    name = input("Please enter the player's name: ")
    playerID = SearchPlayers(allPlayers, name)
    return playerID

def ListPlayers():
    pass

def SearchPlayers(array, item): ##Searches for a player based on name
    mIndex = (len(array)) // 2
    if (len(array) == 1):
        if (data_scraper.DictPlayerInfo(array[mIndex])["name"] == item):
            return array[mIndex]
        else:
            return -1  ##-1 means not there

    else:
        ##mIndex = (len(array)) // 2
        if (data_scraper.DictPlayerInfo(array[mIndex])["name"] == item):
            return array[mIndex]  ##Returns the index of the item
        else:
            if (item < data_scraper.DictPlayerInfo(array[mIndex])["name"]):  ##Look at how I compare
                return SearchPlayers(array[:mIndex], item)
            else:
                return SearchPlayers(array[mIndex:], item)


def MergeSort(array): ##Sorts the array based on name
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
            if (data_scraper.DictPlayerInfo(left[i])["name"] < data_scraper.DictPlayerInfo(right[j])["name"]):  ##Look at how I compare two items when I know what the items will be
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

    ##print (array)
    return array


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

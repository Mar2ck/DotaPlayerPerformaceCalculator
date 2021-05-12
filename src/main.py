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
    print ("Sorting all players...")
    sortedPlayers = MergeSort(data_scraper.ListAllPlayerIDs())
    print ("Sorted " + str(len(data_scraper.ListAllPlayerIDs())) + "players total")
    team1 = []
    team2 = []
    while (menuChoice != "9"):

        if (len(team1) > 0):
            print ("Team 1: ")
            for i in team1:
                print (data_scraper.DictPlayerInfo(i)["name"])
        else:
            print ("Team 1 is empty")
        if (len(team2) > 0):
            print ("Team 2: ")
            for i in team2:
                print (data_scraper.DictPlayerInfo(i)["name"])
        else:
            print("Team 2 is empty")

        if (len(team1) > 0 and len(team2) > 0):
            prob = player_performance_score.GetProbability(player_performance_score.AveragePPS(team1),player_performance_score.AveragePPS((team2)))
            print ("There is a " + str(prob * 100) + "% chance that team 1 will beat team 2")

        print ("1: Add player to team 1")
        print ("2: Add player to team 2")
        print ("3: Remove player from team 1")
        print ("4: Remove player from team 2")
        print ("9: Quit\n")

        try:
            menuChoice = int(input("Select menu item: "))  ##Checks if the input is an int
        except:
            print("Please enter a suitable input")  ##Make polite1
        else:
            if (menuChoice == 9): ##exit loop
                break
            elif (menuChoice == 1): ## add name given
                temp = GetPlayer(sortedPlayers)
                if (temp != -1):
                    if(len(team1) == 5):
                        print("Max amount of players have been added")
                    else:
                        if (nameChecker(temp, (team1 + team2)) == False):
                            team1.append(temp)
                        else:
                            print (data_scraper.DictPlayerInfo(temp)["name"] + " is already in use")
                else:
                    print("Player not found")
            elif (menuChoice == 2):## add name given
                temp = GetPlayer(sortedPlayers)
                if (temp != -1):
                    if(len(team2) == 5):
                        print("Max amount of players have been added")
                    else:
                        if (nameChecker(temp, (team1 + team2)) == False):
                            team2.append(temp)
                        else:
                            print (data_scraper.DictPlayerInfo(temp)["name"] + " is already in use")
                else:
                    print("Player not found")
            elif (menuChoice == 3):#remove name given if found
                if(len(team1) == 0):
                    print("Please enter a player before removing")
                else:
                    removePlayer(team1)
            elif (menuChoice == 4): ##remove name given if found
                if(len(team2) == 0):
                    print("Please enter a player before removing")
                else:
                    removePlayer(team2)
            else:
                print("Please enter a suitable input")  ##Checks if the int is an option

def removePlayer(team):
    playerName = input("Please enter the player's name: ") ##gets user input for removal name
    counter = 0 ##counts index
    for player in team:
        if data_scraper.DictPlayerInfo(player)["name"] == playerName: ##checks to see names match
            print(data_scraper.DictPlayerInfo(player)["name"] + "has been removed")
            del team[counter]
            return
    print(playerName + " isn't found")##displays issue to user


def nameChecker(playerName, team):

    if(len(team) == 0): ##return if the list is empty
        return False
    else:
        for name in team: ## checks all inputted names to see if it is there already
            if (name == playerName):
                return True
    return False

def GetPlayer(allPlayers): ##Get player id from user's player selection
    name = input("Please enter the player's name: ")
    playerID = SearchPlayers(allPlayers, name)
    return playerID

def SearchPlayers(array, item): ##Searches for a player based on name
    mIndex = (len(array)) // 2
    if (len(array) == 1):
        if (data_scraper.DictPlayerInfo(array[mIndex])["name"] == item):
            return array[mIndex]
        else:
            return -1  ##-1 means not there

    else:
        if (data_scraper.DictPlayerInfo(array[mIndex])["name"] == item):
            return array[mIndex]  ##Returns the index of the item
        else:
            if (item < data_scraper.DictPlayerInfo(array[mIndex])["name"]):  ##Look at how I compare
                return SearchPlayers(array[:mIndex], item)
            else:
                return SearchPlayers(array[mIndex:], item)
def OutputAllPlayers():
    for x in data_scraper.ListAllPlayerIDs():
        print(data_scraper.DictPlayerInfo(x)["name"])
    print()

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
            if (data_scraper.DictPlayerInfo(left[i])["name"] < data_scraper.DictPlayerInfo(right[j])["name"]):
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

while True:
    DisplayMenuOptions()
    try:
        menuChoice = int(input("Select main menu item: "))  ##Checks if the input is an int
    except:
        print("Please enter a suitable input")  ##Make polite
    else:  ##Always add new menu options here
        if (menuChoice == 1):
            SetUpMatch()
        elif (menuChoice == 2):
            OutputAllPlayers()
        elif (menuChoice == 9):
            break
        else:
            print("Please enter a suitable input")
print("Thanks for coming")

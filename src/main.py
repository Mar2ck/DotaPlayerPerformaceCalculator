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
    options = ["Set up match", "List all players"]  ##Always add new menu options here
    for i in range(len(options)):  ##Prints out all the options
        print(str(i + 1) + ": " + options[i])
    print("9: Quit\n")  ##Always outputs quit as 9 // Make sure no more than 8 options!

def SetUpMatch():
    menuChoice = ""
    print ("Sorting all players...")
    sortedPlayers = MergeSort(data_scraper.ListAllPlayerIDs()) ##Sorts all players by name
    print ("Sorted " + str(len(data_scraper.ListAllPlayerIDs())) + " players total")
    team1 = []
    team2 = []
    while (menuChoice != "9"):

        if (len(team1) > 0): ##Only prints the teams if they have at least one player
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
            prob = player_performance_score.GetProbability(player_performance_score.TotalPPS(team1),player_performance_score.TotalPPS((team2))) ##Gets the probability of winning
            print ("There is a " + str(prob * 100) + "% chance that team 1 will beat team 2")

        print ("1: Add player to team 1")
        print ("2: Add player to team 2")
        print ("3: Remove player from team 1")
        print ("4: Remove player from team 2")
        print ("9: Quit\n")

        try:
            menuChoice = int(input("Select menu item: "))  ##Checks if the input is an int
        except:
            print("Please enter a suitable input")
        else:
            if (menuChoice == 9): ##Exits the loop
                break
            elif (menuChoice == 1): ##Add a player to team 1
                temp = GetPlayer(sortedPlayers) ##Gets a player from the user
                if (temp != -1): ##Checks if the player exists
                    if(len(team1) == 5): ##Checks if the team is full
                        print("Max amount of players have been added")
                    else:
                        if (nameChecker(temp, (team1 + team2)) == False): ##Checks if the player is already in use
                            team1.append(temp) ##Adds the player to team 1
                        else:
                            print (data_scraper.DictPlayerInfo(temp)["name"] + " is already in use")
                else:
                    print("Player not found")
            elif (menuChoice == 2):##Add a player to team 2
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
            elif (menuChoice == 3):#Remove a player from team 1
                if(len(team1) == 0): ##Checks if the team has players
                    print("Please enter a player before removing")
                else:
                    removePlayer(team1) ##Removes the player from team 1
            elif (menuChoice == 4): ##Remove a player from team 2
                if(len(team2) == 0):
                    print("Please enter a player before removing")
                else:
                    removePlayer(team2)
            else:
                print("Please enter a suitable input")

def removePlayer(team):
    playerName = input("Please enter the player's name: ") ##Gets the user's input
    counter = 0 ##Counts index
    for player in team: ##Loops for each player
        if data_scraper.DictPlayerInfo(player)["name"] == playerName: ##Checks if names match
            print(data_scraper.DictPlayerInfo(player)["name"] + " has been removed")
            del team[counter] ##Removes the player from the team
            return
        counter = counter + 1
    print(playerName + " isn't found") ##Displays issue to user


def nameChecker(playerName, team):
    if(len(team) == 0): ##Checks if the list is empty
        return False
    else:
        for name in team: ##Checks all inputted names to see if it is there already
            if (name == playerName):
                return True
    return False

def GetPlayer(allPlayers): ##Get player id from user's player selection
    name = input("Please enter the player's name: ")
    playerID = SearchPlayers(allPlayers, name)
    return playerID

def SearchPlayers(array, item): ##Searches for a player based on name
    mIndex = (len(array)) // 2 ##Finds the midpoint
    if (len(array) == 1):
        if (data_scraper.DictPlayerInfo(array[mIndex])["name"] == item):
            return array[mIndex] ##Returns the player's ID
        else:
            return -1  ##-1 is returned if the player is not there

    else:
        if (data_scraper.DictPlayerInfo(array[mIndex])["name"] == item):
            return array[mIndex]  ##Returns the player's ID
        else:
            if (item < data_scraper.DictPlayerInfo(array[mIndex])["name"]): ##Checks if the item is less or more than the midpoint
                return SearchPlayers(array[:mIndex], item)
            else:
                return SearchPlayers(array[mIndex:], item)

def OutputAllPlayers():
    for x in data_scraper.ListAllPlayerIDs(): ##Loops through every player
        print(data_scraper.DictPlayerInfo(x)["name"] + ": " + str(int(player_performance_score.playerPPS[x]))) ##Outputs the player's names
    print()

def MergeSort(array): ##Sorts the array based on name
    if (len(array) > 1): ##Checks if the array is split down to one player
        mIndex = (len(array)) // 2 ##Finds the midpoint
        left = array[:mIndex]
        right = array[mIndex:]

        MergeSort(left) ##Sorts the left half of the array
        MergeSort(right) ##Sorts the right half of the array

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right): ##Checks if there are players in both lists
            if (data_scraper.DictPlayerInfo(left[i])["name"] < data_scraper.DictPlayerInfo(right[j])["name"]): ##Compares the two players
                array[k] = left[i] ##Adds the player to the sorted array
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
    return array ##Returns the sorted array

#### Main ####

while True:
    DisplayMenuOptions() ##Displays the main menu options
    try:
        menuChoice = int(input("Select main menu item: "))  ##Checks if the input is an integer
    except:
        print("Please enter a suitable input")
    else:  ##Always add new menu options here
        if (menuChoice == 1):
            SetUpMatch() ##Sets up a new match
        elif (menuChoice == 2):
            OutputAllPlayers() ##Lists all players
        elif (menuChoice == 9):
            break ##Exits the program
        else: ##Checks if the input is an option
            print("Please enter a suitable input")
print("Thanks for coming")

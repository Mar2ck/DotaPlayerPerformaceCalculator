#!/usr/bin/env python3
"""
Program Frontend - CLI/GUI Interface
"""
# Built-in modules
import argparse
# Local modules
import player_performance_score


def DisplayMenuOptions():
    options = ["Set up match", "Look at players"]  ##Always add new menu options here
    for i in range(len(options)):  ##Prints out all the options
        print(str(i + 1) + ": " + options[i])
    print("9: Quit\n")  ##Always outputs quit as 9 // Make sure no more than 8 options!


def SetUpMatch():


def ListPlayers():


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

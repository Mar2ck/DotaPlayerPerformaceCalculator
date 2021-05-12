#!/usr/bin/env python3
"""
Player Performance Score (ELO inspired) Calculations
"""
# Built-in modules
import json
# Local modules
import data_scraper

playerPPS = {}


def GetProbability(ppsA, ppsB):
    return 1/(1+10**((ppsB - ppsA)/400))  # if the difference is 400 the chance of winning is 10x high


def CalculatePPSChange(ppsA, ppsB):
    eloConstant = 32  # Can be changed
    pA = GetProbability(ppsA, ppsB)
    pB = 1 - pA
    change = int(round(eloConstant * (1 - pA)), 0)  # Change is alwways an int
    #if winner == 1:
       # ppsA += change
       # ppsB -= change
    #else:
        #ppsB += change
        #ppsA -= change
    return change


def GetPPS(playerID):
    if playerPPS[playerID] is None:
        playerPPS[playerID] = 1000
    return playerPPS[playerID]

def InitialPPS():
    for i in data_scraper.ListAllPlayerIDs():
        playerPPS[i] = 1000

def AveragePPS(team):
    total = 0
    for i in team:
        total+=playerPPS.get(i)
    return total//i

def SetPlayersNewPPS():
    print ("Updating player PPS...")
    for match in data_scraper.matchArray:
        team1 = team2 = []
        for player in match["players"]:
            if (player["isRadiant"] == True):
                team1.append(player)
            else:
                team2.append(player)

        changeInPPS = 5*(CalculatePPSChange(AveragePPS(team1), AveragePPS(team2)))
        if (match["radiant_win"] == True):
            for player in match["players"]:
                weight = 0.2 ##Update with function
                if (player["isRadiant"] == True):
                    playerPPS[player["account_id"]] += changeInPPS*weight
                else:
                    playerPPS[player["account_id"]] -= changeInPPS*weight


#### Main ####
InitialPPS()
SetPlayersNewPPS()
if __name__ == "__main__":
    print(data_scraper.DictPlayerInfo(135878232))
    print(data_scraper.DictPlayerMatchStats(4967600837, 135878232))


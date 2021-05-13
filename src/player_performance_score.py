#!/usr/bin/env python3
"""
Player Performance Score (ELO inspired) Calculations
"""
# Built-in modules
import json
# Local modules
import data_scraper

playerPPS = {} ##Creates an empty dictionary to store player's pps


def PlayerContributionScore(match_id, player_id):
    score = 0.0
    killWorth = 200 ##Kill weight can be altered
    playerMatchStats = data_scraper.DictPlayerMatchStats(match_id, player_id) ##Gets the player's performance in the match
    score += playerMatchStats["kills"] * killWorth
    score += playerMatchStats["assists"] * killWorth * 0.5
    score += playerMatchStats["deaths"] * killWorth * -1
    score += playerMatchStats["xp_per_min"] * 1
    score += playerMatchStats["gold_per_min"] * 1
    return score ##Returns the total contribution score


def PlayerContributionPercentage(match_id, player_id):
    playersArray = data_scraper.ListPlayersinMatch(match_id)
    teamContributionTotal = 0.0
    for player_id in playersArray: ##Loops through every player's contibutions
        teamContributionTotal += PlayerContributionScore(match_id, player_id)
    return PlayerContributionScore(match_id, player_id)/teamContributionTotal


def GetProbability(ppsA, ppsB):
    return 1/(1+10**((ppsB - ppsA)/400))  ##If the difference is 400 the chance of winning is 10x high


def CalculatePPSChange(ppsA, ppsB):
    eloConstant = 32  ##Elo constant can be altered
    pA = GetProbability(ppsA, ppsB) ##Gets the probability of player A winning
    temp = round(eloConstant * (1 - pA), 0) ##Converts the change into an integer
    change = int(temp)  ##Change is always an int
    return change


def GetPPS(playerID):
    if playerPPS[playerID] is None:
        playerPPS[playerID] = 1000
    return playerPPS[playerID]


def InitialPPS():
    for i in data_scraper.ListAllPlayerIDs(): ##Loops through every player
        playerPPS[i] = 1000 ##Sets the player's PPS to 1000


def AveragePPS(team):
    total = 0
    for i in team: ##Loops through each player in the team
        total += playerPPS.get(i) ##Adds the player's PPS to the total
    return total//i ##Returns the mean average PPS

def TotalPPS(team):
    total = 0
    for i in team:  ##Loops through each player in the team
        total += playerPPS.get(i)  ##Adds the player's PPS to the total
    return total  ##Returns the total PPS


def SetPlayersNewPPS():
    print ("Updating player PPS...")
    for match in data_scraper.matchArray: ##Loops through all matches
        team1 = []
        team2 = []
        i = 0
        for player in match["players"]: ##Loops through each player in the match
            if player["isRadiant"]: ##Checks if the player is on team 1 or 2
                team1.append(player["account_id"]) ##Adds the player to the team
            else:
                team2.append(player["account_id"])
        changeInPPS = 5 * (CalculatePPSChange(AveragePPS(team1), AveragePPS(team2))) ##Calculates the change in PPS based on the averages of the two teams
        if match["radiant_win"]: ##Checks if team 1 won
            for player in match["players"]: ##Loops through each player in the match
                weight = PlayerContributionPercentage(match["match_id"], player["account_id"]) ##Works out the individual player's PPS change based on their contribution
                if player["isRadiant"]: ##Checks if the player was on the winning team
                    playerPPS[player["account_id"]] += changeInPPS * weight ##Increases the player's PPS if they won
                else:
                    playerPPS[player["account_id"]] -= changeInPPS * weight ##Decreases the player's PPS if they lost
        else:
            for player in match["players"]:
                weight = PlayerContributionPercentage(match["match_id"], player["account_id"])
                if player["isRadiant"]:
                    playerPPS[player["account_id"]] -= changeInPPS * weight
                else:
                    playerPPS[player["account_id"]] += changeInPPS * weight


#### Main ####
InitialPPS() ##Sets every player's PPS to 1000
SetPlayersNewPPS() ##Calculates new PPS based on all match data
if __name__ == "__main__":
    print(data_scraper.DictPlayerInfo(135878232))
    print(data_scraper.DictPlayerMatchStats(4967600837, 135878232))
    print(PlayerContributionPercentage(4967600837, 135878232))


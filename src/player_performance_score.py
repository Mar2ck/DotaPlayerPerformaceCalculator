#!/usr/bin/env python3
"""
Player Performance Score (ELO inspired) Calculations
"""
# Built-in modules
import json
# Local modules
import data_scraper


def GetProbability(ratingA, ratingB):
    return 1/(1+10**((ratingB - ratingA)/400))  # if the difference is 400 the chance of winning is 10x high


def CalculateRatingChange(ratingA, ratingB, winner):
    eloConstant = 32  # Can be changed
    pA = GetProbability(ratingA, ratingB)
    pB = 1 - pA
    change = int(round(eloConstant * (1 - pA)), 0)  # Change is alwways an int
    if winner == 1:
        ratingA += change
        ratingB -= change
    else:
        ratingB += change
        ratingA -= change
    return ratingA, ratingB


print(data_scraper.DictPlayerInfo(19672354))

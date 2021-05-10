#!/usr/bin/env python3
"""
Player Performance Score (ELO inspired) Calculations
"""
# Built-in modules
import json
# Local modules
import data_scraper


def GetProbability(ppsA, ppsB):
    return 1/(1+10**((ppsB - ppsA)/400))  # if the difference is 400 the chance of winning is 10x high


def CalculatePPSChange(ppsA, ppsB, winner):
    eloConstant = 32  # Can be changed
    pA = GetProbability(ppsA, ppsB)
    pB = 1 - pA
    change = int(round(eloConstant * (1 - pA)), 0)  # Change is alwways an int
    if winner == 1:
        ppsA += change
        ppsB -= change
    else:
        ppsB += change
        ppsA -= change
    return ppsA, ppsB


print(data_scraper.DictPlayerInfo(19672354))

#!/usr/bin/env python3
"""
OpenDota API Interface
"""
# Built-in modules
import json
import pathlib
import os
import time
# PyPi modules
import requests

matchListFileArray = []

PROJECT_DIR = pathlib.Path(os.path.abspath(__file__)).parent.parent
DATA_DIR = PROJECT_DIR.joinpath("data")
for file in DATA_DIR.iterdir():
    if file.is_file():
        matchListFileArray.append(file)


def _DownloadMatchData():
    # List available match lists
    for fileId in range(len(matchListFileArray)):
        print("[{}]".format(fileId + 1), matchListFileArray[fileId].stem)

    # Pick match list to download
    while True:
        try:
            fileIdSelected = int(input("Select file: ")) - 1
        except ValueError:
            print("Invalid selection")
            continue
        if 0 <= fileIdSelected <= (len(matchListFileArray) - 1):
            break
        else:
            print("Selection out of range")

    # Download matches to folder
    matchListFileJson = json.load(open(matchListFileArray[fileIdSelected]))
    for matchEntry in matchListFileJson:
        matchEntryFileSavePath = pathlib.Path.joinpath(DATA_DIR,
                                                       matchListFileArray[fileIdSelected].stem,
                                                       str(matchEntry["match_id"]) + ".json")
        matchEntryApiAddress = "https://api.opendota.com/api/matches/" + str(matchEntry["match_id"])
        print(matchEntryApiAddress)
        print(matchEntryFileSavePath)
        matchEntryJson = requests.get(matchEntryApiAddress)
        # matchEntryJson = str(matchEntry["match_id"])  # Test text

        # Writing contents
        matchEntryFileSavePath.parent.mkdir(parents=True, exist_ok=True)  # Create parent folders for entry files
        matchEntryFile = open(matchEntryFileSavePath, "w", encoding='utf-8', errors='ignore')
        matchEntryFile.write(matchEntryJson.text)
        matchEntryFile.close()

        print("")
        time.sleep(2)  # Wait between each request to avoid rate limit


if __name__ == "__main__":
    _DownloadMatchData()

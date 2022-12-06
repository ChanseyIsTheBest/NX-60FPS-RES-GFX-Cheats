import os
import urllib.request, urllib.parse
import json

response = urllib.request.urlopen(
    'https://raw.githubusercontent.com/HamletDuFromage/switch-cheats-db/master/versions.json')
allVersions = json.load(response)

table = """# Games List
A list of all games with cheats.

Currently contains {numCheats} cheat files for {numTitles} titles.

| No | NAME | TITLE ID | BUILD ID | VERSION |
| --- | --- | --- | --- | --- |
"""

numCheats = 0
tableItems = []

for title in os.listdir("titles"):
    cheats = [file.removesuffix(".txt") for file in os.listdir(os.path.join("titles", title, "cheats"))]
    names = [file.removesuffix(".txt") for file in os.listdir(os.path.join("titles", title)) if file.endswith(".txt")]
    if len(names) != 0:
        name = names[0]
    else:
        name = "Unknown"
    cheatsLinked = [f"[{cheat}](titles/{title}/cheats/{cheat}.txt)" for cheat in cheats]
    if(not title in allVersions):
        # print(f"Missing version information for {title}")
        versions = []
    else:
        versions = [version for version in allVersions[title].items() if version[1] in cheats]
    
    versionsLinked = [f"[{version[0]}](titles/{title}/cheats/{version[1]}.txt)" for version in versions]
    versionsLinked.sort()

    nameLink = urllib.parse.quote(f"titles/{title}/{name}.txt")
    tableItems.append(f"[{name}]({nameLink}) | [{title}](titles/{title}) | {', '.join(cheatsLinked)} | {', '.join(versionsLinked)} |")
    numCheats += len(cheats)

table = table.replace("{numCheats}", str(numCheats))
table = table.replace("{numTitles}", str(len(tableItems)))

tableItems.sort()
table += "\n".join([f"| {i+1} | {item}" for i, item in enumerate(tableItems)])

if(os.path.exists("GAMES.md")):
    existingGames = open("GAMES.md", "r", encoding="utf-16").read()
    if existingGames != table:
        open("GAMES.md", "w", encoding="utf-16").write(table)
        print("true")
    else:
        print("false")
else:
    open("GAMES.md", "w", encoding="utf-16").write(table)
    print("true")

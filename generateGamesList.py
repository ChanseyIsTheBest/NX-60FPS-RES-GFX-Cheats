import os

table = """# Games List
A list of all games with cheats.

Currently contains {numCheats} cheats for {numTitles} titles.

| No | NAME | TITLE ID | BUILD ID |
| --- | --- | --- | --- |
"""

i = 1
numCheats = 0

for title in os.listdir("titles"):
    cheats = [file.removesuffix(".txt") for file in os.listdir(os.path.join("titles", title, "cheats"))]
    names = [file.removesuffix(".txt") for file in os.listdir(os.path.join("titles", title)) if file.endswith(".txt")]
    if len(names) != 0:
        name = names[0]
    else:
        name = "Unknown"
    cheatsLinked = [f"[{cheat}](titles/{title}/cheats/{cheat}.txt)" for cheat in cheats]
    table += f"| {i} | {name} | [{title}](titles/{title}) | {', '.join(cheatsLinked)} |\n"
    i += 1
    numCheats += len(cheats)

table = table.replace("{numCheats}", str(numCheats))
table = table.replace("{numTitles}", str(i - 1))

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
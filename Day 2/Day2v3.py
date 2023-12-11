import sys
import time

COLORS = ["red", "blue", "green"]
MAXBALLS = {
    "red": 12,
    "blue": 14,
    "green": 13
}
games = {}
for i in range(0,100):
    games[i] = None
print(games)

def import_file():
    try:
        return open(sys.argv[1])
    except FileNotFoundError:
        print("File could not be opened.")
        quit
    except IndexError:
        print("Program requires an argument for the input file.")
        quit() 

def parser(file):
    gameNum = 0
    for line in file:
        startPoint = line.find(":") + 2
        running = True
        isNum = False
        word = ""
        num = 0
        game = []
        subgame = []
        part = []
        while running:
            try:
                char = line[startPoint]
            except IndexError:
                subgame.append(part)
                game.append(subgame)
                running = False

            startPoint += 1
            word += char
            print(word)
            try:
                num = int(word.strip())
                if(line[startPoint] == " "):
                    part.append(num)
                    word = ""
            except ValueError:
                pass

            if(word.strip() in COLORS):
                print("color")
                part.append(word.strip())
                word = ""
            if(char == ","):
                print("comma")
                subgame.append(part)
                word = ""
                print(subgame)
                part = []
            elif(char == ";"):
                print("semi")
                subgame.append(part)
                part = []
                word = ""
                game.append(subgame)
                subgame = []
        games[gameNum] = game
        gameNum = gameNum + 1
    return 0

if __name__ == "__main__":
    file = import_file()
    parser(file)
    #games[game][subgame][part][0: num, 1: color]
    #
    
    #Part 1
    # impossibleGames = []
    # possibleGames = []
    # totalId = 0
    # for i in range(0,100):
    #     isPossible = True
    #     game = games[i]
    #     for subgame in game:
    #         for part in subgame:
    #             match part[1]:
    #                 case "red":
    #                     if(part[0] > MAXBALLS['red']):
    #                         isPossible = False
    #                 case "blue": 
    #                     if(part[0] > MAXBALLS['blue']):
    #                         isPossible = False
    #                 case "green": 
    #                     if(part[0] > MAXBALLS['green']):
    #                         isPossible = False
    #     if isPossible:
    #         totalId = totalId + i + 1
    #         possibleGames.append(i + 1)
    #         possibleGames.append(game)
    #     else:
    #         impossibleGames.append(i + 1)
    #         impossibleGames.append(game)
    # for x in possibleGames:
    #     print(x)
    # print(totalId)

    #Part 2
    total = 0
    for i in range(0,100):
        game = games[i]
        print(game)
        minRed = None
        minBlue = None
        minGreen = None
        firstRed = True
        firstBlue = True
        firstGreen = True
        for subgame in game:
            for part in subgame:
                match part[1]:
                    case "red":
                        if firstRed:
                            minRed = part[0]
                            firstRed = False
                        elif(part[0] > minRed):
                            minRed = part[0]
                    case "blue":
                        if firstBlue:
                            minBlue = part[0]
                            firstBlue = False
                        elif(part[0] > minBlue):
                            minBlue = part[0]
                    case "green":
                        if firstGreen:
                            minGreen = part[0]
                            firstGreen = False
                        elif(part[0] > minGreen):
                            minGreen = part[0]

        total += minRed * minBlue * minGreen 
    print(total)
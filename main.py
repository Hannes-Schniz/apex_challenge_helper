import random
import sys

Apex_Legends_Characters = sorted(['Ash','Fuse','Mad Maggie','Bangalore','Ballistic','Alter','Wraith','Mirage','Octane','Horizon','Valkyrie','Pathfinder','Revenant','Bloodhound','Crypto','Seer','Vantage','Caustic','Wattson','Rampart','Catalyst','Conduit','Lifeline','Loba','Gibraltar','Newcastle'])


testChallenges =[[18,22,8],[3,5,15],[15,25,23],[3,1,19],[22,25,9],[10,13,14],[25,24,11],[18,1,2],[8,9,10],[2,4,13],[18,16,14],[22,10,13],[11,16,12],[25,17,20],[8,11,4],[10,17,7],[18,5,21]] 


def print_characters():
    for i in range(len(Apex_Legends_Characters)):
        print(f"{i}. {Apex_Legends_Characters[i]}")

def input_challenge():
    user_input = input("Please select 3 Characters from the list above separated by commas: ")
    reti = []
    for c in user_input.split(','):
        reti.append(int(c))
    return reti


def getChallenges():
    print_characters()
    user_input = input_challenge()
    challenges = []
    while len(user_input) == 3:
        challenges.append(user_input)
        user_input = input_challenge()
    return challenges

def makeDict(challenges: list):
    charDict = {}
    while len(challenges) > 0:
        curr:list = challenges.pop()
        for c in curr:
            if c in charDict.keys():
                newValue = charDict[c]
                newValue.append(curr)
                charDict[c] = newValue
                continue
            charDict[c] = [curr]
        
    return charDict
        
def getCharacterChalSize(charDict:dict):
    amounts = []
    for key in charDict.keys():
        amounts.append((key, len(charDict.get(key))))
    return amounts


def printList(amontList):
    for amount in amontList:
        print(amount)


def updateDict(charDict:dict, key):
    values = charDict.pop(key)
    for key in charDict.keys():
        charDict[key] = [x for x in charDict.get(key) if x not in values]


def buildGreedyPath(charDict:dict, path:list):
    if len(charDict.keys()) == 0:
        return path
    sortedAmounts = sorted(getCharacterChalSize(charDict), reverse=True, key=lambda x: x[1])
    path.append(Apex_Legends_Characters[sortedAmounts[0][0]])
    updateDict(charDict, sortedAmounts[0][0])
    return buildGreedyPath(charDict, path)        

def getGreedyPath(charDict:dict):
    greedyPath = buildGreedyPath(charDict.copy(), [])
    print(len(greedyPath))
    printList(greedyPath)

def buildLessGreedyPath(charDict:dict, path:list):
    if len(charDict.keys()) == 0:
        return path
    charChalSizes= sorted(getCharacterChalSize(charDict), reverse=True, key=lambda x: x[1])
    maxAmounts = []
    for character in [x[0] for x in charChalSizes if x[1] is charChalSizes[0][1]]:
        values = charDict.get(character)
        currAmount = [len(x) for x in values]
        maxAmounts.append((character, currAmount))
    
    maxAmounts= sorted(maxAmounts, reverse=True, key=lambda x: x[1])
    path.append(Apex_Legends_Characters[maxAmounts[0][0]])
    updateDict(charDict, maxAmounts[0][0])
    return buildLessGreedyPath(charDict, path)

def getLessGreedyPath(charDict:dict):
    greedyPath = buildLessGreedyPath(charDict.copy(), [])
    print(len(greedyPath))
    printList(greedyPath)
    

def buildRandomPath(charDict:dict, path:list):   
    if len(charDict.keys()) == 0:
        return path
    key = random.choice([x for x in charDict.keys()])
    path.append(Apex_Legends_Characters[key])
    updateDict(charDict, key)
    return buildRandomPath(charDict, path)

def getRandomPath(charDict:dict, runs:int):
    bestPath= buildRandomPath(charDict.copy(), [])
    for i in range(runs):
        newPath = buildRandomPath(charDict.copy(), [])
        print('Calculating best Route: ' + str(round(100 / (runs -1) * i, 1)) +'%', end='\r', flush=True)
        if len(newPath) < len(bestPath):
            bestPath = newPath
    print()
    print(len(bestPath))
    printList(bestPath)

# A Dictionary of characters that shows which challenges get completed if a character is played
challenge_Dictionary = makeDict(testChallenges)

print()
print("Greedy Path:")
getGreedyPath(challenge_Dictionary)

print()
print("Double weighted path:")
getLessGreedyPath(challenge_Dictionary)

revisions = 100000000
print()
print("Random path with", revisions, "revision:")
getRandomPath(challenge_Dictionary, revisions)

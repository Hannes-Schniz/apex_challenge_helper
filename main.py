


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
        amounts.append((Apex_Legends_Characters[key], len(charDict.get(key))))
    return amounts


def printAmount(amontList):
    for amount in amontList:
        print(amount)

#challenges = getChallenges()
#
#graph = constructCharacterGraph([x for x in challenges])
#
#print(challenges)
#
#
#printCharacters(challenges,graph)
#     

# A Dictionary of characters that shows which challenges get completed if a character is played
challenge_Dictionary = makeDict(testChallenges)

#for key in sorted(challenge_Dictionary.keys()):
#    print(Apex_Legends_Characters[key], [[Apex_Legends_Characters[y] for y in x] for x in challenge_Dictionary.get(key)])

sortedAmounts = sorted(getCharacterChalSize(challenge_Dictionary), reverse=True, key=lambda x: x[1])

printAmount(sortedAmounts)
#printAmount(getCharacterChalSize(challenge_Dictionary))

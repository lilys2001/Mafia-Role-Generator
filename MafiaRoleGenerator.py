import time, random

print("Mafia Role Generator")
numPlayers = int(input("How many players are there? "))

# not enough players
if numPlayers < 1:
    print("That's not possible.")
else:
    numLGMMB = 0

    if numPlayers > 8:
        additionalRoles = input("Would you like to play with special roles? (yes or no) ").lower()

        while additionalRoles != "yes" and additionalRoles != "no":
            print("invalid response")
            additionalRoles = input("Would you like to play with special roles? (yes or no) ").lower()

        if additionalRoles == "yes":
            numLGMMB = 1
        elif additionalRoles == "no":
            numLGMMB = 0

    namePlayers = []
    roles = []

    # gets names of players
    i = 0
    while i < numPlayers:
        namePlayers.append(input("What is your name? "))
        i += 1

    # scale to 1 mafia, 1 doctor, 1 police, 2 civilians
    scale = numPlayers // 5
    numMDP = scale
    numCiv = numPlayers - (scale * 3) - (numLGMMB * 3)

    def generateRoles(role, num):
        i = 0
        while i < num:
            roles.append(role)
            i += 1

    generateRoles("Mafia (you can collectively kill 1 player each night)", numMDP)
    generateRoles("Doctor (you can save 1 player each night)", numMDP)
    generateRoles("Police (you can check 1 player each night)", numMDP)
    generateRoles("Civilian", numCiv)
    generateRoles("Little Girl (you can peek when the Mafia are woken up)", numLGMMB)
    generateRoles("Muter (you can mute 1 player)", numLGMMB)
    generateRoles("Mafia Boss (you are part of the mafia, but are invisible to the police)", numLGMMB)

    random.shuffle(roles)

    print("Printing Roles...")

    # prints roles
    i = 0
    while i < numPlayers:
        time.sleep(3)
        print(chr(27) + "[2J")
        print(namePlayers[i] + ": " + roles[i])
        time.sleep(3)
        print("Next Player")
        time.sleep(1)
        print(chr(27) + "[2J")
        i += 1

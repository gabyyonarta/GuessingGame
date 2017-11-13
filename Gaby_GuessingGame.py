import random

def main():
    playerone = 0
    playertwo = 0
    rounds = 0
    replay = 'Y'

    while replay == 'Y' or replay == 'y':
        difficulty = int(input("Welcome! Choose your difficulty - 1 (Easy), 2 (Hard)"))
        if difficulty == 1:
            while playerone < 10 and playertwo < 10:
                print("-Player One-")
                randomnumber = random.randrange(1, 11)
                humanguess = 0
                while humanguess != randomnumber:
                    humanguess = int(input("Guess a Number(1-10)"))
                    playerone = playerone + 1
                    if humanguess < randomnumber:
                        print("higher")
                    elif humanguess > randomnumber:
                        print("lower")
                    else:
                        print("Player 1 took " + str(playerone) + " tries to get the right answer.")
                        break

                print("-Player Two-")
                randomnumber = random.randrange(1, 11)
                humanguess = 0
                while humanguess != randomnumber:
                    humanguess = int(input("Guess a Number(1-10)"))
                    playertwo = playertwo + 1
                    if humanguess < randomnumber:
                        print("higher")
                    elif humanguess > randomnumber:
                        print("lower")
                    else:
                        print("Player 2 took " + str(playertwo) + " tries to get the right answer.")
                        break

            if playerone < playertwo:
                print("Player One Wins!")
            elif playerone > playertwo:
                print("Player Two Wins!")
            else:
                print("It's a Tie!")



        elif difficulty == 2:
            while playerone < 15 and playertwo < 15:
                print("-Player One-")
                randomnumber = random.randrange(1, 51)
                humanguess = 0
                while humanguess != randomnumber:
                    humanguess = int(input("Guess a Number(1-100)"))
                    playerone = playerone + 1
                    if humanguess < randomnumber:
                        print("higher")
                    elif humanguess > randomnumber:
                        print("lower")
                    else:
                        print("Player One took " + str(playerone) + " tries to get the right answer.")
                        break

                print("-Player Two-")
                randomnumber = random.randrange(1, 51)
                humanguess = 0
                while humanguess != randomnumber:
                    humanguess = int(input("Guess a Number(1-100)"))
                    playertwo = playertwo + 1
                    if humanguess < randomnumber:
                        print("higher")
                    elif humanguess > randomnumber:
                        print("lower")
                    else:
                        print("Player Two took " + str(playertwo) + " tries to get the right answer.")
                        break

            if playerone < playertwo:
                print("Player One Wins!")
            elif playerone > playertwo:
                print("Player Two Wins!")
            else:
                print("It's a Tie!")

        else:
            while playerone < 15 and playertwo < 15:
                print("-Player One-")
                randomnumber = random.randrange(1, 20)
                humanguess = 0
                while humanguess != randomnumber:
                    humanguess = int(input("Guess a Number(1-100)"))
                    playerone = playerone + 1
                    if humanguess < randomnumber:
                        print("higher")
                    elif humanguess > randomnumber:
                        print("lower")
                    else:
                        print("Player One took " + str(playerone) + " tries to get the right answer.")
                        break

            print("-Player Two-")
            randomnumber = random.randrange(1, 100)
            humanguess = 0
            while humanguess != randomnumber:
                humanguess = int(input("Guess a Number(1-100)"))
                playertwo = playertwo + 1
                if humanguess < randomnumber:
                    print("higher")
                elif humanguess > randomnumber:
                    print("lower")
                else:
                    print("Player Two took " + str(playertwo) + " tries to get the right answer.")
                    break

            if playerone < playertwo:
                print("Player One Wins!")
            elif playerone > playertwo:
                print("Player Two Wins!")
            else:
                print("It's a Tie!")

        playerone = 0
        playertwo = 0
        replay = raw_input("Would you like you play again? (Y/N)")

main()
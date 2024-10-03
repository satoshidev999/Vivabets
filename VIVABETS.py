import random

def intro_banner():
    s = "Welcome to the Game!"
    
    print(s)

def game_over():
    s = "Game Over. Bye!"

    print(s)
    
def main():
    intro_banner()

    playername = input('Player Name >> ')
    money = 50
    print("Welcome to the game, " + playername + ". Your starting amount is " + str(money) + ' Gold.')

    keepplaying = True
    while keepplaying:
        bet = input("Place your bet >> ")
        isbetnotvalid = int(bet) > money or int(bet) < -1
        while isbetnotvalid:
            print("Please enter a valid bet.")
            bet = input("Place fix your bet >> ")
            isbetnotvalid = int(bet) > money or int(bet) < -1

        bet = int(bet)

        player_card = random.randint(1, 12)
        cpu_card = random.randint(1, 12)

        print("Your card is " + str(player_card) + ". CPU card is " + str(cpu_card) + ".")

        if player_card == cpu_card:
            print("It's a DRAW! CPU wins because that's how it is.")
            money = money - bet
        elif player_card > cpu_card:
            print("You win " + str(bet) + " Gold!")
            money = money + bet
        else:
            print("CPU wins! You lose " + str(bet) + " Gold!")
            money = money - bet

        if money < 0:
            print("You're out of money!")
            game_over()
            keepplaying = False
        else: 
            print("Your money is now " + str(money) + " Gold.")
            ask = input("Do you want to keep playing? [y/N] >> ")
            if ask == 'y' or ask == 'Y':
                keepplaying = True
            else:
                print("You're leaving with " + str(money) + " Gold. Bye.")
                game_over()
                keepplaying = False
main()
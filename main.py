import os
import sys
import random
import time
from pyfiglet import Figlet
from chips import Chips
from betting import Bets

# all numbers on wheel in order; used to 'realistically' simulate ball bounce in one
# direction. dictionary key is the number on the wheel, and the
# value is a list of corresponding attributes of that number a player can bet on
WHEEL = {
    "0": ["GREEN", "NONE", "NONE", "NONE", "NONE"],
    "32": ["RED", "EVEN", "19_36", "3rd_12", "COL_2"],
    "15": ["BLACK", "ODD", "1_18", "2nd_12", "COL_3"],
    "19": ["RED", "ODD", "19_36", "2nd_12", "COL_1"],
    "4": ["BLACK", "EVEN", "1_18", "1st_12", "COL_1"],
    "21": ["RED", "ODD", "19_36", "3rd_12", "COL_3"],
    "2": ["BLACK", "EVEN", "1_18", "1st_12", "COL_2"],
    "25": ["RED", "ODD", "19_36", "3rd_12", "COL_1"],
    "17": ["BLACK", "ODD", "1_18", "2nd_12", "COL_2"],
    "34": ["RED", "EVEN", "19_36", "3rd_12", "COL_1"],
    "6": ["BLACK", "EVEN", "1_18", "1st_12", "COL_3"],
    "27": ["RED", "ODD", "19_36", "3rd_12", "COL_3"],
    "13": ["BLACK", "ODD", "1_18", "2nd_12", "COL_1"],
    "36": ["RED", "EVEN", "19_36", "3rd_12", "COL_3"],
    "11": ["BLACK", "ODD", "1_18", "1st_12", "COL_2"],
    "30": ["RED", "EVEN", "19_36", "3rd_12", "COL_3"],
    "8": ["BLACK", "EVEN", "1_18", "1st_12", "COL_2"],
    "23": ["RED", "ODD", "19_36", "2nd_12", "COL_2"],
    "10": ["BLACK", "EVEN", "1_18", "1st_12", "COL_1"],
    "5": ["RED", "ODD", "1_18", "1st_12", "COL_2"],
    "24": ["BLACK", "EVEN", "19_36", "2nd_12", "COL_3"],
    "16": ["RED", "EVEN", "1_18", "2nd_12", "COL_1"],
    "33": ["BLACK", "ODD", "19_36", "3rd_12", "COL_3"],
    "1": ["RED", "ODD", "1_18", "1st_12", "COL_1"],
    "20": ["BLACK", "EVEN", "19_36", "2nd_12", "COL_2"],
    "14": ["RED", "EVEN", "1_18", "2nd_12", "COL_2"],
    "31": ["BLACK", "ODD", "19_36", "3rd_12", "COL_1"],
    "9": ["RED", "ODD", "1_18", "1st_12", "COL_3"],
    "22": ["BLACK", "EVEN", "19_36", "2nd_12", "COL_1"],
    "18": ["RED", "EVEN", "1_18", "2nd_12", "COL_3"],
    "29": ["BLACK", "ODD", "19_36", "3rd_12", "COL_2"],
    "7": ["RED", "ODD", "1_18", "1st_12", "COL_1"],
    "28": ["BLACK", "EVEN", "19_36", "3rd_12", "COL_1"],
    "12": ["RED", "EVEN", "1_18", "1st_12", "COL_3"],
    "35": ["BLACK", "ODD", "19_36", "3rd_12", "COL_2"],
    "3": ["RED", "ODD", "1_18", "1st_12", "COL_3"],
    "26": ["BLACK", "EVEN", "19_36", "3rd_12", "COL_2"],
}

# multipliers to calculate payout depending upon bet type
PAYOUT_RATE = {
    "BLACK": 2, "RED": 2,
    "EVEN": 2, "ODD": 2,
    "EXACT": 36,
    "1st_12": 3, "2nd_12": 3, "3rd_12": 3,
    "1_18": 3, "19_36": 3,
    "COL_1": 3, "COL_2": 3, "COL_3": 3,
}


def spin_wheel():
    # all numbers on wheel in order; used to 'realistically' simulate ball bounce
    wheel = WHEEL

    # use dictionary length so if a bounce index takes it past the last element
    # need to adjust the index to start over at the top of the list by the overage amount

    # generate random number between 0 and 36 for first ball landing
    rand_number = random.randint(0, 36)
    print(f"Ball lands on {rand_number} {wheel.get(str(rand_number))[0]} and bounces")
    new_index = list(WHEEL).index(str(rand_number))

    # timer is to simulate waiting for ball to fall into spots
    timer = 2
    # ball bounce random times
    rand = random.randint(2, 4)
    for i in range(rand):
        # ball will bounce between a range of spaces
        bounce = random.randint(5, 10)
        new_index += bounce
        if new_index > len(wheel) - 1:
            new_index = new_index - len(wheel)
        key = list(wheel)[new_index]
        time.sleep(timer)
        if i < rand - 1:
            print(f"Ball lands on {key} {wheel.get(str(key))[0]} and bounces")
            timer -= 0.33
        else:
            print(f"Ball finally stops on {key} {wheel.get(str(key))[0]}")

    # return where ball lands
    return key


def check_results(number, bet):
    winnings = 0  # return 0 if player lost
    winner = WHEEL.get(number)
    if bet.bet_type == "EXACT":
        if bet.pick == number:
            winnings = bet.wager * int(PAYOUT_RATE.get(bet.bet_type))

    # if the player's pick is in the winner list - cha ching
    if bet.pick in winner:
        winnings = bet.wager * int(PAYOUT_RATE.get(bet.bet_type))

    return winnings


def clear_scr():
    # Windows
    if os.name == "nt":
        os.system("cls")
    # Mac and Linux
    else:
        os.system("clear")

    figlet = Figlet()
    txt = "PLAY ROULETTE"
    figlet.setFont(font="doom")
    print(figlet.renderText(txt))


def main():
    # clear screen and display header
    clear_scr()
    chip = Chips()
    print("Welcome to the Roulette table.")
    print("Please accept some complimentary chips to get you started.")
    print("You can bet a little or you can bet all the chips you have.")
    print("You will be given the chance to buy more chips, if you want.\n")
    while True:
        bet = Bets()
        # display current chip balance (start with 200)
        print(f"Your balance is {chip.balance}.")
        # if chip balance is 0 ask if player wants to buy chips or quit game
        play = ""
        if chip.balance == 0:
            while play != "BUY" and play != "QUIT":
                play = input("Would you like to BUY chips or QUIT the game? ").upper()
            if play == "QUIT": sys.exit("Thanks for playing!")
        else:
            while play != "BUY" and play != "BET":
                play = input("Would you like to BUY chips or place a BET? ").upper()

        # by here play is either BET or BUY - Deal with buy first to fall into BET
        if play == "BUY":
            while True:
                if chip.buy_chips(input("How many chips would you like to BUY? ")): break
            print(f"Now your balance is {chip.balance}.")

        # play is now BET - ask player to make wager
        while True:
            if bet.make_wager(input("How many chips would you like to BET? "), chip): break

        # ask player what betting on make_pick()
        while True:
            print("How would you like to BET? ")
            if bet.make_pick(input(
                    "Select a number from 0-36, RED, BLACK, EVEN, ODD, 1st_12, \n2nd_12, 3rd_12, 1_18, 19_36, COL_1, "
                    "COL_2, COL_3 >>> ").upper()): break

        # call function to spin_wheel() - returns the final number ball lands on
        number = spin_wheel()

        # call function to check_results()
        winnings = check_results(number, bet)

        chip.deposit(winnings)
        # Display results and ask if player wants to QUIT of bet again
        if winnings == 0:
            print("Sorry, you lost!")
        else:
            print(f"Congrats! You won {winnings}!")

        print(f"You now have {chip.balance} chips.")

        play_again = ""
        while play_again != "Y" and play_again != "N":
            play_again = input("Would you like to continue playing Y/N ").upper()
            if play_again == "N": sys.exit("Thanks for playing!")

        # If player wants to continue playing clear the screen and return to top of loop
        clear_scr()


if __name__ == "__main__":
    main()

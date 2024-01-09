# list of all valid options player can enter for a bet
VALID_BETS = ['EVEN', 'ODD', 'BLACK', 'RED', '1st_12', '2nd_12', '3rd_12', '1_18', '19_36',
              'COL_1', 'COL_2', 'COL_3', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
              '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22',
              '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36']


class Bets:
    """ Manage betting """
    def __init__(self, pick="None"):
        # initialize bet
        self.pick = pick
        self.bet_type = pick
        self.wager = 0

    def set_pick(self, pick):
        self.pick = pick
        return self.pick

    def set_wager(self, wager):
        if int(wager) == 0:
            raise ValueError("ValueError: Wagers need to be more than 0.")

        self.wager = int(wager)
        return self.wager

    def set_bet_type(self, bet_type):
        self.bet_type = bet_type
        return self.bet_type

    def make_wager(self, wager, chip):
        if self.validate_wager(wager, chip):
            self.wager = int(wager)
            chip.withdraw(int(wager))
            return True

        return False

    def validate_wager(self, wager, chip):
        if not wager.isnumeric():
            print("Bets need to be written a number value")
            print(f"Your balance is {chip.balance}")
            return False

        if int(wager) > int(chip.balance):
            print("You do not have enough to cover this bet")
            print(f"Your balance is {chip.balance}")
            return False

        return True

    def make_pick(self, pick):
        if self.validate_pick(pick):
            self.pick = pick
            if pick.isnumeric():
                self.bet_type = "EXACT"
            else:
                self.bet_type = pick

            return True

        print("Invalid bet: Please enter a valid bet.")
        return False

    def validate_pick(self, pick):
        global VALID_BETS

        return True if pick in VALID_BETS else False

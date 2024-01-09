class Chips:
    """ manage chip account - be generous and default user with 200 chips """

    def __init__(self, balance=200):
        # initialize chips
        self.balance = balance

    def deposit(self, n):
        try:
            self.balance = self.balance + n
        except:
            raise ValueError("ValueError: Must be a number")

        return self.balance

    def withdraw(self, n):
        try:
            new_balance = self.balance - n
        except:
            raise ValueError("ValueError: Must be a number")

        if new_balance < 0:
            raise ValueError("ValueError: Not enough to cover bet")

        self.balance = new_balance
        return self.balance

    def buy_chips(self, chip_qty):
        if self.validate_buy(chip_qty):
            self.deposit(int(chip_qty))
            return True
        return False

    def validate_buy(self, chip_qty):
        if not chip_qty.isnumeric() or int(chip_qty) < 1:
            print("To buy chips, please enter a number")
            return False
        return True

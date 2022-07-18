class User:

    def __init__(self, name):
        self.name = name
        self.amount = 0

    def make_deposit(self, amount):
        self.amount += amount
        return self

    def make_withdrawl(self,amount):
        self.amount -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")
        return self

    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()
        return self


chaz = User("Chaz")
brock = User("Brock")
lester = User("Lester")

chaz.make_deposit(3400).make_deposit(1200).make_deposit(50).make_withdrawl(900).display_user_balance()

brock.make_deposit(17500).make_deposit(64000).make_withdrawl(1578).make_withdrawl(304).display_user_balance()

lester.make_deposit(3200).make_withdrawl(400).make_withdrawl(500).make_withdrawl(189).display_user_balance()

brock.transfer_money(400, chaz)
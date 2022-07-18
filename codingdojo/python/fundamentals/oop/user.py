class User:

    def __init__(self, name):
        self.name = name
        self.amount = 0

    def make_deposit(self, amount):
        self.amount += amount

    def make_withdrawl(self,amount):
        self.amount -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")

    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()


chaz = User("Chaz")
brock = User("Brock")
lester = User("Lester")

chaz.make_deposit(3400)
chaz.make_deposit(1200)
chaz.make_deposit(50)
chaz.make_withdrawl(900)
chaz.display_user_balance()

brock.make_deposit(17500)
brock.make_deposit(64000)
brock.make_withdrawl(1578)
brock.make_withdrawl(304)
brock.display_user_balance()

lester.make_deposit(3200)
lester.make_withdrawl(400)
lester.make_withdrawl(500)
lester.make_withdrawl(189)
lester.display_user_balance()


brock.transfer_money(400, chaz)
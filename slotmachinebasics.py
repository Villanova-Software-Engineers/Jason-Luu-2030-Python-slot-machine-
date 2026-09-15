class SlotMachine:
    def __init__(self, name, symbols, money):
        self.name = name
        self.symbols = symbols
        self.balance = money
    def spin(self):
        import random
        return random.choice(self.symbols)
    def deposit (self, amount):
        self.balance += amount
        print ('You have', str(amount) + ' dollars')
slots1 = slotmachine('firstSlot', ['a','b','c','d','e'], 10000)


slots1.deposit(int(input('what do you want to deposit')))

print(slots1.spin())

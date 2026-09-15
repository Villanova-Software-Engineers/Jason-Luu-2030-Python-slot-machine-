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
slots1 = SlotMachine('firstSlot', ['a','b','c','d','e'], 10000)


slots1.deposit(int(input('what do you want to deposit')))

result = [slots1.spin(),slots1.spin(),slots1.spin()], \
    [slots1.spin(),slots1.spin(),slots1.spin()], \
        [slots1.spin(),slots1.spin(),slots1.spin()]
winning_row = result[2]

for row in result:
    print(row)
if winning_row[1] == winning_row[2] and winning_row[1] == winning_row[3]:
    print('nice')
else:
    print('gamble again')
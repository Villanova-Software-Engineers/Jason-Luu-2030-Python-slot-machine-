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
slots1 = SlotMachine('firstSlot', ['a','b'], 10000)


def gamblingSequence():
    result = spinning()
    winning_row = result[1]
    for row in result:
         print(row)
    if winning_row[0] == winning_row[1] and winning_row[0] == winning_row[2]:
        print('nice')
        win = True
        retry = ''
    else: 
        retry = input('try again y or n')
    if retry == 'y' or win == False:
        result = ''
        for row in result:
            print(row)
        gamblingSequence()
        retry == ''

def spinning():
    return [ [slots1.spin(),slots1.spin(),slots1.spin()], \
             [slots1.spin(),slots1.spin(),slots1.spin()], \
             [slots1.spin(),slots1.spin(),slots1.spin()] ]


slots1.deposit(int(input('what do you want to deposit')))
gamblingSequence()


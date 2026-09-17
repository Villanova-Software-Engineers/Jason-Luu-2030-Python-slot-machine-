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
        print ('You have', str(amount) + ' dollars in the machine')
slots1 = SlotMachine('firstSlot', ['a','b','c','d','e'], 0)


def gamblingSequence():
    result = spinning()
    winning_row = result[1]
    for row in result:
         print(row)
    if winning_row[0] == winning_row[1] and winning_row[0] == winning_row[2]:
        slots1.balance *= 2
        print('You have doubled your deposit! You now have ' + str(slots1.balance) + ' dollars')
        win = True
        retry = ''
    else: 
        slots1.balance /= 2
        print("Don't go bankrupt. You only have " + str(slots1.balance) + " dollars left")
        retry = input('try again y or n ')
        win = False
    if retry == 'n' or retry != 'y' and win == False:
        print('no keep gambling your about to win big')
    if retry == 'y' and win == False:
        result = ''
        if slots1.balance < 10:
                print('your cooked bruh only ' + str(slots1.balance) + ' dollars')
        else:
            gamblingSequence()
            retry == ''
    

def spinning():
    return [ [slots1.spin(),slots1.spin(),slots1.spin()], \
             [slots1.spin(),slots1.spin(),slots1.spin()], \
             [slots1.spin(),slots1.spin(),slots1.spin()] ]


slots1.deposit(int(input('what do you want to deposit ')))
gamblingSequence()


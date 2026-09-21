class SlotMachine:
    def __init__(self, name, symbols, money):
        self.name = name
        self.symbols = symbols
        self.balance = money
    def spin(self):
        import random
        return random.choice(self.symbols)
    def deposit (self, amount, stake):
        self.balance -= stake
        print ('You have', str(stake) + ' dollars in the machine')
        self.stake = stake
slots1 = SlotMachine('firstSlot', ['a','b','c','d',], 10000)

def gamblingSequence():
    result = spinning()
    winning_row = result[1]
    fresh_start = False
    for row in result:
         print(row)
    if winning_row[0] == winning_row[1] and winning_row[0] == winning_row[2]:
        slots1.balance = slots1.balance + slots1.stake * 2 
        print('You have doubled your deposit! You now have ' + str(slots1.balance) + ' dollars')
        restarting()
    else: 
        print("You have " + '0' + " dollars left in the machine and need to put in more")
        print("There is only " + str(slots1.balance) + ' left in your savings')
        restarting()
def restarting():
    retry = input('try again y or n ')
    if retry == 'n' :
        print('no keep gambling your about to win big')
        restarting()
    elif retry == 'y': 
        result = ''
        slots1.deposit(slots1.balance, int(input('what do you want to deposit ')))
        if slots1.balance < 0 :
                print('your cooked bruh ' + str(slots1.balance) + ' dollars')
        else:
            gamblingSequence()
            retry == ''
    elif retry != 'y' or retry != 'n':
        retry = input('y or n ')
        restarting()
def spinning():
    return [ [slots1.spin(),slots1.spin(),slots1.spin()], \
             [slots1.spin(),slots1.spin(),slots1.spin()], \
             [slots1.spin(),slots1.spin(),slots1.spin()] ]

slots1.deposit(slots1.balance, int(input('what do you want to deposit. You have ' + str(slots1.balance) + ' left ')))
gamblingSequence()




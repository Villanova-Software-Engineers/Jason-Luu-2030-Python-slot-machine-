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
        print ('You put', str(stake) + ' dollars in the machine')
        self.stake = stake
slots1 = SlotMachine('firstSlot', ['a','b','c','d'], 10000)

def gamblingSequence():
    raw_result = spinning()
    result = [list(row) for row in zip(*raw_result)]
    winning_row = result[1]
    for row in result:
         print(" | ".join(row))
    if len(set(winning_row)) == 1:
        slots1.balance = slots1.balance + slots1.stake * 2 
        print('You have doubled your deposit! You now have ' + str(slots1.balance) + ' dollars.')
        restarting()
    else: 
        print("You have " + '0' + " dollars left in the machine and need to put in more.")
        print("There is only " + str(slots1.balance) + ' left in your savings.')
        restarting()
def restarting():
    retry = input('Try again! (y or n) ')
    if retry == 'n' :
        print('Keep gambling! You are about to win big!!!')
        restarting()
    elif retry == 'y': 
        result = ''
        slots1.deposit(slots1.balance, int(input('What do you want to deposit. ')))
        if slots1.balance < 0 :
                print("It's over bro has " + str(slots1.balance) + " dollars 💀")
        else:
            gamblingSequence()
            retry == ''
    elif retry != 'y' or retry != 'n':
        retry = input('You need to actually type y or n. ')
        restarting()
def spinning():
    return [ [slots1.spin(),slots1.spin(),slots1.spin()], \
             [slots1.spin(),slots1.spin(),slots1.spin()], \
             [slots1.spin(),slots1.spin(),slots1.spin()] ]

slots1.deposit(slots1.balance, int(input('What do you want to deposit. You have ' + str(slots1.balance) + ' left. ')))
gamblingSequence()




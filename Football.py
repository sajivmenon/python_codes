import random
import time
def coin_toss(coin):
    decide = random.choice(coin)
    return decide
team1 = input("What is your team's name?")
team2 = input("Choose another name for this team:")
print('%s vs %s' %(team1,team2))
print('Welcome to SuperBowl LI.')
coin1 = ['heads','tails']
choose1 = input('What do you choose for the coin toss, %s? Heads or Tails?' % team1)
cointoss1 = coin_toss(coin1)
print('It is %s' % cointoss1)
defense_switch = 'Not ready'
Offense_switch = 'Not ready'
while True:
    if choose1 == cointoss1 or defense_switch == 'Ready':
        print('You are offense')
        kickoff = random.randint(7,28)
        print('You will start off at the %d yard line.' % kickoff)
        down = 0
        while True:
            offense_choose1 = input('Do you want to run or pass?')
            if offense_choose1 == 'pass' or offense_choose1  == 'Pass':
                coinO1 = ['incomplete', 'complete']
                decO1 = coin_toss(coinO1) 
                print('Pass is %s' % decO1)
                if decO1 == 'complete':
                    yards = random.randint(15,50)
                    print('The pass went %d yards.'% yards)
                    down+=1
                else:
                    down += 1
                    print('It is %d down' % down)
            elif offense_choose1 == 'run' or offense_choose1 == "Run":
                yardage = random.randint(5,18)
                print('You ran %d yards' % yardage)
            if down > 4:
                Offense_switch = 'Ready'
                break
                
    elif choose1 != cointoss1 or Offense_switch == 'Ready':
        down=0
        print('You are defense.')
        while True: 
            dec = input('What do you chose? heads or tails.')
            print('If the coin favors you, the pass will be incomplete.')
            coinD1 = ['Heads','Tails']
            dec02 = coin_toss(coinD1)
            if dec02 == dec:
                print('Pass was incomplete')
                down += 1
            else:
                print('Pass was complete')
                yard = random.randint(12,45)
                print('Offense gained %d yards' % yard)
                down+=1
            if down > 4:
                defense_switch =  'Ready'
                break
                
     
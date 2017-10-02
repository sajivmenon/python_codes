map0 = {1:'Patriots',
       2:'Ravens',
       3:'Seahawks',
       4:'Broncos',
       5:'Steelers',
       6:'Packers',
       7:'Vikings',
       8:'Giants',
       9:'Falcons',
       10:'Cowboys',
       11:'Eagles',
       12:'49ers',
       13:'Rams',
       14:'Buffalo Bills',
       15:'Bucaneers',
       16:'Texans',
       17:'Titans',
       18:'Jets',
       19:'Browns',
       20:'Raiders',
       21:'Colts',
       22:'Jaguars',
       23:'Bengals',
       24:'Cardinals',
       25:'Dolphins'
       }
       
import random
import time
def coin_toss(coin):
    decide = random.choice(coin)
    print (decide)
    return decide
print('This is a 2 player game.')
print('Defense is automated')
team1ch = int(input("Enter a number from 1 to 25:"))
team1 = map0[team1ch]
print('Team 1 is %s' % team1)
team2ch = int(input("Opponent, Enter another numeber from 1 to 25:"))
team2 = map0[team2ch]
print('Team 2 is %s' % team2)
field = 100
print('%s vs %s' %(team1,team2))
print('Welcome to SuperBowl LI.')
coin1 = ['heads','tails']
choose1 = input('What do you choose for the coin toss, %s? Heads or Tails?' % team1)
choose1 = choose1.lower()
cointoss1 = coin_toss(coin1)
print('It is %s' % cointoss1)
Offense_switch = 'Not ready'
Offense_switch2 = 'Not ready'
field = 100
team1_points = 0
team2_points = 0
start = time.time()
while True:
        ## Code for 1st player
        if choose1 == cointoss1 or Offense_switch == 'Ready':
            print('%s are offense' % team1)
            kickoff = random.randint(10,28)
            print('You will start off at the %d yard line.' % kickoff)
            to_reach = 100-kickoff
            print('You have %d more yards to reach the endzone.'% to_reach)
            to_reach_1_down = 10
            down = 0
            first_down = 0
            while True:
                ##Choose wheather you want to run or pass
                offense_choose1 = input('Do you want to run or pass?')
                ##If you want to pass
                if offense_choose1 == 'pass' or offense_choose1  == 'Pass':
                    coinO1 = ['complete','incomplete', 'complete']
                    decO1 = coin_toss(coinO1) 
                    print('Pass is %s' % decO1)
                    ## If complete
                    if decO1 == 'complete':
                        yards = random.randint(4,27)
                        to_reach = to_reach - yards
                        to_reach_1_down = to_reach_1_down - yards
                        print('The pass went %d yards.'% yards)
                        print('You have %d more yards to reach the endzone' % to_reach)
                        first_down = first_down + yards
                        if yards >= 10 or first_down >= 10:
                            down = 1
                            print('It is 1st and 10')
                            first_down = 0
                            to_reach_1_down = 10
                              
                        else:
                            down += 1
                            print('It is %d and %d' % (down, to_reach_1_down))
                            print('You have %d more yards to reach the endzone' % to_reach)
                    ## If incomplete
                    else:
                        down += 1
                        print('It is %d and %d' % (down,to_reach_1_down))
                        
                ##If you want to run
                if offense_choose1 == 'run' or offense_choose1 == "Run":
                    yards = random.randint(7,17)
                    tyards = yards - 9
                    print('You ran %d yards' % tyards)
                    to_reach = to_reach - tyards
                    to_reach_1_down = to_reach_1_down - tyards
                    print('You have %d more yards before the endzone' % to_reach)
                    first_down = first_down + tyards
                    if tyards >= 10 or first_down >= 10:
                        down = 1
                        print('It is 1st and 10')
                        first_down = 0
                        to_reach_1_down = 10
                        
                    else:
                        down += 1
                        print('It is %d and %d' %(down,to_reach_1_down))
                ## If towchdown happens
                if to_reach <= 0:
                    print('TOUCHDOWN!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                    team1_points += 6
                    print('%s currently have %d points' %(team1, team1_points))
                    choosetouch = input('Do you want to do a field goal or 2-pt conversion? type 2-pt if you want to do the 2-pt conversion.')
                    if choosetouch == 'field goal' or choosetouch == 'Field Goal':
                        team1_points += 1
                        print('%s has %d points right now' % (team1, team1_points))
                    elif choosetouch == '2-pt':
                        two_pt = ['complete','complete','incomplete']
                        comcon = random.choice(two_pt)
                        if comcon == 'complete':
                            team1_points += 2
                            print('%s has %d points right now' % (team1, team1_points))
                        else:
                            print('You didnt make it')
                    print('%s has %d points' %(team2, team2_points))
                    Offense_switch2 = 'Ready'
                    break
                if down > 4:
                    Offense_switch2 = 'Ready'
                    print('Sorry. You didnt make it')
                    choosefail = input('Do you want to go for a field goal or kickoff?')
                    if choosefail == 'field goal'or choosefail == 'Field goal':
                        field_goal = ['complete','complete','complete','incomplete','complete','complete']
                        comp = random.choice(field_goal)
                        if comp == 'complete':
                            team1_points += 3
                            print('%s has %d points' % (team1, team1_points))
                           
                        else:
                            print('You failed')
                            
                    else:
                        print('Kickoff is going to happen')
                    break
                
        ## Code for 2nd player
        if choose1 != cointoss1 or Offense_switch2 == 'Ready':
            print('%s are offense' % team2)
            kickoff1 = random.randint(10,28)
            print('You will start off at the %d yard line.' % kickoff1)
            to_reach1 = 100-kickoff1
            print('You have %d more yards to reach the endzone.'% to_reach1)
            down = 0
            first_down = 0
            to_reach_2_down = 10
            while True:
                ##Choose wheather you want to run or pass
                offense_choose2 = input('Do you want to run or pass?')
                ##If you want to pass
                if offense_choose2 == 'pass' or offense_choose2  == 'Pass':
                    coinO2 = ['incomplete', 'complete']
                    decO2 = coin_toss(coinO2) 
                    print('Pass is %s' % decO2)
                    ## If complete
                    if decO2 == 'complete':
                        yards2 = random.randint(4,27)
                        to_reach1 = to_reach1 - yards2
                        to_reach_2_down = to_reach_2_down - yards2
                        print('The pass went %d yards.'% yards2)
                        print('You have %d more yards to reach the endzone' % to_reach1)
                        first_down = first_down + yards2
                        if yards2 >= 10 or first_down >= 10:
                            down = 1
                            print('It is 1st and 10')
                            first_down = 0
                            to_reach_2_down = 10
                              
                        else:
                            down += 1
                            print('It is %d and %d' % (down,to_reach_2_down))
                    
                    ## If incomplete
                    else:
                        down += 1
                        print('It is %d down' % down)
                ##If you want to run
                if offense_choose2 == 'run' or offense_choose2 == "Run":
                    yards2 = random.randint(7,17)
                    tyards2 = yards2 - 9
                    print('You ran %d yards' % tyards2)
                    to_reach1 = to_reach1 - tyards2
                    to_reach_2_down = to_reach_2_down- tyards2
                    print('You have %d more yards before the endzone' % to_reach1)
                    first_down = first_down + tyards2
                    if tyards2 > 10 or first_down >= 10:
                        down = 1
                        print('It is 1st and 10')
                        first_down = 0
                        to_reach_2_down = 10
                    else:
                        down += 1
                        print('It is %d and %d' % (down,to_reach_2_down))
                ## If towchdown happens
                if to_reach1 <= 0:
                    print('TOUCHDOWN!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                    team2_points += 6
                    print('You currently have %d points' % team2_points)
                    choosetouch = input('Do you want to do a field goal or 2-pt conversion? type 2-pt if you want to do the 2-pt conversion.')
                    if choosetouch == 'field goal' or choosetouch == 'Field Goal':
                        team2_points += 1
                        print('%s has %d points right now' % (team2, team2_points))
                    elif choosetouch == '2-pt':
                        two_pt = ['complete','complete','incomplete']
                        comcon = random.choice(two_pt)
                        if comcon == 'complete':
                            team2_points += 2
                            print('%s has %d points right now' % (team2, team2_points))
                        else:
                            print('You didnt make it')
                            print('%s has %d points right now' % (team2, team2_points))
                            
                    print('%s has %d points' %(team2, team2_points))

                    print('%s has %d points' %(team1, team1_points))
                    Offense_switch = 'Ready'
                    break
                if down > 4:
                    Offense_switch = 'Ready'
                    print('Sorry. You didnt make it')
                    choosefail = input('Do you want to go for a field goal or kickoff?')
                    if choosefail == 'field goal'or choosefail == 'Field goal':
                        field_goal = ['complete','complete','complete','complete','incpmplete','complete','complete']
                        comp = random.choice(field_goal)
                        if comp == 'complete':
                            team2_points += 3
                            print('%s has %d points' % (team2, team2_points))
                        else:
                            print('You failed')
                            
                    else:
                        print('Kickoff is going to happen')
                    break

if team1_points > team2_points:
    print('%s wins SuperBowl LI' % team1)
else:
    print('%S wins SuperBowl LI' % team2)

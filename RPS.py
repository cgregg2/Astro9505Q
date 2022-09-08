# Independent work
# Rock Paper Scissors

import time

# Game continues to run if True
Game_on = True
# Game will "restart" if True by re-asking name (after game is complete)
Restart = True

# While Game is on, run through game
while Game_on==True:

#     If game is restarted, ask player names and welcome them
    if Restart== True:
        RPS = {'Player 1':'None', 'Input1':'None', 'Player 2': 'None', 'Input2':'None', 'Score':[0,0]}

        RPS['Player 1']=input('Player 1 Name: ')
        RPS['Player 2'] = input('Player 2 Name: ')

        print('\n\nWelcome players', RPS['Player 1'], 'and', RPS['Player 2']+"!\n\n")

    Max_Score = input('What score would you like to play to?\n')
    Score_int=False

    RPS['Score'] = [0,0]

    while Score_int==False:
        try:
            Max_Score = int(Max_Score)
            if Max_Score > 0:
                Score_int=True
            else:
                Max_Score = input('Invalid input, please input an integer...\n:')
        except:
            Max_Score = input('Invalid input, please input an integer...\n:')
        

    print('\nOkay! PLaying until a player reaches a score of ', Max_Score, '\n\n')
    time.sleep(0.5)

    while max(RPS['Score']) < Max_Score:
        print(RPS['Player 1']+"'s decsion,", RPS['Player 2'], 'please look away.\n')
        time.sleep(1)
        print(
            RPS['Player 1'], 'choose one of the following options:\n|Rock|Paper|Scissors|\n| 0  |  1  |    2   |\n'
        )
        RPS['Input1'] = input(RPS['Player 1']+"'s input: ")


        input1_false = True
        while input1_false == True:
            try:
                RPS['Input1'] = int(RPS['Input1'])
                if RPS['Input1']>2 or RPS['Input1']<0:
                    print('Invalid input, please choose another option...')
                    RPS['Input1'] = input(RPS['Player 1']+"'s input: ")
                elif 0<=RPS['Input1']<=2:
                    input1_false=False
            except:
                print('Invalid input, please choose another option...')
                RPS['Input1'] = input(RPS['Player 1']+"'s input: ")

        print('\n'*100)

        time.sleep(1)

        print(RPS['Player 2']+"'s decsion,", RPS['Player 1'], 'please look away.\n')
        print(
            RPS['Player 2'], 'choose one of the following options:\n|Rock|Paper|Scissors|\n| 0  |  1  |    2   |\n'
        )
        RPS['Input2'] = input(RPS['Player 2']+"'s input: ")
        input2_false = True
        while input2_false == True:
            try:
                RPS['Input2'] = int(RPS['Input2'])
                if RPS['Input2']>2 or RPS['Input2']<0:
                    print('Invalid input, please choose another option...')
                    RPS['Input2'] = input(RPS['Player 2']+"'s input: ")
                elif 0<=RPS['Input2']<=2:
                    input2_false=False
            except:
                print('Invalid input, please choose another option...')
                RPS['Input2'] = input(RPS['Player 2']+"'s input: ")

        print('\n'*100)

        time.sleep(0.5)

        if RPS['Input1'] == 0:
            if RPS['Input2'] == 0:
                print('Draw! Score remains the same.')
            if RPS['Input2'] == 1:
                print(RPS['Player 2'],'wins round!')
                RPS['Score'][1] += 1
            elif RPS['Input2']==2:
                print(RPS['Player 1'],'wins round!')
                RPS['Score'][0] += 1
        elif RPS['Input1'] == 1:
            if RPS['Input2'] == 0:
                print(RPS['Player 1'],'wins round!')
                RPS['Score'][0] += 1
            if RPS['Input2'] == 1:
                print('Draw! Score remains the same.')
            elif RPS['Input2']==2:
                print(RPS['Player 2'],'wins round!')
                RPS['Score'][1] += 1
        elif RPS['Input1'] == 2:
            if RPS['Input2'] == 0:
                print(RPS['Player 2'],'wins round!')
                RPS['Score'][1] += 1
            if RPS['Input2'] == 1:
                print(RPS['Player 1'],'wins round!')
                RPS['Score'][0] += 1
            elif RPS['Input2']==2:
                print('Draw! Score remains the same.')

        time.sleep(0.5)

        print('\nCurrent Score:', RPS['Score'],'\n\n')

        time.sleep(0.5)

    if RPS['Score'].index(max(RPS['Score'])) == 0:
        print('Congratulations', RPS['Player 1'], 'on your victory!\n')
    else:
        print('Congratulations', RPS['Player 2'], 'on your victory!\n')

    time.sleep(1)

    Play_Again = input('Would you like to play again (y/n)?\n')
    Valid_PlayAgain = False
    while Valid_PlayAgain == False:
        if Play_Again != 'y' and Play_Again != 'n':
            Play_Again = input('Would you like to play again (y/n)?\n')
        else:
            Valid_PlayAgain = True
            print('\n')
            if Play_Again=='n':
                Game_on=False
            else:
                Restart_game = input('Would you like to fully restart (y/n)?\n')
                Valid_Restart = False
                while Valid_Restart == False:
                    if Restart_game != 'y' and Restart_game != 'n':
                        Restart_game = input('Would you like to fully restart (y/n)?\n')
                    else:
                        Valid_Restart = True
                        print('\n')
                        if Restart_game=='n':
                            Restart=False

print('Thank you for playing RPS!\n')
time.sleep(1)
print('Good bye, world!\n\n')
time.sleep(1)

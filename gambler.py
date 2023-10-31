import random
stake  = int(input("stake="))
goal   = int(input("goal="))
trials = int(input("trials="))

# Run trialCount experiments that start with stake and terminate on

def SingleTrial(stake, trials):
    bets = 0
    cash=stake

    while cash > 0 and cash < goal:
        bets += 1
        if random.random() < 0.5:
            cash += 1
        else:
            cash -= 1

    return bets,  cash == goal

winslst=[]
betslst=[]
for t in range(trials):
    # Run one experiment.
    bets,win=SingleTrial(stake,goal)
    winslst.append(win)
    betslst.append(bets)

betssum= sum(betslst)
number_wins = sum(winslst)

     

print(winslst)
print(betslst)
print("-------- Results ---------")
print('Win ratio:'+str(number_wins/trials))
print('Avg # bets per trial: ' + str(betssum//trials))

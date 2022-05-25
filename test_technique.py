from diceroll import *
no_of_wins=0
no_of_lose=0
total_simulation=1000
f=open("dump.txt",'w')
won_bets=open("won.txt",'w')
start_balance=500
money_per_face=150
bets=[2,3]
def stat_Counter(start_balance):
	formatted_text=''
	while start_balance>=money_per_face:
		rolled=roll()
		money=win_lose(rolled,bets,money_per_face)
		formatted_text+=f"Cash:{start_balance},Your bets {bets} Rolled Bets {str(rolled)},PNL:{money}\n"
		start_balance+=money
		if start_balance>=1000:
			won_bets.write(formatted_text)
			won_bets.write("____________\n")
			return "Won"
	return "Lost"
for i in range (0,total_simulation):
	result=stat_Counter(start_balance)
	if result=="Won":
		no_of_wins+=1
	else:
		no_of_lose+=1
print (f"Wins :{no_of_wins} ,Loses :  {no_of_lose}")
print (f"Winning Probablity = {(no_of_wins/total_simulation)*100} %")
f.close()
won_bets.close()
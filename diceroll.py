import random
faces =['brick','spade','clubs','hearts','flag','crown']

def roll():
	result=[]
	for i in range (1,7):
		die=random.randint(0,5)
		result.append(die)
	return result
# print(roll())
# [1, 5, 1, 1, 5, 3]
def win_lose(rolls,bets,money_per_face):
	amount=0
	# print ("Rol ls are ",rolls)
	for items in bets:
		repeats=rolls.count(items)
		if repeats>=2:
			amount+= money_per_face*repeats
		else:
			amount-=money_per_face
	return amount
# trial
# money_per_face=10
# rolls=roll()
# bets=[1,3]
# print(win_lose(rolls,bets,money_per_face))



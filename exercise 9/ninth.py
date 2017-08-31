from random import randint

choice = int(raw_input("Enter Rock Paper or Scissors... 1 2 and 3 Respectivley: "))
compchoice = randint(1, 3)

def duel(user, comp):

	if user == comp:
		return 'Draw!'
	if user == 1:
		if comp == 3:
			return 'You win!'
		else: 
			return 'You lose! :('		
	if user == 2:
		if comp == 1:
			return 'You win!'
		else:
			return 'You lose! :('	
	if user == 3:
		if comp == 2:
			return 'You win!'
		else:
			return 'You lose! :('
		

outcome = duel(choice, compchoice)
print(outcome)


		
		
	

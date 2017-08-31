import random 

user = raw_input("Guess a number between 1 and 20, type exit to exit: ")



while user != "exit":
	a = random.randint(1, 5)
	user = raw_input("Guess a number between 1 and 20, type exit to exit: ")
	if user == a:
		print('You win! :)')
		a = random.randint(1, 5)
	else:
		print('Nope...')
		a = random.randint(1, 5)






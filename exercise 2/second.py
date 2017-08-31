name = raw_input("whats your name?: ")
born_year = int(raw_input("what year were you born?: "))
age_wanted = int(raw_input("What age do you want to find the date for?: "))


def agemagic(name, born, age):
	#print('Hello, ', name)
	#print('You will be ', age)
	#print('in the year', born + age)
	time = born + age
	preanswer = ['Hello,', str(name), 'you will be', str(age), 'in the year', str(time)]
	answer = ' '.join(preanswer)

	
	return answer
	

future_year = agemagic(name, born_year, age_wanted)
	
print(future_year)


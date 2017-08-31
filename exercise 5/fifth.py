mynumber = int(raw_input("pick a number and I will tell you its divisors: "))
w = []

def checkdivisors(num):
	x = range(2, num)
	
	for test in x:
		if mynumber % test == 0:
			w.append(test)
			print test
			
	return w

		
y = checkdivisors(mynumber)
print y

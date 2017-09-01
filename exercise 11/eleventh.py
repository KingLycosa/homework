num = int(raw_input("How many fibbonaci numbers would you like to generate?:"))


def fibnum(amt):
	loop = 0
	first = 0
	second = 1
	next = 0
	while loop < amt:
		loop += 1
		if loop <= 1:
			next = loop
		else:
			next = first + second
			first = second
			second = next
		print(next)
		
		
fibnum(num)

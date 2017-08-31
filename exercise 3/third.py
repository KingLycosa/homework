firstnumber = int(raw_input("pick the number you want to check for divisibility: "))
secondnumber = int(raw_input("what do you want to check if its divisible by?: "))


def check_division(number, dividedby):
	if number % dividedby == 0:
		answer = True
		print(str(number) + ' is divisible by ' + str(dividedby))
	else:
		answer = False
		print(str(number) + ' is not divisible by ' + str(dividedby))
	return answer


check_division(firstnumber, secondnumber)
	


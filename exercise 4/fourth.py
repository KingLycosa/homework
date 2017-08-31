abc = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
divide = int(raw_input("chose a number and i'll tell you which numbers in the list are smaller: "))

x = []

def lessthanfive(cba, div):
	for curnum in cba:
		if curnum < div:
			x.append(curnum)

	return x

xyz = lessthanfive(abc, divide)
print('there are ' + str(len(xyz)) + ' numbers less than' + str(divide) + 'in that list ' + ' and they are...')
print(xyz)


a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x = []

def evenlist(lst):
	for el in lst:
		if el % 2 == 0:
			x.append(el)
	return x

print(evenlist(a))


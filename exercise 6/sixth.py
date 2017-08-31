a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
x = []

def listoverlap(lone, ltwo):
	for checks in lone:
			if checks in ltwo:
				#print('if called')
				x.append(checks)
	return x

print listoverlap(a, b)

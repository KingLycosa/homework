uin = raw_input("enter a word and ill check if its a palindrome: ")
y = []

def isreverse(wrd):
	if uin[::-1] == uin:
		return True
	else:
		return False

print isreverse(uin)


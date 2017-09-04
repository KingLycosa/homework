usrinput = str(input("Give me a sentence to reverse: "))

def reverseIt(instr):
	split = usrinput.split(" ")	
	split.reverse()
	result = ' '.join(split)
	
	print(result)



reverseIt(usrinput)

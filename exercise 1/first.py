hworld = 'how now brown cow'

#
# dont know why i did this i just like the aesthetic of camel case i guess...
# 8292017
#

def camelCase(ostr):
	ostr = ostr.split( )
	for index, word in enumerate(ostr):

		if index == 0:
			#print('the first word is ')
			#print(word.lower())
			ostr[index] = word.lower()
		else:
			#print('the next word is')			
			#print(word.capitalize())
			ostr[index] = word.capitalize()
	nstr = ''.join(ostr)

	return nstr



test = camelCase(hworld)
#print('\r\r')
print(test)

#print(hworld)



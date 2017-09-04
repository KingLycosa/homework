import random
import string
import datetime

char = string.ascii_letters + string.digits + string.punctuation

leng = int(input("how long do you want your password to be?: "))
website = str(input("what is this password for?: "))



def genPass(length):
	cur = 0
	pas = []
	while cur < length:
		cur = cur + 1
		pas.append(random.choice(char))
	password = ''.join(pas)
	return password
		
print("\nYour new password is...")
newPass = genPass(leng)
print(newPass + "\n\n")


#open file with append (a) so u dont delete it all
with open('keychain.txt', 'a') as file:
	file.write("(" + website + ") Generated on " + str(datetime.datetime.now()) + "\n" + newPass + "\n\n")

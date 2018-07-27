x = raw_input()
vowel = ['a','e','i','o','u']
if x>='a' and x<='z':
	if x in vowel:
		print('vowel')
	else:
		print('consonant')
else:
	print('invalid')

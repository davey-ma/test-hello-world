print('Hello World')
naam = input('naam: ')
print('hallo ' + naam)
age = input('hoe oud ben je? ')
confirm = input('dus je bent ' + age + ' jaar oud? ')
if confirm == 'ja':
	print('nice')
elif confirm == 'nee':
	age2 = input('hoe oud ben je dan?: ')
	print('je bent ' + age2 + ' jaar oud')
home = input('woon je alleen?')
if home == 'ja':
	print('nice')
elif home == 'nee':
	home2 = input('met hoeveel woon je thuis? ')
	if home2 >= '3':
		home3 = input('heb je broers of zusses? ')
		if home3 == 'ja':
			input = home4('hoeveel? ')
			print(home4 + ' nice')
	elif home2 <= '3':
		print('nice')


	
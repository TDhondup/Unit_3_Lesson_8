print('-' * 65)
print('Morbid Predictions Program:')
print()

print('This program asks you for your current age and tells you the year that you will die(on average.)')
print()

age = input('What is your age today? ')
age = int(age)
birth = 2018 - age
birth = int(birth)
death = birth + 79

print('...thinking...')
print('...thinking...')
print('...thinking...')

print('You will die in the year...' + str(death) + '.')

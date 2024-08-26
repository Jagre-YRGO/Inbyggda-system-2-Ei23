import time

#my first comment
my_string = 'erik jagre'
my_age = 47
print(f'{my_string} detta är en sträng {my_age}')

#trying some basig string-methods (functions)
print(my_string.title())
print(my_string.upper())

#trying string concatination and typecast of int-object
print(my_string + ' ' + str(my_age))

#print a good bye greeting after some delay
time.sleep(1)
print(f'Good bye {my_string}')

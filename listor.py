#objekt av typen sträng och metoden upper
my_string = 'some characters'
print(my_string)
print(my_string.upper())

#skapa en enkel lista med 3 nollor
lista = [0,0,0]
print(lista)
print(lista[1])

#maniplulera element
lista[1] = 5
print(lista)
print(my_string[1])

#indexering
my_string = 'snart rast'
min_blandade_lista = [1,'apa',3.14,'erik']
print(min_blandade_lista[3])
print(min_blandade_lista[3][0])
min_blandade_lista[2] = 'k'
print(min_blandade_lista)
print(type(min_blandade_lista[0]))

#skriv ut typen av objekt
my_range = range(5)
print(type(my_range))
print(my_range)
print(list(my_range))

#skapa listor med range
my_range = range(5,11)
print(list(my_range))
my_range = range(10,101,10)
print(list(my_range))

#bestäm längd på en lista
min_string = 'lknsaflkjsafdlknasflkn'
print(len(min_string))
print(len('Jag pluggar elektronik på YRGO ei23'))

#anropa en strängmetod direkt på objektet
print('Jag pluggar elektronik på YRGO ei23'.upper())

#sortera en lista
listan = [6,7,2,9]
listan.sort()
print(listan)

#kopiera en lista
listan = [6,7,2,9]
my_tmp = listan[0:]
my_tmp.sort()
print(my_tmp)
print(listan)

#kopiera en lista
listan = [6,7,2,9]
my_tmp = listan.copy()
my_tmp.sort()
print(listan)
print(my_tmp)

#ta bort element
my_int = 10
my_new_int = my_int
my_new_int += 1
print(my_int)
print(my_new_int)
listan.pop(1)
print(listan)
listan.pop()
print(listan)
listan.insert(0, 55)
print(listan)
del listan[1]
print(listan)

#lsit comprehension
my_cubes = [i**2 for i in [1,2,3,4,5]]
print(my_cubes)
my_cubes = [i**2 for i in [1,2,3,4,5] if i == 3]
print(my_cubes)
my_cubes = [i**2 for i in range(10)]
print(my_cubes)

#enkel loop
for i in [1,2,3]:
    print(i)

#skriver ut 7:ans gångertabell
factors = list(range(1,11))
print(factors)
for i in factors:
    print(7*i)

    

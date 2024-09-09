import numpy

def calc_circum(dia):
    dia = float(dia)
    return dia*numpy.pi

try:
    dia = float(input('Ange diamaeter! '))
    print(f'Diamtern är {calc_circum(dia)}')
except ValueError:
    print('ange korrekt format!')

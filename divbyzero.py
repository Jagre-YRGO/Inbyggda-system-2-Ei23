numerator = input('ange täljare:')
denominator = input('ange nämnare:')

try:
    numerator = int(numerator)
    denominator = int(denominator)
    print(f'kvoten blir: {numerator/denominator}')
except ZeroDivisionError:
    print('kan inte dividera med 0!')
except ValueError:
    print('kan bara ta emot tal!')
except:
    print('nått konstigt hände')
else:
    print('allt gick bra- inget exception kastat')





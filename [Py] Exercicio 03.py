numero = int(input('Digite um numero: '))
if numero % 2 == 0:
    if numero < 0:
        print('O numero {} é par e negativo.'.format(numero))
    else:
        print('O numero {} é par e positivo.'.format(numero))
else:
    if numero < 0:
        print('O numero {} é impar e negativo.'.format(numero))
    else:
        print('O numero {} é impar e positivo.'.format(numero))
print('LAÇOS DE REPETIÇÂO EM PYTHON')
print()

print(' *** WHILE *** ')

contador = 0
while contador < 10:
    print(contador)
    contador += 1
print()

print(' *** FOR *** ')

for numero in range(10):
    print(numero)
print()

print(' *** BREAK ***')

contador = 0
while True:
    print(contador)
    contador += 1
    if contador == 10:
        break
print()

print(' *** CONTINUE *** ')
contador = 0
while True:
    contador += 1
    if contador == 10:
        continue
    print(contador)
    if contador == 20:
        break
print()

print(' *** ELSE *** ')
contador = 0
while contador < 10:
    print(contador)
    contador +=1
else:
    print('Fim do laço de repetição')
dicionario = {
    'chave1': 'valor1',
    'chave2': 2,
    'chave3': 3.0,
}
print(dicionario['chave1'])
print(dicionario['chave2'])
print(dicionario['chave3'])

dicionario['chave4'] = 'valor4'
dicionario['chave5'] = 5
dicionario['chave6'] = 6.0
print(dicionario)

dicionario.pop('chave1')

print(dicionario)

print(dicionario.keys())

print(dicionario.values())

print(dicionario.items)

dicionario.clear()

print(dicionario)

dicionario = {
    'chave1': 'valor1',
    'chave2': 2,
    'chave3': 3.0,
}

dicionarioCopia = dicionario.copy()

print(dicionarioCopia)

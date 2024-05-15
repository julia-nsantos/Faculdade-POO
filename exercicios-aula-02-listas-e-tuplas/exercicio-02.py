lista = []

for i in range(10):
    n = int(input("Numero: "))
    lista.append(n)
print(lista)

conta_pares = 0
for item in lista:
    if item % 2 == 0:
        conta_pares += 1
print(f'Quantidade de pares: {conta_pares}')

soma_impares = 0
for item in lista:
    if item % 2 != 0:
        soma_impares += item
print(f'Somatório dos ímpares: {soma_impares}')

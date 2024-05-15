lista = []

for i in range(10):
    n = int(input("Numero: "))
    lista.append(n)
print("Essa e a lista de numeros:", lista)

lista_pares = []
lista_impares = []

for item in lista:
    if item % 2 == 0:
        lista_pares.append(item)
    else:
        lista_impares.append(item)

print("Esses são os numeros pares:", lista_pares)
print("Esses são os numeros impares", lista_impares)
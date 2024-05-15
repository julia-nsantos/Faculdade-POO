lista = []
for i in range(10):
    n = int(input('Numero: '))
    lista.append(n)

tupla = tuple(lista)    # copia os itens da lista para uma tupla
print(tupla)

numeros = []

for i in range(10):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(numero)

maior_numero = max(numeros)
menor_numero = min(numeros)

soma_numeros = sum(numeros)
media_numeros = soma_numeros / len(numeros)

print(f"O maior número da lista é: {maior_numero}")
print(f"O menor número da lista é: {menor_numero}")
print(f"A média dos números contidos na lista é: {media_numeros:.2f}")

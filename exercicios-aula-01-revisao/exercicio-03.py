def soma_dos_quadrados(num1, num2):
    quadrado1 = num1 ** 2
    quadrado2 = num2 ** 2
    soma = quadrado1 + quadrado2
    return soma


numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

resultado = soma_dos_quadrados(numero1, numero2)
print(f"A soma dos quadrados de {numero1} e {numero2} é {resultado}")

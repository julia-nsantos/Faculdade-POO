def media(num1, num2, num3):
    return (num1 + num2 + num3) / 3


numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))
numero3 = float(input("Digite o terceiro numero: "))

resultado = media(numero1, numero2, numero3)
print(f"A media dos numeros {numero1}, {numero2} e {numero3} é: {resultado}")

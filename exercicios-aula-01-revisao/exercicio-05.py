def calcular_salario(salario_atual):
    if salario_atual > 2000:
        aumento = salario_atual * 0.07  # 7% de aumento
    else:
        aumento = salario_atual * 0.15  # 15% de aumento
    
    salario_com_aumento = salario_atual + aumento
    return salario_com_aumento


salario_atual = float(input("Digite o salário atual do funcionário: "))


salario_com_aumento = calcular_salario(salario_atual)


print(f"O salário com o reajuste é: R$ {salario_com_aumento:.3f}")

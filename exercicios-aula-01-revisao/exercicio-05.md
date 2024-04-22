# Exercício 05: Cálculo do Salário com Reajuste

Neste exercício, você deve implementar a função `calcular_salario` que recebe o salário atual de um funcionário e retorna o salário com um reajuste de aumento. As regras para o reajuste são as seguintes:

- Caso o salário seja maior que R$ 2.000,00, o funcionário receberá 7% de aumento.
- Caso contrário, o funcionário receberá 15% de aumento.

## Descrição

Implemente a função `calcular_salario` de acordo com as seguintes especificações:

- A função `calcular_salario` deve receber um parâmetro: `salario_atual`.
- A função deve calcular o salário com o reajuste de aumento de acordo com as regras especificadas e retornar o resultado.

## Exemplo

Se `salario_atual` for igual a R$ 2.500,00, então a chamada da função `calcular_salario(2500)` deve retornar R$ 2.675,00, pois 7% de aumento em R$ 2.500,00 é R$ 175,00, resultando em um salário de R$ 2.675,00.


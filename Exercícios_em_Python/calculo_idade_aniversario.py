"""
CÁLCULO DE IDADE E DATA DO ANIVERSÁRIO
=======================================
Este programa calcula a idade de uma pessoa em anos, meses e dias,
recebendo a data de aniversário e a data atual.

Conceitos abordados:
- Operações sequenciais (sem loops ou condições)
- Entrada e conversão de dados
- Cálculos com datas
- Aritmética simples com valores
- Formatação de saída

Entrada: Data de aniversário (ano, mês, dia) e data atual
Saída: Idade em anos, meses e dias aproximados
"""

# Solicita a data de aniversário
ano_ani = int(input("Informe o ano do aniversário: "))
dia_ani = int(input("Informe o dia do aniversário: "))
mes_ani = int(input("Informe o mês do aniversário (formato numérico 01-12): "))

# Solicita a data atual
ano_atual = int(input("Informe o ano atual: "))
dia_atual = int(input("Informe o dia atual: "))
mes_atual = int(input("Informe o mês atual: "))

# Calcula a diferença de anos
ano = ano_atual - ano_ani

# Calcula o número de dias em um ano (aprox. 365 dias)
dia = 365 * 30

# Calcula quantos meses aproximados em um ano
mes = dia / 12

# Exibe os resultados
print(f"\nIdade calculada:")
print(f"  Anos: {ano}")
print(f"  Meses aproximados: {mes:.0f}")
print(f"  Dias aproximados: {dia}")

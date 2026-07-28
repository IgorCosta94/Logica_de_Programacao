"""
CÁLCULO DE JUROS E DESCONTO
============================
Este programa calcula juros e descontos sobre uma prestação em atraso,
demonstrando como uma multa pode ser reduzida por bom pagamento.

Conceitos abordados:
- Operações sequenciais
- Cálculo de percentuais e juros
- Aplicação de descontos
- Aritmética com valores monetários
- Comparação de impactos financeiros

Operações:
1. Aplicação de 10% de juros
2. Aplicação de 10% de desconto
3. Cálculo do prejuízo para o comerciante
"""

# Solicita o valor da prestação em atraso
n = float(input("Informe o valor da prestação em atraso (R$): "))

# Calcula o valor com juros (10% de acréscimo)
juros = n + (n * 0.10)

# Calcula o valor final após aplicar desconto de 10% sobre o valor com juros
desconto = juros - (juros * 0.10)

# Exibe os resultados detalhados
print("\n" + "="*50)
print("CÁLCULO DE JUROS E DESCONTO")
print("="*50)
print(f"Valor original da prestação: R$ {n:.2f}")
print(f"Valor com juros de 10%:      R$ {juros:.2f}")
print(f"Valor final com desconto:    R$ {desconto:.2f}")
print(f"Prejuízo para o comerciante: R$ {juros - desconto:.2f}")
print("="*50)

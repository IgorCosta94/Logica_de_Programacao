"""
CÁLCULO DE IMPOSTO DE RENDA
============================
Este programa calcula o imposto de renda devido com base no número de salários
mínimos recebidos, com deduções por dependentes e alíquotas progressivas.

Conceitos abordados:
- Estruturas condicionais com múltiplas ramificações (if/elif)
- Cálculos com alíquotas e percentuais
- Loops de coleta de dados
- Deduções e abatimentos fiscais

Entrada: Número de salários mínimos, quantidade de dependentes, CPF
Saída: Status de isento ou valor do imposto a pagar
"""

print("\nPara encerrar digite 0 - Zero para salário\n")

# Coleta dados do primeiro contribuinte
salario = int(input("Informe quantos salários mínimos você recebe: "))
n_dependentes = int(input("Informe quantos dependentes possui: "))
n_CPF = int(input("Informe o número do seu CPF: "))

# Loop que processa múltiplos contribuintes
while salario != 0:
    # Categoria 1: Até 2 salários mínimos - ISENTO
    if salario <= 2:
        print("Você está isento. NÃO DEVE PAGAR!!!!\n")
    
    # Categoria 2: Exatamente 3 salários mínimos - Alíquota de 5%
    elif salario == 3:
        if n_dependentes > 0:
            # Converte salários em valor monetário (1 SM = R$ 1.412,00)
            salario_valor = 1412 * salario
            # Calcula dedução por dependentes (5% por dependente)
            deducao_dependentes = (0.05 * n_dependentes) * salario_valor
            # Calcula imposto com desconto de dependentes e alíquota de 5%
            imposto = salario_valor - (deducao_dependentes - (0.05 * salario_valor))
            print(f"Você deve pagar um valor de R$ {imposto:.2f}\n")
    
    # Categoria 3: Exatamente 4 salários mínimos - Alíquota de 7.5%
    elif salario == 4:
        if n_dependentes > 0:
            salario_valor = 1412 * salario
            deducao_dependentes = (0.05 * n_dependentes) * salario_valor
            imposto = salario_valor - (deducao_dependentes - (0.075 * salario_valor))
            print(f"Você deve pagar um valor de R$ {imposto:.2f}\n")
    
    # Categoria 4: Exatamente 5 salários mínimos - Alíquota de 10%
    elif salario == 5:
        if n_dependentes > 0:
            salario_valor = 1412 * salario
            deducao_dependentes = (0.05 * n_dependentes) * salario_valor
            imposto = salario_valor - (deducao_dependentes - (0.10 * salario_valor))
            print(f"Você deve pagar um valor de R$ {imposto:.2f}\n")
    
    # Categoria 5: Exatamente 6 salários mínimos - Alíquota de 12%
    elif salario == 6:
        if n_dependentes > 0:
            salario_valor = 1412 * salario
            deducao_dependentes = (0.05 * n_dependentes) * salario_valor
            imposto = salario_valor - (deducao_dependentes - (0.12 * salario_valor))
            print(f"Você deve pagar um valor de R$ {imposto:.2f}\n")
    
    # Coleta dados do próximo contribuinte
    print("Para encerrar digite 0 - Zero para salário\n")
    salario = int(input("Informe quantos salários mínimos você recebe: "))
    
    if salario != 0:
        n_dependentes = int(input("Informe quantos dependentes possui: "))
        n_CPF = int(input("Informe o número do seu CPF: "))

print("Fim do processamento.")

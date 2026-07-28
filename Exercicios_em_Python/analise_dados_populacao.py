"""
ANÁLISE DE DADOS DA POPULAÇÃO
==============================
Este programa coleta e analisa dados de habitantes, calculando estatísticas como:
- A maior idade entre os habitantes
- Porcentagem de homens entre 18 e 35 anos
- Porcentagem de mulheres com olhos verdes e cabelos loiros

Conceitos abordados:
- Loops com condições múltiplas
- Acumuladores (contadores e máximos)
- Estruturas condicionais aninhadas
- Cálculo de porcentagens

Entrada: Dados de sexo, características físicas e idade de múltiplos habitantes
Saída: Estatísticas e porcentagens calculadas
"""

# Coleta de dados iniciais do primeiro habitante
sexo = input("Informe o sexo. 'M'- masculino ou 'F' - feminino: ")
olhos = input("Informe a cor dos olhos. 'A'- Azuis, 'V' - verdes, ou 'C' - castanhos: ")
cabelos = input("Informe a cor do cabelo. 'L' - loiros, 'C' - castanhos, 'P' - pretos: ")
idade = int(input("Informe a idade: "))
print("\nPara terminar digite -1 para idade\n")

# Inicialização dos acumuladores
acum_ih = 0           # Armazena a maior idade
acum_H = 0            # Conta homens entre 18 e 35 anos
acum_TH = 0           # Conta total de homens
acum_T = 0            # Conta total de pessoas
acum_M = 0            # Conta mulheres com olhos verdes e cabelos loiros

# Loop principal que processa dados até que idade seja -1
while idade != -1:
    # Verifica e atualiza a maior idade
    if idade > acum_ih:
        acum_ih = idade
        
    # Processa dados de homens
    if sexo == 'M':
        acum_TH += 1  # Incrementa total de homens
        if idade >= 18 or idade <= 35:  # Verifica faixa etária
            acum_H += 1  # Incrementa contador de homens na faixa
    
    # Processa dados de mulheres
    elif sexo == 'F':
        if olhos == 'V' and cabelos == 'L':  # Verifica características específicas
            acum_M += 1  # Incrementa contador de mulheres com esses atributos
            
    # Incrementa o total geral de pessoas
    acum_T += 1
    
    # Coleta dados do próximo habitante
    sexo = input("Informe o sexo. 'M'- masculino ou 'F' - feminino: ")
    olhos = input("Informe a cor dos olhos. 'A'- Azuis, 'V' - verdes, ou 'C' - castanhos: ")
    cabelos = input("Informe a cor do cabelo. 'L' - loiros, 'C' - castanhos, 'P' - pretos: ")
    idade = int(input("Informe a idade: "))

# Exibição dos resultados
print(f"\nA maior idade entre os habitantes é igual a: {acum_ih}")
print(f"A porcentagem entre os homens com idade entre 18 e 35 anos é: {(acum_H * 100) / acum_TH:.2f}%")
print(f"A porcentagem do total de indivíduos do sexo feminino entre 18 e 35,")
print(f"e com olhos verdes e cabelos loiros: {(acum_M * 100) / acum_T:.2f}%")

"""
BUSCA DA MAIOR EMPRESA POR PORTE
=================================
Este programa coleta dados de empresas e identifica qual empresa tem o maior
número de funcionários em cada categoria de porte (Grande, Média, Pequena, Micro).

Conceitos abordados:
- Loops com múltiplas condições
- Estruturas condicionais aninhadas
- Variáveis para armazenar máximos e seus códigos
- Validação de entrada com mensagens de erro

Entrada: Código da empresa, número de funcionários, porte da empresa
Saída: Para cada porte, exibe o código da empresa com mais funcionários
"""

print("Para encerrar digite 0 no código da empresa")

# Coleta dados da primeira empresa
codigo = int(input("Informe o código da empresa: "))
n_funcionarios = int(input("Informe o número de funcionários: "))
porte = input("Informe o porte da empresa (Grande, Media, Pequena ou Micro): ")

# Inicialização das variáveis para armazenar o maior número de funcionários
# e o código da empresa correspondente para cada porte
nf_g = 0    # Número de funcionários da maior empresa Grande
nf_m = 0    # Número de funcionários da maior empresa Média
nf_p = 0    # Número de funcionários da maior empresa Pequena
nf_mc = 0   # Número de funcionários da maior empresa Micro

cg = 0      # Código da maior empresa Grande
cm = 0      # Código da maior empresa Média
cp = 0      # Código da maior empresa Pequena
cmc = 0     # Código da maior empresa Micro

# Loop principal que processa empresas até que código seja 0
while codigo != 0:
    # Classifica a empresa por porte e atualiza o máximo se necessário
    if porte.lower() == "grande":
        if n_funcionarios > nf_g:  # Se esta empresa é maior que a anterior
            nf_g = n_funcionarios
            cg = codigo
    
    elif porte.lower() == "media":
        if n_funcionarios > nf_m:
            nf_m = n_funcionarios
            cm = codigo
    
    elif porte.lower() == "pequena":
        if n_funcionarios > nf_p:
            nf_p = n_funcionarios
            cp = codigo
    
    elif porte.lower() == "micro":
        if n_funcionarios > nf_mc:
            nf_mc = n_funcionarios
            cmc = codigo
    
    else:
        # Valida a entrada do porte
        print("Informe o porte da empresa correto (Grande, Media, Pequena ou Micro)\n")

    # Coleta dados da próxima empresa
    print("\nPara encerrar digite 0 no código da empresa")
    codigo = int(input("Informe o código da empresa: "))
    
    if codigo != 0:  # Evita pedir dados desnecessários após o fim
        n_funcionarios = int(input("Informe o número de funcionários: "))
        porte = input("Informe o porte da empresa (Grande, Media, Pequena ou Micro): ")

# Exibe os resultados
print("\n" + "="*50)
print("EMPRESAS COM MAIOR NÚMERO DE FUNCIONÁRIOS POR PORTE")
print("="*50)
if cg != 0:
    print(f"Grande:  Código {cg} com {nf_g} funcionários")
if cm != 0:
    print(f"Média:   Código {cm} com {nf_m} funcionários")
if cp != 0:
    print(f"Pequena: Código {cp} com {nf_p} funcionários")
if cmc != 0:
    print(f"Micro:   Código {cmc} com {nf_mc} funcionários")

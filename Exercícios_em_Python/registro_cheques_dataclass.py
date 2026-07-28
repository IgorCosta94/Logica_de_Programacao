"""
REGISTRO DE CHEQUES COM DATACLASS
==================================
Este programa gerencia um registro de cheques usando dataclasses,
demonstrando como estruturar dados com classes de forma elegante
e eficiente em Python.

Conceitos abordados:
- Dataclasses para criar estruturas de dados
- Registros (structs) com validação de campo
- Armazenamento de dados estruturados
- Funções para manipulação de registros
- Cálculo de dígito verificador
- Integração com listas de registros

Estrutura do Cheque:
- Número do cheque
- Número da agência
- Número da conta
- Dígito verificador
- Nome do titular
- Valor do cheque
"""

from dataclasses import dataclass

def reg():
    """
    Função principal que gerencia o registro de cheques.
    Coleta dados de até 100 cheques e os armazena em uma dataclass.
    """
    
    # Define a estrutura de dados para um cheque usando dataclass
    @dataclass
    class cheque:
        numero_cheque: int      # Identificador único do cheque
        agencia: int            # Código da agência bancária
        numero_conta: int       # Número da conta corrente
        DV: int                 # Dígito verificador da conta
        nome: str               # Nome do titular
        valor: float            # Valor do cheque em reais
    
    # Inicializa um array para armazenar até 100 cheques
    cont = 0
    x = [0] * 100
    
    # Inicializa todos os elementos com um cheque vazio
    for w in range(0, len(x), 1):
        x[w] = cheque(0, 0, 0, 0, '', 0.0)
    
    print("//Para encerrar digite 0 - zero para o número da conta//")
    print()
    
    # Solicita o primeiro cheque
    numero_cheque = int(input("Informe o número do cheque: "))
    
    # Loop de entrada de dados
    while numero_cheque != 0 and cont < 100:
        agencia = int(input("Informe o número da agência: "))
        numero_conta = int(input("Informe o número da conta: "))
        
        # Calcula o dígito verificador da conta
        DV = verificador(numero_conta)
        
        nome = input("Informe seu nome: ")
        valor = float(input("Informe o valor do cheque: "))
        
        # Armazena o cheque no array
        x[cont] = cheque(numero_cheque, agencia, numero_conta, DV, nome, valor)
        print()
        
        print("//Para encerrar digite 0 - zero para o número da conta//")
        print()
        cont += 1
        numero_cheque = int(input("Informe o número do cheque: "))
    
    # Processa os cheques registrados
    relatório(x)


def verificador(x):
    """
    Calcula o dígito verificador da conta bancária.
 
    """
    s = x
    calculo = 0
    global cont
    cont = 0
    w = 0
    
    # Conta quantos dígitos tem o número
    while x != 0:
        calculo = x % 10
        x = x // 10
        cont += 1
    
    return inverso(s, cont)


def inverso(q, m):
    """
    Inverte o cálculo para obter o dígito verificador.
 
    """
    v = q
    w = pow(10, m - 1)
    soma = 0
    
    while w != 0:
        calculo = q % 10
        cont = w * calculo
        soma += cont
        w = w // 10
        q = q // 10
    
    soma = soma + v
    return inverso2(soma)


def inverso2(r):
    """
    Etapa final do cálculo do dígito verificador.
    """
    x = r
    soma = 0
    cont = 0
    
    while x != 0:
        soma += x % 10
        x = x // 10
        cont += 1
    
    return soma % 11


def relatório(x):
    """
    Exibe o relatório dos cheques registrados.
    """
    print("\n" + "="*80)
    print("RELATÓRIO DE CHEQUES REGISTRADOS")
    print("="*80)
    
    i = 1
    while x[i].numero_cheque != 0:
        print(f"\nCheque {i}:")
        print(f"  Número: {x[i].numero_cheque}")
        print(f"  Agência: {x[i].agencia}")
        print(f"  Conta: {x[i].numero_conta}")
        print(f"  DV: {x[i].DV}")
        print(f"  Titular: {x[i].nome}")
        print(f"  Valor: R$ {x[i].valor:.2f}")
        i += 1
        
        if i >= 100:  # Previne estouro de array
            break


# Executa o programa
if __name__ == "__main__":
    reg()

"""
GERENCIAMENTO DE NOMES - SISTEMA CRUD
======================================
Este programa implementa um sistema completo de gerenciamento de nomes
com operações CRUD (Create, Read, Update, Delete) para duas listas
(homens e mulheres).

Conceitos abordados:
- Listas em Python
- Funções para modularização
- Menu de opções
- Operações CRUD completas
- Busca e modificação de elementos
- Validação com sinalizadores (flags)

Operações:
1. Exclusão: Remove um nome de uma das listas
2. Localização: Encontra a posição de um nome
3. Alteração: Modifica um nome existente
"""

# Listas globais para armazenar nomes
homens = []
mulheres = []
cont = 0

# ====================
# FUNÇÕES DE INSERÇÃO
# ====================

def lista_H(hom):
    """Adiciona um nome à lista de homens"""
    hom.append(input("Digite um nome para homens: "))

def lista_M(mum):
    """Adiciona um nome à lista de mulheres"""
    mum.append(input("Digite um nome para mulheres: "))

# ====================
# FUNÇÃO DE MENU
# ====================

def opcoes(hom, mum):
    """
    Exibe o menu de opções e direciona para a operação escolhida
    1 - Exclusão
    2 - Localização
    3 - Alteração
    """
    opcs = int(input("Digite 1 para exclusão, 2 para localização e 3 para alteração\n"))
    
    if opcs == 1:
        exclusao(hom, mum)
    elif opcs == 2:
        localizacao(hom, mum)
    elif opcs == 3:
        alteracao(hom, mum)

# ====================
# FUNÇÃO DE EXCLUSÃO
# ====================

def exclusao(hom, mum):
    """Remove um nome da lista selecionada"""
    sinalizador = 0
    h_ou_m = int(input("Digite 1 para homem ou 2 para mulher: "))
    nome = input("Forneça o nome que deseja excluir: ")
    
    # Busca e remove de homens
    if h_ou_m == 1:
        for w in range(0, len(hom) - 1, 1):
            if nome == hom[w]:
                hom.remove(hom[w])
                sinalizador = 1
        
        if sinalizador == 1:
            print("O Nome foi excluído com sucesso\n")
        elif sinalizador == 0:
            print("Nome não encontrado!!! Não foi possível excluir\n")
    
    # Busca e remove de mulheres
    elif h_ou_m == 2:
        for w in range(0, len(mum) - 1, 1):
            if nome == mum[w]:
                mum.remove(mum[w])
                sinalizador = 1
        
        if sinalizador == 1:
            print("O Nome foi excluído com sucesso\n")
        elif sinalizador == 0:
            print("Nome não encontrado!!! Não foi possível excluir\n")

# ====================
# FUNÇÃO DE LOCALIZAÇÃO
# ====================

def localizacao(hom, mum):
    """Encontra e exibe a posição de um nome na lista"""
    sinalizador = 0
    h_ou_m = int(input("Digite 1 para homem ou 2 para mulher: "))
    nome = input("Forneça o nome que deseja localizar: ")
    
    # Busca em homens
    if h_ou_m == 1:
        for w in range(0, len(hom) - 1, 1):
            if nome == hom[w]:
                print(f"O nome: {nome} está na posição {hom.index(nome)}\n")
                sinalizador = 1
        
        if sinalizador == 1:
            print("O Nome foi localizado\n")
        elif sinalizador == 0:
            print("O Nome não foi localizado\n")
    
    # Busca em mulheres
    elif h_ou_m == 2:
        for w in range(0, len(mum) - 1, 1):
            if nome == mum[w]:
                print(f"O nome: {nome} está na posição {mum.index(nome)}\n")
                sinalizador = 1
        
        if sinalizador == 1:
            print("O Nome foi localizado\n")
        elif sinalizador == 0:
            print("O Nome não foi localizado\n")

# ====================
# FUNÇÃO DE ALTERAÇÃO
# ====================

def alteracao(hom, mum):
    """Modifica um nome existente em uma das listas"""
    h_ou_m = int(input("Digite 1 para homem ou 2 para mulher: "))
    nome = input("Forneça o nome que deseja alterar: ")
    nome2 = input("Forneça o novo nome que deseja substituir: ")
    
    # Altera em homens
    if h_ou_m == 1:
        for w in range(0, len(hom) - 1, 1):
            if nome == hom[w]:
                hom.remove(hom[w])
                hom.insert(w, nome2)
    
    # Altera em mulheres
    elif h_ou_m == 2:
        for w in range(0, len(mum) - 1, 1):
            if nome == mum[w]:
                mum.remove(mum[w])
                mum.insert(w, nome2)

print("Sistema de Gerenciamento de Nomes")
print("Escolha uma operação: 1-Exclusão, 2-Localização, 3-Alteração")

# Exemplo de uso
opcoes(homens, mulheres)

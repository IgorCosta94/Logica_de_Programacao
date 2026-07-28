"""
ESTRUTURA DE DADOS: LISTA ENCADEADA
=====================================
Este programa demonstra uma LISTA ENCADEADA, onde cada nó contém dados
e uma referência para o próximo nó. A sequência é controlada pela ordem
de encadeamento, não pela posição na lista.

Conceitos abordados:
- Estrutura de dados não-linear em armazenamento
- Nós com dados e referência para próximo (pointer)
- Navegação através de encadeamento
- Ordem flexível através do campo "prox"

Caso de uso: Ordem customizável de tarefas, listas ligadas, grafos
"""

from dataclasses import dataclass

# Define a estrutura do item com dados e referência para o próximo
@dataclass
class regitem():
    item: str      # Descrição da tarefa
    prox: int      # Índice do próximo item na lista (-1 = fim)

# Cria a lista de tarefas com suas referências de encadeamento
lista = [
    regitem("Efetuar um saque no caixa", 5),
    regitem("Comprar livros na livraria", 3),
    regitem("Deixar o carro no estacionamento", 7),
    regitem("Pegar as roupas na lavanderia", -1),  # -1 indica fim da lista
    regitem("Buscar encomenda no correio", 0),
    regitem("Comprar presente", 1),
    regitem("Autenticar documentos no cartório", 4),
    regitem("Comprar calçados no shopping", 6),
]

# Define o índice de início da sequência
comeco = 2  # Começa na posição 2 ("Deixar o carro...")

# Recupera o primeiro item
tarefa = lista[comeco]
i = 1

# Exibe a primeira tarefa
print(f"Tarefa {i}: {tarefa.item}")

# Navegação através da lista encadeada seguindo os ponteiros
while tarefa.prox != -1:
    i += 1
    tarefa = lista[tarefa.prox]  # Vai para o próximo item
    print(f"Tarefa {i}: {tarefa.item}")

print(f"\nTotal de tarefas na sequência: {i}")

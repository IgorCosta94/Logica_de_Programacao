"""
ESTRUTURA DE DADOS: PILHA (LIFO - Last In, First Out)
=======================================================
Este programa demonstra o funcionamento de uma PILHA (stack), uma estrutura
de dados onde o último elemento inserido é o primeiro a sair.

Conceitos abordados:
- Estrutura de dados linear (LIFO)
- Operações: append (push) e pop (pop)
- Visualização de tamanho e conteúdo
- Ordem de remoção inversa à inserção

Caso de uso: Histórico de ações, desfazer/refazer, pilha de chamadas
"""

# Inicializa a pilha com dois elementos
pilhalocal = ["Ciclano", "João"]
print(f"Estado 1 - Tamanho: {len(pilhalocal)}, Pilha: {pilhalocal}")

# Adiciona dois novos elementos à pilha
pilhalocal.extend(["Beltrano", "José"])
print(f"Estado 2 - Tamanho: {len(pilhalocal)}, Pilha: {pilhalocal}")

# Adiciona um novo elemento à pilha
pilhalocal.append("Fulano")
print(f"Estado 3 - Tamanho: {len(pilhalocal)}, Pilha: {pilhalocal}")

# Remove elementos da pilha (LIFO - último adicionado sai primeiro)
print("\nRemovendo elementos da pilha (LIFO):")
while pilhalocal:
    # pop() remove e retorna o último elemento
    print("Atendendo: ", pilhalocal.pop())

print("\nPilha vazia!")

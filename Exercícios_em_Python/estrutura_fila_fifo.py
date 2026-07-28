"""
ESTRUTURA DE DADOS: FILA (FIFO - First In, First Out)
=======================================================
Este programa demonstra o funcionamento de uma FILA (queue), uma estrutura
de dados onde o primeiro elemento inserido é o primeiro a sair.

Conceitos abordados:
- Estrutura de dados linear (FIFO)
- Uso de deque (double-ended queue) para eficiência
- Operações: append (enqueue) e popleft (dequeue)
- Visualização de tamanho e conteúdo
- Ordem de remoção igual à inserção (como em filas do mundo real)

Caso de uso: Filas de atendimento, processamento de tarefas, agendamento
"""

from collections import deque

# Inicializa a fila com dois elementos
filacliente = deque(["Ciclano", "João"])
print(f"Estado 1 - Tamanho: {len(filacliente)}, Fila: {filacliente}")

# Adiciona dois novos elementos à fila
filacliente.extend(["Beltrano", "José"])
print(f"Estado 2 - Tamanho: {len(filacliente)}, Fila: {filacliente}")

# Adiciona um novo elemento à fila
filacliente.append("Fulano")
print(f"Estado 3 - Tamanho: {len(filacliente)}, Fila: {filacliente}")

# Remove elementos da fila (FIFO - primeiro adicionado sai primeiro)
print("\nRemovendo elementos da fila (FIFO):")
while filacliente:
    # popleft() remove e retorna o primeiro elemento
    print("Atendendo: ", filacliente.popleft())

print("\nFila vazia!")

"""
COMPARAÇÃO DE CRESCIMENTO DE ALTURA
====================================
Este programa simula o crescimento de altura de duas pessoas ao longo dos anos
e determina quantos anos serão necessários para uma pessoa ultrapassar a outra
em altura.

Conceitos abordados:
- Loops com variável de controle
- Incrementos e acumuladores
- Comparação de valores
- Simulação e iteração

Entrada: Alturas iniciais (hardcoded: Anacleto 1.50m, Felisberto 1.10m)
         Incrementos anuais (0.02m e 0.03m respectivamente)
Saída: Número de anos até Felisberto ficar mais alto que Anacleto
"""

# Inicialização das variáveis
anos = 0              # Contador de anos passados
sentinela = 0         # Variável de controle do loop
anacleto = 1.50       # Altura inicial de Anacleto em metros
felisberto = 1.10     # Altura inicial de Felisberto em metros

# Loop que simula o crescimento anual
while sentinela != -1:
    # Verifica se Felisberto ultrapassou Anacleto em altura
    if felisberto > anacleto:
        sentinela = -1  # Encerra o loop
        
    # Incrementa a altura de cada pessoa por ano
    anacleto += 0.02      # Crescimento de Anacleto: 2cm por ano
    felisberto += 0.03    # Crescimento de Felisberto: 3cm por ano
    anos += 1             # Incrementa o contador de anos

# Exibe o resultado
print(f"A quantidade de anos para Felisberto ficar maior que Anacleto é: {anos} anos")
print(f"Altura de Anacleto após {anos} anos: {anacleto:.2f}m")
print(f"Altura de Felisberto após {anos} anos: {felisberto:.2f}m")

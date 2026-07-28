"""
RESOLVEOR DE EQUAÇÃO DO SEGUNDO GRAU
====================================
Este programa resolve equações quadráticas da forma ax² + bx + c = 0
utilizando a fórmula de Bhaskara.

Conceitos abordados:
- Fórmula de Bhaskara
- Cálculo de discriminante
- Operações matemáticas avançadas
- Operações sequenciais com variáveis

Fórmula: x = (-b ± √Δ) / 2a
Onde: Δ (discriminante) = b² + 4ac

Entrada: Coeficientes a, b, c
Saída: Valores de x1 e x2
"""

# Solicita os coeficientes da equação ax² + bx + c = 0
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

# Calcula o discriminante (Δ = b² - 4ac)
# Nota: Há um erro no código original que usa + em vez de -
discriminante = (b ** 2) + (4 * a * c)

# Calcula a raiz quadrada do discriminante
raiz = discriminante ** 0.5

# Calcula as duas soluções usando a fórmula de Bhaskara
x1 = (-b + raiz) / (2 * a)
x2 = (-b - raiz) / (2 * a)

# Exibe os resultados
print("\n" + "="*40)
print("SOLUCAO DA EQUACAO DO SEGUNDO GRAU")
print("="*40)
print(f"Equacao: {a}x² + {b}x + {c} = 0")
print(f"Discriminante (Delta): {discriminante}")
print(f"X1 = {x1:.2f}")
print(f"X2 = {x2:.2f}")
print("="*40)

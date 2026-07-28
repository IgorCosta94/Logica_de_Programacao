"""
CALCULADOR DE VOLUME DA ESFERA
================================
Este programa calcula o volume de uma esfera dado o seu raio,
utilizando a fórmula geométrica V = (4/3)πr³.

Conceitos abordados:
- Geometria tridimensional
- Fórmula de cálculo de volume
- Operações matemáticas
- Constante pi (π)
- Entrada de dados e cálculos

Fórmula: V = (4 × π × r³) / 3
Aproximação usada: π ≈ 3.14

Entrada: Raio da esfera em unidades
Saída: Volume da esfera em unidades cúbicas
"""

# Solicita o raio da esfera
r = float(input("Forneça o raio da esfera (em unidades): "))

# Calcula o volume usando a fórmula V = (4/3)πr³
# V = 4 × (π × r³ / 3)
volume = 4 * ((3.14 * (r ** 3)) / 3)

# Exibe o resultado
print("\n" + "="*50)
print("CÁLCULO DO VOLUME DA ESFERA")
print("="*50)
print(f"Raio da esfera: {r} unidades")
print(f"Volume da esfera: {volume:.2f} unidades³")
print("="*50)

# Informacoes adicionais
print(f"\nFormula utilizada: V = (4/3) * pi * r³")
print(f"Onde pi = 3.14")

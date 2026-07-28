"""
CALCULADOR DE MÉDIA DE NOTAS
=============================
Este programa calcula a média aritmética de 4 notas de um aluno.
Demonstra o uso de loops para coleta de dados e acumuladores.

Conceitos abordados:
- Loops para coleta repetida de dados
- Acumuladores (soma)
- Cálculo de média aritmética
- Conversão de tipos (float para armazenar valores decimais)
- Contadores para controlar iterações

Entrada: 4 notas de um aluno (números decimais)
Saída: Média aritmética das 4 notas
"""

# Inicializa as variáveis
contador = 1  # Controla quantas notas foram digitadas
soma = 0      # Acumulador para somar todas as notas

# Loop para coletar as 4 notas
while (contador <= 4):
    # Solicita a nota do aluno
    n = float(input("Digite a nota do aluno (digite uma por vez): "))
    
    # Soma a nota atual ao acumulador
    soma += n
    
    # Incrementa o contador
    contador += 1

# Calcula e exibe a média
media = soma / 4

print("\n" + "="*40)
print("RESULTADO")
print("="*40)
print(f"Soma das notas: {soma:.2f}")
print(f"A média das notas do aluno é: {media:.2f}")
print("="*40)

# Exibe situacao do aluno (exemplo basico)
if media >= 7:
    print("Status: APROVADO [OK]")
elif media >= 5:
    print("Status: RECUPERACAO")
else:
    print("Status: REPROVADO [FALHA]")

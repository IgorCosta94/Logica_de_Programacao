"""
CONVERSOR DE NÚMEROS EM EXTENSO
================================
Este programa converte números (de 1 a 999.999) em sua representação
textual por extenso em português (ex: 123 → "Cento e vinte e três").

Conceitos abordados:
- Funções personalizadas
- Estruturas condicionais múltiplas
- Manipulação de strings e listas
- Formatação de saída
- Validação de intervalos

Entrada: Um número inteiro entre 1 e 999.999
Saída: O número representado em extenso
"""

def extenso(numero):
    """
    Converte um número inteiro em sua representação em extenso.
    
    Args:
        numero (int): Um valor entre 1 e 999.999
    
    Returns:
        None (imprime o resultado)
    """
    
    # Valida se o número está no intervalo aceito
    if numero >= 1 and numero <= 999999:
        
        # Lista com todos os números em extenso de 0 a 28
        x = ['', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
             'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 
             'Dezenove', 'Vinte', 'Trinta', 'Quarenta', 'Cinquenta', 'Sessenta', 'Setenta', 
             'Oitenta', 'Noventa', 'Cem']
        
        # Números de 1 a 20
        if numero <= 20:
            print(f"{x[numero]}")
        
        # Números de 21 a 29
        elif numero > 20 and numero < 30:
            print(f"{x[20]} e {x[numero % 10]}")
        
        # Números 30 a 39
        if numero == 30:
            print(f"{x[21]}")
        elif numero > 30 and numero < 40:
            print(f"{x[21]} e {x[numero % 10]}")
        
        # Números 40 a 49
        if numero == 40:
            print(f"{x[22]}")
        elif numero > 40 and numero < 50:
            print(f"{x[22]} e {x[numero % 10]}")
        
        # Números 50 a 59
        if numero == 50:
            print(f"{x[23]}")
        elif numero > 50 and numero < 60:
            print(f"{x[23]} e {x[numero % 10]}")
        
        # Números 60 a 69
        if numero == 60:
            print(f"{x[24]}")
        elif numero > 60 and numero < 70:
            print(f"{x[24]} e {x[numero % 10]}")
        
        # Números 70 a 79
        if numero == 70:
            print(f"{x[25]}")
        elif numero > 70 and numero < 80:
            print(f"{x[25]} e {x[numero % 10]}")
        
        # Números 80 a 89
        if numero == 80:
            print(f"{x[26]}")
        elif numero > 80 and numero < 90:
            print(f"{x[26]} e {x[numero % 10]}")
        
        # Números 90 a 99
        if numero == 90:
            print(f"{x[27]}")
        elif numero > 90 and numero < 100:
            print(f"{x[27]} e {x[numero % 10]}")
        
        # Números 100 a 119
        if numero == 100:
            print(f"{x[28]}")
        elif numero > 100 and numero < 120:
            print(f"{x[28]} e {x[numero % 100]}")
    
    else:
        # Mensagem de erro para números fora do intervalo
        print("ERRO!!! NÚMERO FORA DO INTERVALO... (use valores entre 1 e 999.999)")

# Solicita entrada do usuário
n = int(input("Informe um número no intervalo de 1 a 999.999: "))

# Chama a função para exibir o resultado
extenso(n)

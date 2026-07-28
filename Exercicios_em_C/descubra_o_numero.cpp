#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <ctype.h>

int validar_entrada_inteira(const char *entrada);
void iniciar_jogo(void);
void exibir_feedback_final(int tentativas);

/*
 * Jogo de adivinhar o numero: o programa escolhe um valor aleatorio
 * entre 1 e 1000 e o usuario tenta descobrir com base nos palpites.
 */
int main(void)
{
    char continuar;

    /* Inicializa o gerador de numeros aleatorios com o tempo atual. */
    srand(time(NULL));

    do
    {
        iniciar_jogo();
        printf("Gostaria de jogar novamente (s/n)? ");
        scanf(" %c", &continuar);
    } while (tolower(continuar) == 's');

    printf("\nObrigado por jogar! Ate logo.\n");
    return 0;
}

void iniciar_jogo(void)
{
    int numero_secreto = 1 + rand() % 1000;
    int palpite_usuario = 0;
    int contador_tentativas = 0;
    char buffer_entrada[50];

    printf("\n--- JOGO DA ADIVINHACAO ---\n");
    printf("Eu tenho um numero entre 1 e 1000.\n");
    printf("Voce consegue descobrir qual e?\n\n");

    while (palpite_usuario != numero_secreto)
    {
        printf("Digite sua tentativa: ");
        scanf("%s", buffer_entrada);

        if (!validar_entrada_inteira(buffer_entrada))
        {
            printf("Entrada invalida! Por favor, digite apenas numeros inteiros.\n\n");
            continue;
        }

        palpite_usuario = atoi(buffer_entrada);
        contador_tentativas++;

        if (palpite_usuario < numero_secreto)
        {
            printf("Muito baixo. Tente novamente.\n\n");
        }
        else if (palpite_usuario > numero_secreto)
        {
            printf("Muito alto. Tente novamente.\n\n");
        }
    }

    printf("Excelente! Voce descobriu o numero!\n");
    exibir_feedback_final(contador_tentativas);
}

void exibir_feedback_final(int tentativas)
{
    printf("Total de tentativas: %d\n", tentativas);

    /* Feedback baseado na quantidade de palpites. */
    if (tentativas < 10)
    {
        printf("Aha! Voce conhece o segredo ou teve muita sorte!\n\n");
    }
    else if (tentativas == 10)
    {
        printf("Ah! Voce conhece o segredo!\n\n");
    }
    else
    {
        printf("Voce deveria se sair melhor. Tente usar a busca binaria!\n\n");
    }
}

int validar_entrada_inteira(const char *entrada)
{
    if (entrada == NULL || entrada[0] == '\0')
        return 0;

    int i = (entrada[0] == '-') ? 1 : 0;

    /* Garante que todos os caracteres lidos sao digitos numericos. */
    for (; entrada[i] != '\0'; i++)
    {
        if (!isdigit(entrada[i]))
            return 0;
    }
    return 1;
}

#include <stdio.h>

#define TAMANHO 10

/*
 * Bubble Sort: ordena um array comparando elementos adjacentes
 * e movendo os maiores elementos para o fim em cada passagem.
 */
int main(void)
{
    int lista_numeros[TAMANHO] = {2, 6, 4, 8, 10, 12, 89, 68, 45, 37};
    int iteracao, indice, auxiliar_troca;

    /* Exibe o vetor antes da ordenação. */
    printf("Dados na ordem original:\n");
    for (indice = 0; indice < TAMANHO; indice++)
    {
        printf("%4d", lista_numeros[indice]);
    }

    /* Loop externo percorre as passagens do algoritmo. */
    for (iteracao = 0; iteracao < TAMANHO - 1; iteracao++)
    {
        /* Loop interno compara elementos adjacentes em cada passagem. */
        for (indice = 0; indice < TAMANHO - 1 - iteracao; indice++)
        {
            /* Troca se o elemento atual for maior que o próximo. */
            if (lista_numeros[indice] > lista_numeros[indice + 1])
            {
                auxiliar_troca = lista_numeros[indice];
                lista_numeros[indice] = lista_numeros[indice + 1];
                lista_numeros[indice + 1] = auxiliar_troca;
            }
        }
    }

    /* Exibe o vetor já ordenado em ordem crescente. */
    printf("\n\nDados em ordem crescente:\n");
    for (indice = 0; indice < TAMANHO; indice++)
    {
        printf("%4d", lista_numeros[indice]);
    }

    printf("\n");

    return 0;
}

/* Programa para calcular o fatorial de um numero inteiro nao negativo.

   ATENÇÃO!!! Para valores muitos grandes, o resultado pode ultrapassar o limite do tipo long int,
   retornando um valor incorreto.
*/

#include <stdio.h>

int main(void)
{
    int numero_entrada;
    int numero_original;
    long int fatorial_acumulado = 1;

    /* Garante que o usuario insira um número inteiro >= 0. */
    do
    {
        printf("Informe um valor inteiro nao negativo (n!): ");
        scanf("%d", &numero_entrada);

        if (numero_entrada < 0)
        {
            printf("Erro: O numero deve ser maior ou igual a zero.\n");
        }
    } while (numero_entrada < 0);

    numero_original = numero_entrada;

    /* Calcula o fatorial por multiplicacao decrescente. */
    while (numero_entrada > 1)
    {
        fatorial_acumulado *= numero_entrada;
        numero_entrada--;
    }

    printf("O fatorial de %d (%d!) e: %ld\n", numero_original, numero_original, fatorial_acumulado);

    return 0;
}

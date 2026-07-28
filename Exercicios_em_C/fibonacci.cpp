#include <stdio.h>

unsigned long long calcular_fibonacci(int termo_alvo);

/*
 * Calcula o n-esimo termo da sequencia de Fibonacci usando iteracao.
 */
int main(void)
{
    int termo_desejado;
    unsigned long long resultado;

    printf("--- Gerador da Sequencia de Fibonacci ---\n");
    printf("Digite o termo que deseja saber (ex: 1, 2, 3...): ");

    if (scanf("%d", &termo_desejado) != 1 || termo_desejado <= 0)
    {
        printf("Erro: Por favor, insira um numero inteiro positivo.\n");
        return 1;
    }

    resultado = calcular_fibonacci(termo_desejado);

    printf("O %do termo da serie Fibonacci e: %llu\n", termo_desejado, resultado);

    return 0;
}

unsigned long long calcular_fibonacci(int termo_alvo)
{
    unsigned long long termo_anterior = 0;
    unsigned long long termo_atual = 1;
    unsigned long long proximo_termo;

    /* Casos base da sequencia. */
    if (termo_alvo == 1)
        return termo_anterior;
    if (termo_alvo == 2)
        return termo_atual;

    /* Calcula termo a termo a sequencia iterativamente. */
    for (int contador = 3; contador <= termo_alvo; contador++)
    {
        proximo_termo = termo_anterior + termo_atual;
        termo_anterior = termo_atual;
        termo_atual = proximo_termo;
    }

    return termo_atual;
}

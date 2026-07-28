#include <stdio.h>

/*
 * Conversor de temperatura: de Fahrenheit para Celsius.
 */
int main(void)
{
    int fahr;
    float celsius;

    printf("Digite a temperatura em Fahrenheit: ");
    if (scanf("%d", &fahr) == 1)
    {
        /* Formula de conversão: C = 5/9 * (F - 32) */
        celsius = 5.0 / 9.0 * (fahr - 32);

        printf("\nRESULTADO DA CONVERSAO:\n");
        printf("----------------------------\n");
        printf("FAHRENHEIT: %10d\n", fahr);
        printf("CELSIUS:    %+10.3f\n", celsius);
        printf("----------------------------\n");
    }
    else
    {
        printf("Erro: Por favor, insira um valor numerico inteiro.\n");
    }

    return 0;
}

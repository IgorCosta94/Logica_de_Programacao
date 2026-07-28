#include <stdio.h>

/*
 * Le tres valores inteiros e calcula soma, produto, media, maior e menor.
 */
int main(void)
{
    int primeiro_numero, segundo_numero, terceiro_numero;
    int valor_maximo, valor_minimo;
    int resultado_soma, resultado_produto;
    float resultado_media;

    printf("Analise Numerica: Digite tres valores inteiros: ");
    scanf("%d %d %d", &primeiro_numero, &segundo_numero, &terceiro_numero);

    resultado_soma = primeiro_numero + segundo_numero + terceiro_numero;
    resultado_produto = primeiro_numero * segundo_numero * terceiro_numero;
    resultado_media = resultado_soma / 3.0;

    printf("\n--- Resultados ---\n");
    printf("Soma Total:      %d\n", resultado_soma);
    printf("Media Aritmetica: %.2f\n", resultado_media);
    printf("Produto:         %d\n", resultado_produto);

    /* Determina o maior valor entre os tres numeros. */
    valor_maximo = primeiro_numero;
    if (segundo_numero > valor_maximo)
        valor_maximo = segundo_numero;
    if (terceiro_numero > valor_maximo)
        valor_maximo = terceiro_numero;

    /* Determina o menor valor entre os tres numeros. */
    valor_minimo = primeiro_numero;
    if (segundo_numero < valor_minimo)
        valor_minimo = segundo_numero;
    if (terceiro_numero < valor_minimo)
        valor_minimo = terceiro_numero;

    printf("Maior Valor:     %d\n", valor_maximo);
    printf("Menor Valor:     %d\n", valor_minimo);

    return 0;
}

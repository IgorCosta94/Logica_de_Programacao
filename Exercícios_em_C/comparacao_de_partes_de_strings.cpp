#include <stdio.h>
#include <string.h>

/*
 * Demonstração de comparacao parcial de strings usando strncmp e memcmp.
 */
int main(void)
{
    char a[100] = "C casa";
    char b[100] = "C carro";

    /*
     * strncmp compara strings como texto, até 5 caracteres ou até o termo nulo.
     * O valor retornado indica a ordem lexicográfica entre as strings.
     */
    printf("strncmp: %d\n", strncmp(a, b, 5));

    /*
     * memcmp compara os primeiros 4 bytes da memória sem tratar terminador de string.
     * É útil para comparar blocos de memória brutos.
     */
    printf("memcmp: %d\n", memcmp(a, b, 4));

    return 0;
}

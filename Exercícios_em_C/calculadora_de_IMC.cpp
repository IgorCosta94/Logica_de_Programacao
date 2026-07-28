#include <stdio.h>
#include <math.h>

/*
 * Calculadora de IMC: lê altura e peso do usuário,
 * calcula o índice de massa corporal e classifica o resultado.
 */
int main(void)
{
    float indice_massa_corporal, altura_do_usuario, peso_do_usuario;

    printf("--- Calculadora de IMC ---\n");

    printf("Digite sua altura em metros (ex: 1.75): ");
    if (scanf("%f", &altura_do_usuario) != 1 || altura_do_usuario <= 0)
    {
        printf("Erro: Altura invalida.\n");
        return 1;
    }

    printf("Digite seu peso em quilos (ex: 70.5): ");
    if (scanf("%f", &peso_do_usuario) != 1 || peso_do_usuario <= 0)
    {
        printf("Erro: Peso invalido.\n");
        return 1;
    }

    /* Formula do IMC: peso / altura^2 */
    indice_massa_corporal = peso_do_usuario / pow(altura_do_usuario, 2);

    printf("\nSeu IMC e: %.1f\n", indice_massa_corporal);
    printf("Classificacao: ");

    /* Classificação conforme valores do IMC. */
    if (indice_massa_corporal < 18.5)
    {
        printf("Abaixo do peso\n");
    }
    else if (indice_massa_corporal < 25.0)
    {
        printf("Peso normal\n");
    }
    else if (indice_massa_corporal < 30.0)
    {
        printf("Acima do peso (sobrepeso)\n");
    }
    else
    {
        printf("Obesidade\n");
    }

    return 0;
}

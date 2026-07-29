import java.util.Scanner;

public class SalarioTrabalhadores {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double[] salarios = new double[15];

        for (int i = 0; i < 15; i++) {
            System.out.printf("Digite o salario do trabalhador %d : ", i + 1);
            salarios[i] = scanner.nextDouble();
        }
       
        double soma = 0;
        for (int i = 0 ; i < 15; i++) {
            soma += salarios[i];
        }
        double mediaSalarial = soma / 15 ;

        int abaixoDaMedia = 0;
        int acimaDaMedia = 0;
        int naMedia = 0;

        for (int i = 0 ; i < 15; i++) {
            if (salarios[i] < mediaSalarial) {
                abaixoDaMedia += 1;
            } else if (salarios[i] > mediaSalarial) {
                acimaDaMedia += 1;
            } else {
                naMedia += 1;
            }
        }
        
        System.out.printf("\nMedia salarial: %.2f\n", mediaSalarial);
        System.out.println("Trabalhadores abaixo da media : " + abaixoDaMedia);
        System.out.println("Trabalhadores acima da media : " + acimaDaMedia);
        System.out.println("Trabalhadores na media : " + naMedia);

        scanner.close();
    }
}

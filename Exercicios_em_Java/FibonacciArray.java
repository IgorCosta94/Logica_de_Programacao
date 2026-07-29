

import java.util.Scanner;

public class FibonacciArray {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite o valor do termo que deseja saber: ");
        int n = scanner.nextInt();

        if (n < 0) {
            System.out.println("Por favor!Insira um valor positivo.");
        } else {
            
            int[] fibonacci = new int[n + 1];

            
            if (n >= 1) {
                fibonacci[0] = 0;
            }
            if (n >= 2) {
                fibonacci[1] = 1;
            }
            
            for (int i = 2; i <= n; i++) {
                fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2];
            }

            System.out.println("O termo " + n + " da sequencia de Fibonacci e: " + fibonacci[n]);
        }

        scanner.close();
    }
}

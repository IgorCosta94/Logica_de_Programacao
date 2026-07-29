
import java.util.Scanner;

public class NumeroConta {

    public static String obterNumeroContaCompleto(int numeroConta) {
        int somaDigitos = 0;
        int temp = numeroConta;
        
        while (temp != 0) {
            somaDigitos += temp % 10;
            temp /= 10;
        }
        
        int digitoVerificador = somaDigitos % 10;
       
        String numeroContaCompleto = String.format("%06d", numeroConta) + "-" + digitoVerificador;
        
        return numeroContaCompleto;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite o número da conta: ");
        int numeroConta = scanner.nextInt();

        String numeroContaCompleto = obterNumeroContaCompleto(numeroConta);
        System.out.println("Número da conta completo: " + numeroContaCompleto);

        scanner.close();
    }
}

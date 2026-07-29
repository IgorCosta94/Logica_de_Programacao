

public class CaixaLoja {

    public static double calcularDesconto(double total) {
        double desconto;
        if (total < 50) {
            desconto = total * 0.05;
        } else if (total <= 100) {
            desconto = total * 0.10;
        } else if (total <= 200) {
            desconto = total * 0.15;
        } else {
            desconto = total * 0.20;
        }
        return desconto;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double total = 0 , preco;
        System.out.print("Digite o preço da mercadoria (0 para sair): ");
        preco = scanner.nextDouble();
        
        while (preco != 0) {
            total += preco;
            System.out.print("Digite o preço da próxima mercadoria (0 para sair): ");
            preco = scanner.nextDouble();
        }
        
        double desconto = calcularDesconto(total);
        double valorAPagar = total - desconto;

        System.out.printf("Total: R$%.2f\n", total);
        System.out.printf("Desconto aplicado: R$%.2f\n", desconto);
        System.out.printf("Valor a ser pago pelo cliente: R%.2f\n" , valorAPagar);

        scanner.close();
    }
}

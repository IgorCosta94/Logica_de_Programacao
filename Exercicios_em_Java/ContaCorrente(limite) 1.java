import java.util.Scanner;

public class ContaCorrente {
    private int numeroConta;
    private String titular;
    private double saldo;
    private double limite;

    public ContaCorrente(int numeroConta, String titular, double saldoInicial, double limite) {
        this.numeroConta = numeroConta;
        this.titular = titular;
        this.saldo = Math.max(saldoInicial, 0);
        this.limite = limite;
    }

    public ContaCorrente(int numeroConta, String titular, double saldoInicial) {
        this(numeroConta, titular, saldoInicial, 1000.0); 
    }

    public ContaCorrente(int numeroConta, String titular) {
        this(numeroConta, titular, 0, 0); 
    }

    public void deposito(double quantia) {
        if (quantia > 0) {
            this.saldo += quantia;
            System.out.println("\nDepósito de R$" + quantia + " realizado com sucesso.");
        } else {
            System.out.println("Valor inválido para depósito.");
        }
    }

    public void saque(double quantia) {
        double saldoDisponivel = this.saldo + this.limite;
        if (quantia > 0 && saldoDisponivel >= quantia) {
            this.saldo -= quantia;
            System.out.println("Saque de R$" + quantia + " realizado com sucesso.\n");
        } else {
            System.out.println("Não foi possível realizar o saque por falta de recursos.");
        }
    }

    public void exibirDados() {
        System.out.println("Número da Conta: " + getNumeroConta());
        System.out.println("Titular da Conta: " + getTitular());
        System.out.println("\nSaldo da Conta: R$" + getSaldo());
        System.out.println("Limite da Conta: R$" + getLimite());
    }

    public int getNumeroConta() {
        return numeroConta;
    }

    public double getSaldo() {
        return saldo;
    }

    public double getLimite() {
        return limite;
    }

    public String getTitular() {
        return titular;
    }

    public void setTitular(String titular) {
        this.titular = titular;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite o número da conta: ");
        int numeroConta = scanner.nextInt();
        scanner.nextLine();

        System.out.print("Digite o nome do titular: ");
        String titular = scanner.nextLine();

        System.out.print("Digite o saldo inicial: ");
        double saldoInicial = scanner.nextDouble();

        ContaCorrente conta = new ContaCorrente(numeroConta, titular, saldoInicial);

        System.out.print("Digite o valor do depósito: ");
        double valorDeposito = scanner.nextDouble();
        conta.deposito(valorDeposito);

        System.out.print("Digite o valor do saque: ");
        double valorSaque = scanner.nextDouble();
        conta.saque(valorSaque);

        conta.exibirDados();

        scanner.close();
    }
}

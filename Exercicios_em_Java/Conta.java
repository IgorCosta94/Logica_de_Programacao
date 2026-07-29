

public class Conta {

    private int numeroConta;
    private String titular;
    private double saldo;


    public Conta(int numeroConta, String titular, double saldoInicial) {
        this.numeroConta = numeroConta;
        this.titular = titular;
        if (saldoInicial >= 0) {
            this.saldo = saldoInicial;
        } else {
            this.saldo = 0;
        }
    }


    public void deposito(double quantia) {
        if (quantia > 0) {
            this.saldo += quantia;
            System.out.println("Depósito de R$" + quantia + " realizado com sucesso.");
        } else {
            System.out.println("Valor inválido para depósito.");
        }
    }


    public void saque(double quantia) {
        if (quantia > 0 && this.saldo >= quantia) {
            this.saldo -= quantia;
            System.out.println("Saque de R$" + quantia + " realizado com sucesso.");
        } else {
            System.out.println("Saldo insuficiente ou valor inválido para saque.");
        }
    }


    public void exibirDados() {
        System.out.println("Número da Conta: " + this.numeroConta);
        System.out.println("Titular da Conta: " + this.titular);
        System.out.println("Saldo da Conta: R$" + this.saldo);
    }

  
    public static void main(String[] args) {

        Conta minhaConta = new Conta(123456, "Fulano de Tal", 1000);


        minhaConta.exibirDados();


        minhaConta.deposito(500);
        minhaConta.saque(200);

        
        minhaConta.exibirDados();
    }
}

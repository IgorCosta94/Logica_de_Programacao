
import java.util.Scanner;

public class Circulo {
    
    private double raio;


    public Circulo(double raio) {
        this.raio = raio;
    }

    
    public void setRaio(double raio) {
        this.raio = raio;
    }


    public double getRaio() {
        return this.raio;
    }

    
    public double calcularDiametro() {
        return 2 * raio;
    }


    public double calcularArea() {
        return Math.PI * Math.pow(raio, 2);
    }

    
    public double calcularCircunferencia() {
        return 2 * Math.PI * raio;
    }

    
    public void exibirDados() {
        System.out.printf("Diametro:%.2f\n" , calcularDiametro());
        System.out.printf("Area:%.2f\n" , calcularArea());
        System.out.printf("Circunferencia:%.2f\n" , calcularCircunferencia());
    }

    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Digite o raio do circulo: ");
        double raio = scanner.nextDouble();

        
        Circulo circulo = new Circulo(raio);

        
        circulo.exibirDados();

        
        System.out.print("Digite o novo raio do circulo: ");
        double novoRaio = scanner.nextDouble();
        circulo.setRaio(novoRaio);
        circulo.exibirDados();

        scanner.close();
    }
}

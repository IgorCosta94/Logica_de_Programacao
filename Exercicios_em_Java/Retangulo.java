

public class Retangulo {
    private double base;
    private double altura;

   
    public Retangulo(double base, double altura) {
        if (base <= 0 || altura <= 0) {
            this.base = 2;
            this.altura = 1;
        } else {
            this.base = base;
            this.altura = altura;
        }
    }

    
    public double getBase() {
        return base;
    }

    public double getAltura() {
        return altura;
    }

    public double calcularArea() {
        return base * altura;
    }

    public double calcularPerimetro() {
        return 2 * (base + altura);
    }

    public boolean ehQuadrado() {
        return base == altura;
    }

    public void imprimirInformacoes() {
        System.out.println("Base: " + base);
        System.out.println("Altura: " + altura);
        System.out.println("Area: " + calcularArea());
        System.out.println("Perimetro: " + calcularPerimetro());
        System.out.println("E um quadrado? " + ehQuadrado());
    }

    
    public static void main(String[] args) {
        Retangulo retangulo1 = new Retangulo(3, 4);
        Retangulo retangulo2 = new Retangulo(5, 5); 
        Retangulo retangulo3 = new Retangulo(-1, 6); 

        System.out.println("Informacoes sobre o retangulo 1:");
        retangulo1.imprimirInformacoes();

        System.out.println("\nInformacoes sobre o retangulo 2:");
        retangulo2.imprimirInformacoes();

        System.out.println("\nInformacoes sobre o retangulo 3:");
        retangulo3.imprimirInformacoes();
    }
}

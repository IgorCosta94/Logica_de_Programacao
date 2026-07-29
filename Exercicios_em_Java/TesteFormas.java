

import java.lang.Math;
import java.util.Scanner;


abstract class FormaGeometrica {
    protected int lados;

    public void setLados(int lados) {
        if (lados < 0) this.lados = 0;
        else this.lados = lados;
    }

    public abstract double area();

    public void imprime() {
        System.out.println("Numero de lados: " + lados);
        System.out.printf("Area: %.2f\n", area());
    }
}

class Circulo extends FormaGeometrica {
    private double raio;

    public Circulo(double raio) {
        setRaio(raio);
    }

    public void setRaio(double raio) {
        if (raio < 0) this.raio = 0;
        else this.raio = raio;
    }

    
    public double area() {
        return Math.PI * Math.pow(raio, 2);
    }
    public void imprime() {
        System.out.println("Dados do Circulo:");
        super.imprime();
        System.out.println("Raio: " + raio);
    }
}

class Retangulo extends FormaGeometrica {
    private double largura;
    private double altura;

    public Retangulo(double largura, double altura) {
        this.largura = largura;
        this.altura = altura;
        this.lados = 4; 
    }


    public double area() {
        return largura * altura;
    }

  
    public void imprime() {
        System.out.println("Dados do Retangulo:");
        super.imprime();
        System.out.println("Largura: " + largura);
        System.out.println("Altura: " + altura);
    }
}

class Triangulo extends FormaGeometrica {
    private double base;
    private double altura;

    public Triangulo(double base, double altura) {
        this.base = base;
        this.altura = altura;
        this.lados = 3;
    }

  
    public double area() {
        return (base * altura) / 2;
    }

  
    public void imprime() {
        System.out.println("Dados do Triângulo:");
        super.imprime();
        System.out.println("Base: " + base);
        System.out.println("Altura: " + altura);
    }
}

public class TesteFormas {
    public static void main(String[] args) {
        FormaGeometrica circulo = new Circulo(5);
        FormaGeometrica retangulo = new Retangulo(4, 6);
        FormaGeometrica triangulo = new Triangulo(3, 4);

        exibirInformacoes(circulo);
        exibirInformacoes(retangulo);
        exibirInformacoes(triangulo);
    }

    public static void exibirInformacoes(FormaGeometrica forma) {
        System.out.println("Informacoes das formas geometricas(Circulo, Retangulo e Triangulo):");
        forma.imprime();
        System.out.println("\n");
    }
}

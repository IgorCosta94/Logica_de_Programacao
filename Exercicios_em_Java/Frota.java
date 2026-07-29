
import java.util.Scanner;

class Veiculo {
    protected String modelo;
    protected String placa;
    protected int anoFabr;
    protected double valor;

    public Veiculo(String modelo, String placa, int anoFabr, double valor) {
        this.modelo = modelo;
        this.placa = placa;
        this.anoFabr = anoFabr;
        this.valor = valor;
    }

    public void imprime() {
        System.out.println("Modelo: " + modelo);
        System.out.println("Placa: " + placa);
        System.out.println("Ano de Fabricacao: " + anoFabr);
        System.out.println("Valor: " + valor);
    }
}

class Carro extends Veiculo {
    private int anoModelo;
    private int numPortas;

    public Carro(String modelo, String placa, int anoFabr, int anoModelo, int numPortas, double valor) {
        super(modelo, placa, anoFabr, valor);
        this.anoModelo = anoModelo;
        this.numPortas = numPortas;
    }

    @Override
    public void imprime() {
        super.imprime();
        System.out.println("Ano Modelo: " + anoModelo);
        System.out.println("Numero de Portas: " + numPortas);
    }
}

class Caminhao extends Veiculo {
    private double capacidade;
    private int numEixos;

    public Caminhao(String modelo, String placa, int anoFabr, double capacidade, int numEixos, double valor) {
        super(modelo, placa, anoFabr, valor);
        this.capacidade = capacidade;
        this.numEixos = numEixos;
    }

    @Override
    public void imprime() {
        super.imprime();
        System.out.println("Capacidade (toneladas): " + capacidade);
        System.out.println("Numero de Eixos: " + numEixos);
    }
}

public class Frota {
    public static void main(String[] args) {
        Scanner sInput = new Scanner(System.in);
        int tam, anoFabr, anoModelo, numPortas, numEixos;
        double capacidade, valor;
        String tipo, modelo, placa;

        System.out.println("Digite o tamanho da frota: ");
        tam = sInput.nextInt();
        sInput.nextLine(); 

        Veiculo[] frota = new Veiculo[tam];

        for (int i = 0; i < tam; i++) {
            System.out.println("Tipo do " + (i + 1) + ".o veiculo (a - auto/ c - caminhao): ");
            tipo = sInput.nextLine();

            if (!tipo.equalsIgnoreCase("a") && !tipo.equalsIgnoreCase("c")) {
                System.out.println("Tipo nao previsto");
                i--; 
                continue;
            }

            System.out.println("Modelo:");
            modelo = sInput.nextLine();

            System.out.println("Placa:");
            placa = sInput.nextLine();

            System.out.println("Ano Fabricacao:");
            anoFabr = sInput.nextInt();

            System.out.println("Valor:");
            valor = sInput.nextDouble();

            if (tipo.equalsIgnoreCase("a")) {
                System.out.println("Ano Modelo: ");
                anoModelo = sInput.nextInt();
                System.out.println("Portas: ");
                numPortas = sInput.nextInt();
                frota[i] = new Carro(modelo, placa, anoFabr, anoModelo, numPortas, valor);
            } else if (tipo.equalsIgnoreCase("c")) {
                System.out.println("Capacidade (toneladas): ");
                capacidade = sInput.nextDouble();
                System.out.println("Num de Eixos: ");
                numEixos = sInput.nextInt();
                frota[i] = new Caminhao(modelo, placa, anoFabr, capacidade, numEixos, valor);
            }
            sInput.nextLine();
        }

        for (int i = 0; i < tam; i++) {
            System.out.println("Veiculo n.o " + (i + 1));
            if (frota[i] != null) {
                frota[i].imprime();
            }
            System.out.println();
        }
        sInput.close();
    }
}

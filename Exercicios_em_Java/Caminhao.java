

public class Caminhao extends Veiculo {
    private double capacidade;
    private int numeroEixos;

   
    public Caminhao(String modelo, String placa, int anoFabricacao, double valor, double capacidade, int numeroEixos) {
        super(modelo, placa, anoFabricacao, valor);
        this.capacidade = capacidade;
        this.numeroEixos = numeroEixos;
    }

    public double getCapacidade() {
        return capacidade;
    }

    public void setCapacidade(double capacidade) {
        this.capacidade = capacidade;
    }

    public int getNumeroEixos() {
        return numeroEixos;
    }

    public void setNumeroEixos(int numeroEixos) {
        this.numeroEixos = numeroEixos;
    }

    public void imprimirDadosCaminhao() {
        super.imprimirDados(); 
        System.out.println("Capacidade: " + capacidade);
        System.out.println("Numero de Eixos: " + numeroEixos);
    }

/*                       PROGRAMA TESTE
                                ||
                               \  /
                                \/                                                                           */
    public static void main(String[] args) {
        Caminhao meuCaminhao = new Caminhao("Volvo", "XYZ5678", 2018, 150000, 20000, 4);

        System.out.println("Dados do caminhao:");
        meuCaminhao.imprimirDadosCaminhao();
    }
}

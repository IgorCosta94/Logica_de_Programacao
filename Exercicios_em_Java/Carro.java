

public class Carro extends Veiculo {
    private int numeroPortas;
    private int anoModelo;

   
    public Carro(String modelo, String placa, int anoFabricacao, double valor, int numeroPortas, int anoModelo) {
        super(modelo, placa, anoFabricacao, valor);
        this.numeroPortas = numeroPortas;
        this.anoModelo = anoModelo;
    }

   
    public int getNumeroPortas() {
        return numeroPortas;
    }

    public void setNumeroPortas(int numeroPortas) {
        this.numeroPortas = numeroPortas;
    }

    public int getAnoModelo() {
        return anoModelo;
    }

    public void setAnoModelo(int anoModelo) {
        this.anoModelo = anoModelo;
    }

    
    public void imprimirDadosCarro() {
        super.imprimirDados(); 
        System.out.println("Numero de Portas: " + numeroPortas);
        System.out.println("Ano do Modelo: " + anoModelo);
    }
    
                        /* PROGRAMA TESTE*
                                ||
                               \  /
                                \/     */
    
    public static void main(String[] args) {
        Carro meuCarro = new Carro("Sedan", "ABC1234", 2020, 50000, 4, 2020);

        System.out.println("Dados do carro:");
        meuCarro.imprimirDadosCarro();
    }
}

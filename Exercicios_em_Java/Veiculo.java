

public class Veiculo {
    private String modelo;
    private String placa;
    private int anoFabricacao;
    private double valor;

    public Veiculo(String modelo, String placa, int anoFabricacao, double valor) {
        this.modelo = modelo;
        this.placa = placa;
        this.anoFabricacao = anoFabricacao;
        this.valor = valor;
    }

    public void setModelo(String modelo) {
        this.modelo = modelo;
    }

    public String getModelo() {
        return modelo;
    }

    public void setPlaca(String placa) {
        this.placa = placa;
    }

    public String getPlaca() {
        return placa;
    }

    public void setAnoFabricacao(int anoFabricacao) {
        this.anoFabricacao = anoFabricacao;
    }

    public int getAnoFabricacao() {
        return anoFabricacao;
    }

    public void setValor(double valor) {
        this.valor = valor;
    }

    public double getValor() {
        return valor;
    }

    public void depreciar(double taxa) {
        this.valor -= this.valor * (taxa / 100);
    }

    public void imprimirDados() {
        System.out.println("Modelo: " + modelo);
        System.out.println("Placa: " + placa);
        System.out.println("Ano de Fabricacao: " + anoFabricacao);
        System.out.println("Valor: " + valor);
    }


                   /*PROGRAMA TESTE*
                           ||
                          \  /
                           \/     */
                           
    public static void main(String[] args) {
        
        Veiculo meuCarro = new Veiculo("Sedan", "ABC1234", 2020, 50000);

        System.out.println("Dados do veiculo antes da depreciacao:");
        meuCarro.imprimirDados();

        meuCarro.depreciar(10);

        System.out.println("\nDados do veiculo apos a depreciacao:");
        meuCarro.imprimirDados();
    }
}

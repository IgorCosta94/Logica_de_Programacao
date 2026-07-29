import java.util.Scanner;
class Banco{
   
   public static void main(String[]jarvis){
      Scanner leia = new Scanner(System.in);
      Conta conta = new Conta();
      int op;
      do{
         System.out.println("Bem vindo ao Banco Queremos Dinherio");
         System.out.println("1 = Consultar Saldo");
         System.out.println("2 = Depositar Valor");
         System.out.println("3 = Sacar Valor");
         System.out.println("4 = Sair");
         op = leia.nextInt();
         switch(op){
            case 1:
               System.out.printf("Saldo atual: R$ %.2f\n",conta.consultarSaldo());
            break;
            case 2:
               System.out.print("Digite o valor para depositar: ");
               conta.depositarValor(leia.nextDouble());
            break;
            case 3:
               System.out.print("Digite o valor que voce quer sacar: ");
               conta.sacarValor(leia.nextDouble());
            break;
         }
      }while(op != 4);
   }
   
}

import java.util.Scanner;

public class PontoNoPlano {
   
   public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Quantos pares de pontos devem ser lidos?");
        int n = scanner.nextInt();
        
        for (int i = 0; i < n; i++) {
            System.out.printf("Digite as coordenadas do ponto %d (x): ", i + 1);
            double x = scanner.nextDouble();
            System.out.printf("Digite as coordenadas do ponto %d (y): ", i + 1);
            double y = scanner.nextDouble();
            
            String resultado = classificarPonto(x, y);
            System.out.printf("Ponto %d: (%.1f , %.1f) esta no %s\n", i + 1, x, y, resultado);
        }
        
        scanner.close();
    }

    public static String classificarPonto(double x, double y) {
        if (x == 0 && y == 0) {
            return "Origem";
            
        } else 
               if (x == 0) {
               return "Eixo Y";
            
        } else 
                if (y == 0) {
                  return "Eixo X";
            
        } else 
               if (x > 0 && y > 0) {
                   return "Quadrante Q1";
            
        } else 
               if (x < 0 && y > 0) {
                  return "Quadrante Q2";
            
        } else 
                if (x < 0 && y < 0) {
                  return "Quadrante Q3";
            
        } else { 
               return "Quadrante Q4";
        }
    }

 
}

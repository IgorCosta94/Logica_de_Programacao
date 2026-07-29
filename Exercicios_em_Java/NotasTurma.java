


import java.util.Scanner;

public class NotasTurma {
   
    public static void main(String args[]) {
      
        final int ALUNOS = 5;
        final int PROVAS = 2;
      
        int lin, col;
        double mediaTurma = 0;
        double somaNotas = 0;
        int totalNotas = ALUNOS * PROVAS;
      
        double notas[][] = new double[ALUNOS][PROVAS];
        Scanner entrada = new Scanner(System.in);
      
        for (lin = 0; lin < ALUNOS; lin++) {
         
            System.out.printf("\nDigite as notas do %do aluno: ", lin + 1);
         
            for (col = 0; col < PROVAS; col++) {
                notas[lin][col] = entrada.nextDouble();
                somaNotas += notas[lin][col];
            }
        }
      
        mediaTurma = somaNotas / totalNotas;
      
        System.out.println();
        System.out.println("Notas e Media");
      
        for (lin = 0; lin < ALUNOS; lin++) {
            System.out.printf("\nAluno %d: ", lin + 1);
            double mediaAluno = 0;
         
            for (col = 0; col < PROVAS; col++) {
                System.out.printf("%2.2f ", notas[lin][col]);
                mediaAluno += notas[lin][col];
            }
            
            mediaAluno /= PROVAS;
            
            System.out.printf("- Media: %2.2f", mediaAluno);
            
            if (mediaAluno > mediaTurma) {
                System.out.print(" - Acima da media ");
            } else if (mediaAluno < mediaTurma) {
                System.out.print(" - Abaixo da media");
            } else {
                System.out.print(" - Na media ");
            }
        }
        
        System.out.printf("\n\nMedia da turma: %2.2f\n", mediaTurma);
    }
}
  
      




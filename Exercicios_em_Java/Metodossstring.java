

import java.util.Scanner; 

public class Metodossstring
{

   public static void main ( String args[] )
      {
         Scanner input = new Scanner ( System.in );
    
         String nome = " Champy ";
         String nome2 = " Sistema Solar ";
         
         int numero1 = 100;
         double numero2 = 100.50;
         boolean booleano = numero1 > numero2;
         
         
         //Primeiro método CharAt
         System.out.printf( "Primeiro Metodo CharAt\n " );
        
         System.out.printf("Saida: %s\n",nome.charAt(1));
         System.out.printf(" Saida: %s\n",nome2.charAt(4));
         
         
         // Segundo método codePointAt
         System.out.printf( "\nSegundo Metodo codePointAt\n " );
        
         System.out.printf("Saida: %s\n",nome.codePointAt(1));
         System.out.printf(" Saida: %s\n",nome2.codePointAt(5));
         
         
         //Terceiro método valueOf
         System.out.printf( "\nTerceiro Metodo valueOf\n " );
        
         System.out.printf("Saida: %s\n",String.valueOf(numero1));
         System.out.printf(" Saida: %s\n",String.valueOf(numero2));
         System.out.printf(" Saida: %s\n",String.valueOf(booleano));
      }
}


import java.util.Scanner; 


public class Triangulo
{

   public static void main ( String args[ ] ) 
      {
 
         Scanner input = new Scanner ( System.in );
         int lado_a , lado_b , lado_c;
         boolean teste_de_existencia;
                  
         
         System.out.print ( " Para verificar a condicao de existencia de um triangulo digite tres valores.\n Cada valor representa um lado do triangulo.\n " );
         
         System.out.print ( "Lado A: " );
         lado_a = input.nextInt();
         
         System.out.print ( " Lado B: " );
         lado_b = input.nextInt();
         
         System.out.print ( " Lado C: " );
         lado_c = input.nextInt();
         
         teste_de_existencia = lado_a + lado_b > lado_c &&  lado_a + lado_c > lado_b &&  lado_b + lado_c > lado_a;
         
         if( teste_de_existencia ) 
         
               System.out.print ( "A condicao de existencia foi satisfeita. Os lados A , B e C formam um triangulo.\n " );
               
          else 
          
               System.out.print ( "Os lado A , B e C NAO satisfazem a condicao de existencia de um triangulo.\n " );
               
          if(teste_de_existencia && lado_a == lado_b && lado_b == lado_c)
          
            System.out.print ( "Os lados A , B e C formam um triangulo equilatero.\n " );
            
          if( teste_de_existencia && lado_a == lado_b && lado_a != lado_c || lado_a == lado_c && lado_a != lado_b || lado_b == lado_c && lado_b != lado_a )
          
             System.out.print ( "Os lado A , B e C formam um triangulo isosceles.\n " );
               
          if( teste_de_existencia &&  lado_a != lado_b && lado_a != lado_c && lado_b != lado_c) 
          
            System.out.print ( "Os lado A , B e C formam um triangulo escaleno.\n " );
        
      }
}

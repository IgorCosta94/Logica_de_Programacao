

import java.util.Scanner; 

public class Convertemperatura
{

   public static void main ( String args[ ] ) 
      {
         Scanner input = new Scanner ( System.in );
         float temperatura_celsius;
         float temperatura_fahrenheit;
         
         
         System.out.print ( "Digite uma temperatura em Fahrenheit que será convertida para Celsius: " );
         temperatura_fahrenheit = input.nextFloat();
         
         temperatura_celsius = ( temperatura_fahrenheit - 32 ) *   5 / 9 ;
         
         System.out.printf("Valor da Temperatura em Celsius: %.4f" ,temperatura_celsius );
      }
}

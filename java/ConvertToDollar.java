import java.util.Scanner;

// DIESES PROGRAMM KANN FEHLER BEINHALTEN!


public class Main {
    public static void main(String[] args) {
//SCANNER
        System.out.println("Geben Sie bitte Ihren Betrag in Euro ein: ");
    Scanner scanner = new Scanner(System.in);
//VARIABLE
    Double eur = scanner.nextDouble();
    ConvertToDollar(eur);
    }
    public static void ConvertToDollar(Double eur) {

        Double dollar = eur * 1.10;
        System.out.println(dollar + "$");
        

    }
}

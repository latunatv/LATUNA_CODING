import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

            Scanner scanner = new Scanner(System.in);
            System.out.println("Gebe hier die gewünschte Rechenart ein:");
            String rechenart = scanner.nextLine();

            if (rechenart.equals("Addition")) {
                System.out.println("Gebe hier den Wert der ersten Zahl ein: ");
                Float a = scanner.nextFloat();
                Float b = scanner.nextFloat();
                Float ergebnis = a + b;
                System.out.println("Dein Ergebnis ist " + ergebnis);

            } else if (rechenart.equals("Subtraktion")) {
                System.out.println("Gebe hier den Wert der ersten Zahl ein: ");
                Float a = scanner.nextFloat();
                Float b = scanner.nextFloat();
                Float ergebnis = a - b;
                System.out.println("Dein Ergebnis ist " + ergebnis);

            } else if (rechenart.equals("Multiplikation")) {

                System.out.println("Gebe hier den Wert der ersten Zahl ein: ");
                Float a = scanner.nextFloat();
                Float b = scanner.nextFloat();
                Float ergebnis = a * b;
                System.out.println("Dein Ergebnis ist " + ergebnis);

            } else if (rechenart.equals("Division")) {

                System.out.println("Gebe hier den Wert der ersten Zahl ein: ");
                Float a = scanner.nextFloat();
                Float b = scanner.nextFloat();
                Float ergebnis = a / b;
                System.out.println("Dein Ergebnis ist " + ergebnis);

            }
            else {


                System.out.println("Ein Fehler ist aufgetaucht!");
            }

        System.out.println("Vielen Dank fürs Verwenden!");
    }
    }

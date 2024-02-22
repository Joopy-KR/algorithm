import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int total = 0;

        for (int i = 0; i < 5; i++) {
            int score = scanner.nextInt();
            if (score < 40) {
                total += 40;
            } else {
                total += score;
            }
        }

        int result = total / 5;
        System.out.println(result);
    }
}

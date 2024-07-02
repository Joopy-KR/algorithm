import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] arr = new int[6];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = sc.nextInt();
        }
        int T = sc.nextInt();
        int P = sc.nextInt();

        double total_tshirt = 0;
        for (int i: arr) {
            total_tshirt += Math.ceil((double) i / (double) T);
        }
        System.out.println((int) total_tshirt);
        int total_pen = N / P;
        System.out.print(total_pen + " ");
        System.out.println(N - (P * total_pen));
    }
}

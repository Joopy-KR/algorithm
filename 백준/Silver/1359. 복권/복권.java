import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int N = scanner.nextInt();
        int M = scanner.nextInt();
        int K = scanner.nextInt();

        double result = 0;
        double possible_cnt = Combination(N, M);

        while (M >= K) {
            if (N - M < M - K) {
                K++;
                continue;
            }

            double c = Combination(M, K) * Combination(N - M, M - K);

            result += c / possible_cnt;
            K++;
        }

        System.out.println(result);
    }

    public static long Combination(int n, int r) {
        if(n == r || r == 0) {
            return 1;
        } else {
            return Combination(n - 1, r - 1) + Combination(n - 1, r);
        }
    }
}

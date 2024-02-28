import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        solution(2, N);
        solution(3, N);
        solution(5, N);
        solution(7, N);
    }

    static boolean isPrime(int X) {
        for (int i = 2; i < (X / 2) + 1; i++) {
            if (X % i == 0) {
                return false;
            }
        }
        return true;
    }

    static void solution(int number, int N) {
        if (Integer.toString(number).length() == N) {
            System.out.println(number);
        } else {
            for (int i = 1; i < 10; i++) {
                if (i % 2 == 0) {
                    continue;
                }
                if (isPrime(number * 10 + i)) {
                    solution(number * 10 + i, N);
                }
            }
        }
    }
}

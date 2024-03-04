import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        double repeat = Math.ceil((double) N / 4.0);
        for (int i = 0; i < repeat; i++) {
            System.out.print("long ");
        }
        System.out.println("int");
    }
}

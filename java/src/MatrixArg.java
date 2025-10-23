import java.util.Random;
public class MatrixArg {
    public static void main(String[] args) {
        int n = (args.length > 0) ? Integer.parseInt(args[0]) : 1024;
        double[][] a = new double[n][n];
        double[][] b = new double[n][n];
        double[][] c = new double[n][n];
        Random random = new Random(42);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                a[i][j] = random.nextDouble();
                b[i][j] = random.nextDouble();
            }
        }
        long start = System.nanoTime();
        for (int i = 0; i < n; i++) {
            for (int k = 0; k < n; k++) {
                double aik = a[i][k];
                double[] bk = b[k];
                double[] ci = c[i];
                for (int j = 0; j < n; j++) {
                    ci[j] += aik * bk[j];
                }
            }
        }
        long end = System.nanoTime();
        System.out.printf("%.6f%n", (end - start) / 1e9);
    }
}

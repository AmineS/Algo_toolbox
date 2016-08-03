import java.util.*;

public class LCM {
  private static long gcd(long a, long b) {
    long t = 0;
    while (b != 0) {
      t = b;
      b = a % b;
      a = t;
    }
    return a;
  }

  private static long lcm(long a, long b) {
    return (long)(a * b) / gcd(a, b);
  }

  public static void main(String args[]) {
    Scanner scanner = new Scanner(System.in);
    long a = scanner.nextLong();
    long b = scanner.nextLong();
    System.out.println(lcm(a, b));
  }
}

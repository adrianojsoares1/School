/*Professor Marlowe
 *Linear Algebra
 *Integration using Trapezoid, Midpoint, and Simpson method
 *Written by Adriano Soares and Michael Grassi
 *5/1/2017
 */

import java.text.DecimalFormat;
interface InputExpression {double f(double x);}
interface R{double f(double x, double y, double z);}

public class Integration {

    private static double TrapezoidMethod(double a, double b, int N, InputExpression x){

        double d = (b - a) / N;
        double sum = 0; //First + Last sum

        //Trapezoid Rule: Integral = Delta(x) / 2 * [f(x0) + 2f(x1) + 2f(x2) ... + 2f(xn) + f(x(n+1))]
        for (double i = a; i < b; i+=d) {
            double cur = x.f(i), next = x.f(i + d);
            sum += (d * cur) + (d * (next - cur) / 2);
        }
        return sum;
    }

    //Integration using midpoint
    private static double Midpoint(double a, double b, int N, InputExpression x){
        double d = (b - a) / N, sum = 0;
        for (double i = a; i < b; i+=d) {
            sum += x.f(((i + i + d) / 2));
        }
        return d * sum;
    }
    //Simpson Method of Integration
    private static double SimpsonMethod(double a, double b, int N, InputExpression x){
        double d = (b - a) / (N - 1);
        double sum = (double)(1 / 3) * (x.f(a) + x.f(b));

        for (int i = 1; i < N - 1; i += 2) {
            double num = a + (d * i);
            sum += (double)(4 / 3) * x.f(num);
        }
        for (int i = 2; i < N - 1; i += 2) {
            double num = a + d * i;
            sum += (double)(2 / 3) * x.f(num);
        }
        return sum * d * 2;
    }

    //Tests
    public static void main(String[] args) {
        DecimalFormat round = new DecimalFormat("#0.000");
        InputExpression equation = (double x) -> Math.pow(Math.E, x) / Math.pow(x, 2);

        int interval_1 = 50;
        int interval_2 = 100;

        //Lambda expression to save some code
        R richardson = (double x, double y, double z) -> y + ((Math.pow(interval_2, z) * Math.pow(interval_1, z)) /
                (Math.pow(interval_2, z) - Math.pow(interval_1, z))) *
                (y - x) * (1 / Math.pow(interval_2, z));

        double Trap_1 = TrapezoidMethod(1, 4, interval_1, equation);
        double Trap_2 = TrapezoidMethod(1, 4, interval_2, equation);
        double Trap_3 = richardson.f(Trap_1, Trap_2, 4);

        double Midpoint_1 = Midpoint(1, 4, interval_1, equation);
        double Midpoint_2 = Midpoint(1, 4, interval_2, equation);
        double Midpoint_3 = Midpoint_2 + (interval_2 * interval_1) / (interval_2 - interval_1) *
                (Midpoint_2 - Midpoint_1) * (1/interval_2);

        double Simpson_1 = SimpsonMethod(1, 4, interval_1, equation);
        double Simpson_2 = SimpsonMethod(1, 4, interval_2, equation);
        double Simpson_3 = richardson.f(Simpson_1, Simpson_2, 4);


        //Print out tests
        System.out.println("Function: (e ^ x) / (x ^ 2)");
        System.out.println("Interval: [a, b] -> [1, 4] \n");
        System.out.println("                  Trap |  Mid  | Simpson\n");

        System.out.println("50 intervals	"+round.format(Trap_1)+"	"
                + round.format(Midpoint_1)+"	"+round.format(Simpson_1));
        System.out.println("100 intervals	"+round.format(Trap_2)+"	"+round.format(Midpoint_2)
                +"	"+round.format(Simpson_2));
        System.out.println("Richardson's    "+round.format(Trap_3)+"	"+round.format(Midpoint_3)
                +"	"+round.format(Simpson_3));
    }
}
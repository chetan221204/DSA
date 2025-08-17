import java.util.Scanner;

public class greater {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a ,b;
        System.out.println("Enter number a: ");
        a =sc.nextInt();
        System.out.println("Enter number b:");
        b =sc.nextInt();
        if(a>b){
            System.out.println(a+": is Greater");
        }
        else
            System.out.println(b+": is Greater");
    
    }
}

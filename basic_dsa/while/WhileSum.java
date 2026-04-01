 
import java.util.Scanner;

public class WhileSum {

 

    public static void main(String[] args) {
        int n ;
        Scanner sc =new Scanner(System.in);
        System.out.println("enter a number");
        n =sc.nextInt();
         int sum=0;
            int i=1;
            while(i<=n){
              
                sum= sum +i;
                i=i+1;
            }  System.out.println(sum);
    }
}    
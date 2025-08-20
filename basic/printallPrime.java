import java.util.Scanner;

public class printallPrime {
    public static void main(String[] args) {
        int count=0;
        Scanner sc =new Scanner(System.in);
        System.out.println("Enter a number: ");
        int n =sc.nextInt();
        for(int i=1;i<=n;i++){
            count = 0; // Reset count for each number
            for(int j=1;j<=i;j++){
                if(i%j==0){
                    count++;
                }
            }
            if(count==2){
                System.out.println(i + " is a Prime Number");
            }
        }
    }
}

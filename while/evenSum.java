import java.util.Scanner;

public class evenSum {
    public static void main(String[] args) {
        int i=1;
        Scanner sc = new Scanner(System.in);
        int n= sc.nextInt();
      
        int sum=0;
        while(i<=n ){
            if(i%2==0){
                 sum=sum+i;
                }
                i=i+1;
           


        }System.out.println(sum);
    }
}

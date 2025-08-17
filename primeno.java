import java.util.Scanner;

public class primeno {
    public static void main(String[] args) {
            Scanner sc =new Scanner(System.in);
            System.out.println("Enter a num");
           int  n= sc.nextInt();

           int count=0;
           for(int i=2;i<n;i++){
            if(n%i==0){
                count++;
            }
            if(count==0){
                System.out.println("Its Prime");
            }
            else{
                System.out.println("not prime");
            }
           }
             
    }    
}
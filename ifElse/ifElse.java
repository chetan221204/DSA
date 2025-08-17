import java.util.Scanner;

public class ifElse {

    public static void main(String[] args) {
        int x;
        Scanner sc =new Scanner(System.in);
        System.out.println("Enter a number:");
        x = sc.nextInt();
        if(x>0){
            System.out.println( x +" is possitive number");
        }
        else{
            System.out.println(x+" 40is negative number");
        }
    }
}

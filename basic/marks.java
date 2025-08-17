import java.util.Scanner;

public class marks {
public static void main(String[] args) {
    Scanner sc =new Scanner(System.in);
    System.out.println("Enter Your Marks:");
    int x = sc.nextInt();
    if(x>90){
        System.out.println("Excellent");
    }
    else if(x>80){
        System.out.println("good");

     } else if(x>70){
            System.out.println("fair");
        }

        else if(x>60){
            System.out.println("meets expectations");
        }
        else if(x<60){
            System.out.println("below par");
        }

    }
}    


import java.util.Scanner;

public class switchCase {

    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a digit:");
        int n= sc.nextInt();
        switch (n) {
            case 1:   System.out.println("Monday");
                
                break;
            case 2: System.out.println("Tuesday");

                break;
            
            case 3: System.out.println("Wednesday");

                break;

            case 4: System.out.println("Thusday");

                break;
            
            case 5: System.out.println("Friday");

                break;
            case 6: System.out.println("Saturday");

                break;
 

            default: System.out.println("sunday");
                break;
        }
    }
    
}

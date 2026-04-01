package DSA;

public class Array1 {

    //  public static void main(String[] args) {

    //     int [] arr=  {0,2,3,0,4,5};
    //     int j=0;
    //     for(int i=0;i<arr.length;i++){
    //         if(arr[i]!=0){
    //             int temp = arr[i];
    //             arr[i]=arr[j];
    //             arr[j]=temp;
    //             j++;
                
    //         }
    //     }
    //     for(int i:arr){
    //         System.out.print(i+" ");
        
    // }
    //  }

    public static void main(String[] args){
        int [] arr = {2,13,4,5,6};
        int j=0;
        for(int i=0;i<arr.length;i++){
            if(arr[i]%2==0){
                int temp = arr[i];
                arr[i]=arr[j];
                arr[j]=temp;
                j++;
            }
        }
        for(int i:arr){
            System.out.print(i+" ");
            }
    
    }
}


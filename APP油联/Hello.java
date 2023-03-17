import java.util.Scanner;
import java.util.ArrayList;

public class Hello {
    public static void main(String[] args){
        System.out.print("请输入：");

        Scanner input = new Scanner(System.in);
        String text = input.nextLine();

        ArrayList data = new ArrayList();
        data.add("alex");
        data.add("海军");

        System.out.print(text);
    }
}


// interface List{
//     public void add(Object data);
// }

// class ArrayList implements List{
//     public void add(Object data){
        
//     }
// }

// class LinkedList implements List{
//     public void add(Object data){

//     }
// }



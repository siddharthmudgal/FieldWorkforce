package Loktra;

import java.io.InputStreamReader;
import java.util.Scanner;

import static Loktra.Constants.keys;
import static Loktra.Constants.keysLength;
import static Loktra.Constants.menu;

public class ReverseHashProblem {

    public static void main(String[] args){
        if (args.length != 0){
            int length = args.length;
            for (int i = 0; i < length; i++){
                System.out.println("Hash -> "+args[i]+"\tString -> "+reverseHash(Long.valueOf(args[i])));
            }
        }
        else{
            Scanner scanner = new Scanner(new InputStreamReader(System.in));
            long hash;
            int choice;
            while (true){
                System.out.println(menu);
                choice = scanner.nextInt();
                if (choice == 2 || (choice != 2 && choice != 1))
                    break;
                hash = scanner.nextLong();
                System.out.println(reverseHash(hash));
            }
        }
    }

    /**
     * @param hash - takes hash key as input
     * @return - String as output
     */
    public static String reverseHash(long hash){
        String message = "";
        long temp = hash;
        long div = 37L;
        int rem;
        while (temp > 7L ){
            rem = (int) (temp % div);
            if (rem > keysLength)
                return "Invalid Hash";
            message = keys.charAt(rem) + message;
            temp = temp / div;
        }
        if (temp != 7L)
            return "Invalid Hash";
        return message;
    }
}

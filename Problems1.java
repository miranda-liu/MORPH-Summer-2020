/**
 * Problems1
 */
public class Problems1 {

    public static void main(String[] args) {
        /*testing reverseArray
        String[] arr1 = {"h", "i"};
        reverseArray(arr1);
        System.out.println("");

        String[] arr2 = {"H", "i"};
        reverseArray(arr2);
        System.out.println("");

        String[] arr3 = {"a", "a"};
        reverseArray(arr3);
        System.out.println("");

        String[] arr4 = {""};
        reverseArray(arr4);
        System.out.println("");

        String[] arr5 = {"a", "A", "A", "a", "b", "B", "b", "C", "a"};
        reverseArray(arr5);
        System.out.println("");

        String[] arr6 = {"h", "h"};
        reverseArray(arr6);
        System.out.println("");
        */

        /*testing isPalindrome
        System.out.println(isPalindrome("aa"));
        System.out.println(isPalindrome("a"));
        System.out.println(isPalindrome("aba"));
        System.out.println(isPalindrome("abccdccba"));
        System.out.println(isPalindrome(""));
        System.out.println(isPalindrome("Aa"));
        System.out.println(isPalindrome("abcdefga"));
        */

        //testing returnIndices
        int[] arr1 = {1, 4, 5, 9, 2, -1};
        System.out.println(returnIndices(arr1, 7));
        System.out.println(returnIndices(arr1, 5));
        System.out.println(returnIndices(arr1, 15));

    }

    public static void reverseArray(String[] arr){
        String place = "";
        for(int i = 0; i < arr.length; i++){
            place = arr[i];
            arr[i]= arr[arr.length - 1];
            arr[arr.length - 1] = place;
        }
        for(String str : arr){
            System.out.print(str + "   ");
        }
    }

    public static boolean isPalindrome(String str){
    int length = str.length();
    for(int i = 0; i < str.length()/2; i++){
            if(!str.substring(i,i+1).equals(str.substring(length-i-1, length-i))){
                return false;
            }
        }
        return true;
    }

    public static String returnIndices(int[] arr, int target){
        for(int i = 0; i < arr.length; i++){
            for(int j = 1; j < arr.length; j++){
                if(arr[i] + arr[j] == target){
                    return i + ", " + j; 
                }
            }
        }
        return "can't be found";
    }
}
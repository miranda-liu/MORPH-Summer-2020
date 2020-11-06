import java.util.Arrays;
public class Problems3{
    //basic math
    public void o1(int a, int b){
        System.out.println(a+b);
    }
    //binary search, ask about recursion
    public int oLogN(int target, int low, int high, int[] n){
        Arrays.sort(n);
        int mid = (low + high)/2;
        if(low > high){
            return -1;
        }
        else if(n[mid] == target){
            return mid;
        }
        else if(n[mid] > target){
            high = mid - 1;
            return oLogN(target, low, high, n);
        }
        else{
            low = mid + 1;
            return oLogN(target, low, high, n);
        }
    }
    //adding up all numbers from 1 to n
    public void oN(int n){
        int count = 0;
        for(int i = 1; i <= n; i++){
            count += i;
        }
        System.out.println(count);
    }
    //nested loop
    public void oN2(int n){
        int count = 0;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                count = count + i + j;
            }
        }
    }

    public void oN3(int n){
        int count = 0;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                for(int k = 0; k < n; k++){
                count = count + i + j + k;
                }
            }
        }
    }
    //an infinite loop
    public void OInfinity(int n){
        int i = 0;
        while(i < n){
            System.out.println(i);
        }
    }
}
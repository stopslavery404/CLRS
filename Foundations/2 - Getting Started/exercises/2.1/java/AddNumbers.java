/**
 * 
 * ALGORITHM: Incremental
 * INPUT: Two n-bit binary arrays
 * OUTPUT: One (n+1)-bit binary array representing sum of two n-bit binary arrays.
 * TIME COMPLEXITY: O(n)
 * 
 * */

public class AddNumbers {
	/*main method*/
    public static void main(String[] args) {
       
       /*input binary arrays - initial*/
       int[] num1 = {1,1,0,1,0,1,0,1}; // 213
       int[] num2 = {1,0,1,0,0,0,1,1}; // 163

       int[] res = new int[num1.length+1];


        
       /*algo starts*/
        int carry = 0;
        int sum = 0;
        int ind = res.length-1;

        for(int index = num1.length-1; index > -1; index--) {
           sum = (carry + num1[index] + num2[index]);
           res[ind--] = sum % 2;
           carry = sum / 2;
        }

        if(carry>0) res[ind] = carry;
       /*algo ends*/

       System.out.println(java.util.Arrays.toString(res)); // Expected : [1, 0, 1, 1, 1, 1, 0, 0, 0] = 376
    }	
}

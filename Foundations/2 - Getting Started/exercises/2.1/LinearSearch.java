/**
 * 
 * ALGORITHM: Linear Search
 * INPUT: Sequence of elements and a value to find
 * OUTPUT: position of val in case it exists else -1 (0-indexed)
 * TIME COMPLEXITY: O(n)
 * 
 * */

public class LinearSearch {
   /*main method*/
    public static void main(String[] args) {
       
       /*input array - initial*/
       int[] arr = {1,4,2,5,3,9,8,6,7};

       /*input value to search*/
       int val = 9;
       
       /*to store position of val, default value -1*/
       int pos = -1;
        
       /*algo starts*/
       
       for(int index = 0; index < arr.length; index++) {
           /*check if current element equal to val*/
           if(val==arr[index]) {

               /*we found it , note it and break out of loop, no need to check more*/
               pos = index;
               break;
           }

       }
       /*algo ends*/

       System.out.println(pos); // Expected : 5
    } 
}
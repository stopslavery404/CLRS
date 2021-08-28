/**
 * 
 * ALGORITHM: Insertion Sort
 * INPUT: Sequence of elements
 * OUTPUT: Descending order sequence of same elements
 * TIME COMPLEXITY: O(n^2)
 * 
 * */

public class InsertionSortDescending {
	/*main method*/
    public static void main(String[] args) {
       
       /*input array - initial*/
       int[] arr = {1,4,2,5,3,9,8,6,7};


        
       /*algo starts
         
        NOTE : Invariant maintained is that for each iteration of outer loop 
               all elements from [0,index] are sorted in descending order.
               You can prove it using PMI and this statement prove the correctness
               of algorithm.

       */

       for(int index = 1; index < arr.length; index++) {
            /*curElement*/
            int key = arr[index];
            int prevIndex = index - 1;

            //loop for searching a position for key
            while(prevIndex>-1 && arr[prevIndex]<key) {
            	arr[prevIndex+1] = arr[prevIndex];
            	prevIndex--;
            }

            arr[prevIndex+1] = key;

       }
       /*algo ends*/

       System.out.println(java.util.Arrays.toString(arr)); // Expected : [9, 8, 7, 6, 5, 4, 3, 2, 1]
    }	
}

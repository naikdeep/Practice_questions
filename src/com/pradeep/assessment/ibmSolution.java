package com.pradeep.assessment;

public class ibmSolution {
	public static void findTopTwo(int[] arr) {
		int n=arr.length;
		int firstMax= Integer.MIN_VALUE;
		int secondMax = Integer.MIN_VALUE;
		int counter=0;
		int prevMax= Integer.MIN_VALUE;
		for (int i=0;i<n;i++) {
			
			if(arr[i]>firstMax) {
				firstMax= arr[i];
				counter++;
			}
			
			
			if (secondMax<prevMax) {
				secondMax = prevMax;
			}
			prevMax =firstMax;
			
		}
		System.out.println("firstMax is : " +firstMax +" second max is :" + secondMax);
		
	}
    public static void main(String[] args) {
    	int[] arr= {4,2,3,1};
    	findTopTwo(arr);
	    
    	
    }
}

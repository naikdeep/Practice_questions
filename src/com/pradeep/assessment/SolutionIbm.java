package com.pradeep.assessment;

public class SolutionIbm {
	
	/**
	 * @param arr
	 */
	public static  void twoMaxEle(int[] arr) {
		
		int lh=arr.length;
		if (lh==0 || lh ==1) {
			return;
		}
		int firstMax = Integer.MIN_VALUE;
		int secondMax = Integer.MIN_VALUE;
		boolean flag = false;
		for (int i=1;i<lh;i++) {
			
			if (arr[i]>firstMax) {
				firstMax=arr[i];
			}
			if (arr[i-1]>secondMax && arr[i-1]<=firstMax) {
				secondMax =arr[i-1];
			
			}
			
		}
		if (arr[0]>firstMax) {
			firstMax=arr[0];
		}
		if (arr[lh-1]>secondMax) {
			secondMax =arr[lh-1];
		}
		System.out.println("first max is :"+ firstMax + " secondMax is :" + secondMax);
		
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int [] arrex= {1,2,4,5,6,10,10,11,9,8};
        twoMaxEle(arrex);
	}

}

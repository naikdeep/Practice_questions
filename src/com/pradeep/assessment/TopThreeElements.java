package com.pradeep.assessment;

import java.util.Arrays;

public class TopThreeElements {
	public static int[] topThree(int[] arr,int n) {
		
		int first=  Integer.MIN_VALUE;
		int second = Integer.MIN_VALUE;
		int three = Integer.MIN_VALUE;
		for (int i=0;i<n;i++) {
			if (arr[i]>first) {
				second = first;
				first = arr[i];
				}
			if (second<arr[i] && arr[i]<first) {
				three = second;
				second = arr[i];
				}
			if (three< arr[i] && arr[i]<second) {
				three = arr[i];
				}
		}
		int[] ans=new int[3];
		ans[0] = first;
		ans[1] = second;
		ans[2] = three;
		return ans;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] qtn= {1,2,2,2,4,56,7};
		int[] ans= topThree(qtn,7);
     System.out.println(Arrays.toString(ans));
	}

}

package com.pradeep.assessment;


public class Solution {
		  static int sumOfNumsInStr(String str){
		    
		    int sum=0;
		    char[] charArr=str.toCharArray();
		    int n=str.length();
		    System.out.println(n);
		    int i=0;
		    while(i<n-1){
		      int j=i+1;
		      if ((((int)charArr[i])>=48) && (((int)charArr[i])<=57)){
		         int num= (int) charArr[i]-48;
		         while((((int)charArr[j])>=48) && (((int)charArr[j])<=57)&&(j<n-1)){
		        	 //System.out.println(num);
		              num=num*10;
		              num=num+((int)charArr[j]-48);
		              
		              j++;
		             }
		         //System.out.println(num);
		          if((j==n-1) &&((int)charArr[j])>=48 && ((int)charArr[j])<=57 ){
		        	  num=num*10;
		        	  num=num+((int)charArr[j]-48);
		          }
		         sum+=num;
		      }
		      i=j;
		      

		    }
		    return sum;
		  }
		  public static void main(String[] args){
		    //String str="a1b8b1d777ee5ef1n";
		    // output = 793
		    //System.out.println(sumOfNumsInStr(str));
		    //System.out.println(Integer.parseInt("2"));
		    String str2="a11b8b1d785ee5ef10";
		    System.out.println(sumOfNumsInStr(str2));
		    
		  }
		}

	


package com.pradeep.assessment;

import java.util.HashSet;
import java.util.Set;

public class RemoveDuplicate {
     public static HashSet<String> removeDuplicateString(String[] arr){
    	 int len = arr.length;
    	 HashSet<String> set =new HashSet<>();
    	 int i=0;
    	 while(i<len) {
    		 set.add(arr[i]);
    		 i++;
    	 }
    	 return set;
     }
	
    public static void main(String[] args) {
		// TODO Auto-generated method stub
	String[] qtn = 	{"bottle" , "pen" ,"book", "bottle", "basket"};
	HashSet<String> ans = removeDuplicateString(qtn);
	String name = "pradeep";
	String name1= "pradeep";
	System.out.println(name.hashCode());
	System.out.println(name1.hashCode());
	
    System.out.println(ans);
	
	}

}

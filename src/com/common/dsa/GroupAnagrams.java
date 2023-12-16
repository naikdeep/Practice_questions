package com.common.dsa;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
public class GroupAnagrams {
	public static ArrayList<ArrayList<String>> groupByAnagrams(String[] arr,int n){
		ArrayList<ArrayList<String>> ans=new ArrayList<>();
		
		HashMap<String,ArrayList<String>> map=new HashMap<>();
		
		int i=0;
		
		while (i<n) {
		   char[] strArr=arr[i].toCharArray();
		   Arrays.sort(strArr);
		   String sortedString=String.valueOf(strArr);
		   
		   if (map.containsKey(sortedString)) {
			   ArrayList<String> groupedStr=map.get(sortedString);
			   groupedStr.add(arr[i]);
		   }
		   else {
			    ArrayList<String> groupedStr=new ArrayList<>();
			    groupedStr.add(arr[i]);
			    map.put(sortedString, groupedStr);
			    
			    }
		   i++;
		   
		}
		for (String key:map.keySet()) {
			ArrayList<String> groups= map.get(key);
			ans.add(groups);
		}
		return ans;
		
		
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String [] qtn= {"ton","six","ton","evil","xis","cat","act","ball","llab"};
		System.out.println(groupByAnagrams(qtn,9));

	}

}

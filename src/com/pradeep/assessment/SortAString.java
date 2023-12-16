package com.pradeep.assessment;

import java.util.Arrays;

import ortjava.lang.Object;

public class SortAString extends Object {
	int n;
	SortAString(int n){
		this.n=n;
	}
      public void printEven() throws InterruptedException {
    	  synchronized(this) {
    		  for (int i=2;i<=10;i++) {
    			  if (i%2==0) {
    				  System.out.println("even num "+ i );
    				  notify();
    			  }
    			  else {
    				  wait();
    			  }
    		  }
    	  }
    	  
    	  
      }
      public void printOdd() {
    	  synchronized(this) {
    		  for (int i=1;i<=10;i++) {
    			  if (i%2!=0) {
    				  System.out.println("odd num "+ i );
    			  }
    		  }
    	  }
    	  
    	  
      }
      
	public static void main(String[] args) {
		// TODO Auto-generated method stub
     String name= "pradeep";
     System.out.println(name);
     char[] nameChar= name.toCharArray();
     Arrays.sort(nameChar);
     System.out.println(nameChar);
     name = nameChar.toString();
     SortAString obj1=new SortAString(10);
     Runnable r1=()->{ obj1.printOdd();};
     Runnable r2= ()->{obj1.printEven();};
     
     Thread t1=new Thread(r1);
     Thread t2=new Thread(r2);
     t1.start();
     t2.start();
     
     
     
	}

}

import sys

def maxSumSubArray(arr,k):
    i=0
    n=len(arr)
    sum=0
    maxSum=0
    while(i<k):
        sum+=arr[i]
        i+=1
    maxSum=sum
    while(i<n):
        sum-=arr[k-i]
        sum+=arr[i]
        if sum>maxSum:
            maxSum=sum
            
        i+=1
    return maxSum

print(maxSumSubArray([-1,2,3,4,-2],3))




    

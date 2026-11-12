class Solution {
    public int longestMonotonicSubarray(int[] nums) {
        int a=1;
        int b=1;
        for (int i=1;i<nums.length;i++){
            if (nums[i]>nums[i-1]){
                a++;
                b=Math.max(a,b);
            }
            else{
                a=1;
            }
        }
        int c=1;
        int d=1;
        for (int i=1;i<nums.length;i++){
            if(nums[i]<nums[i-1]){
                c++;
                d=Math.max(c,d);
            }
            else{
                c=1;
            }
        }
        return Math.max(b,d);

        
    }
}
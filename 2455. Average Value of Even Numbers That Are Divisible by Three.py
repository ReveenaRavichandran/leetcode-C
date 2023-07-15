2455. Average Value of Even Numbers That Are Divisible by Three

int averageValue(int* nums, int numsSize)
{
    int c,s,i,a;
    c=0;
        s=0;
        for(i=0;i<numsSize;i++)
            if(nums[i]%2==0 && nums[i]%3==0)
            {
                s=s+nums[i];
                c+=1;
            }
        if (c>0)
        {
            a=s/c;
            return a;
        }
        else
            return 0;

}

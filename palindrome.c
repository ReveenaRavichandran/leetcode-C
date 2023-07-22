bool isPalindrome(int x)
{
    int m,r;
    long  s=0;
    m=x;

while(x!=0)
{
    r=x%10;
    s=s*10+r;
    x=x/10;
}

if(m==s && m>=0)
return true;
else
return false;
}
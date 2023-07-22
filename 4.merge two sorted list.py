class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l=[]
        for i in nums1:
            l.append(i)
        for j in nums2:
            l.append(j)
        l.sort()
        n=len(l)
        if(n%2!=0):
            return l[n//2]
        else:
            y=n//2
            x=float((l[y]+l[y-1]))/2
        return x
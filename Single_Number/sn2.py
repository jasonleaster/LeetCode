"""
Programmer  :   EOF
Code date   :   2015.03.02
file        :   sn.py
e-mail      :   jasonleaster@gmail.com

Code description :

　　　　　　　Given an array of integers, every element appears 
twice except for one. Find that single one.

Note:
	Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?

	In this solution, I sort the inputed @array by 
@counting sort which is a very fast algorithm which's runtime complexity
is O(n). BUT I have to use extra memory to solve this problem by
this method.


"""
class Solution():

    def counting_sort(self, array) :
        array_size = len(array)

        max_value = 0

        for i in range(0, array_size) :
            if max_value < array[i] :
                max_value = array[i]

        buf_size = max_value+1

        buf = [0] * buf_size
        ret = [0] * array_size

        for i in range(0, array_size) :
            buf[array[i]] += 1

        for i in range(1, buf_size) :
            buf[i] += buf[i-1]

        for i in range(array_size-1, -1, -1) :
            ret[buf[array[i]] - 1] = array[i]
            buf[array[i]] -= 1

        return ret

    def singleNumber(self, A) :

        A = self.counting_sort(A)
        length = len(A)
        for i in range(0, length, 2) :
            if i < length-2 and A[i] != A[i+1] :
                return A[i]
            elif i == length-1 :
                return A[i]

#----------for testing ----------------

array = [1,2,3,4,5,4,3,2,1]

s = Solution()
print s.singleNumber(array)

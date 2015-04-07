class Solution:

    def Q_sort(self, A, i, j):
        if i < j:
            k = self.partition(A, i, j)
            A = self.Q_sort(A, i, k-1)
            A = self.Q_sort(A, k+1, j)

        return A

    def partition(self, A, p, r):
        x = A[r]
        i = p - 1
        for j in range(p, r):
            if A[j] <= x:
                i += 1
                A[i], A[j] = A[j], A[i]

        A[i+1], A[r] = A[r], A[i+1]

        return i+1

    def findMedianSortedArrays(self, A, B):
        if A is None and B is None:
            return

        C = A + B
        C = self.Q_sort(C,0, len(C)-1)

        print C

        if len(C) % 2 is 0:
            return (C[len(C)//2] + C[len(C)//2 - 1])/(2.0)
        else:
            return C[len(C)//2]*(1.0)


#----------testing---------------

#A = [1,5,3,9,2]
#B = [8,7,4,6]
A = [1]
B = [2]

s = Solution()
print "A: ", A, "B: ", B
print "Median of two sorted array : ", s.findMedianSortedArrays(A, B)



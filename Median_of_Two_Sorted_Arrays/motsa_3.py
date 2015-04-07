class Solution:

    def parent(self, i):
        return i/2

    def left(self, i):
        return i*2

    def right(self, i):
        return (i*2 + 1)

    def heap_size(self, A):
        return A[0]

    def init_input(self, A):
        size = len(A)
        A = [size] + A

        return A

    def max_heapify(self, A, i):
        l = self.left(i)
        r = self.right(i)

        if l < self.heap_size(A) and A[l] > A[i]:
            largest = l
        else:
            largest = i

        if r < self.heap_size(A) and A[r] > A[largest]:
                largest = r

        if largest != i:
            A[i], A[largest] = A[largest], A[i]
            self.max_heapify(A, largest)

        return A

    def build_max_heap(self, A):
        hs = self.heap_size(A)
        for i in range(hs/2, 0, -1):
            A = self.max_heapify(A, i)

        return A

    def heap_sort(self, A):

        A = self.init_input(A)

        for i in range(len(A)-1, 0, -1):
            A[1], A[i] = A[i], A[1]

            A[0] -= 1
            self.max_heapify(A, 1)

        return A


    def findMedianSortedArrays(self, A, B):
        if A is None and B is None:
            return

        C = A + B
        C = self.heap_sort(C)

        print C

        if len(C) % 2 is 0:
            return (C[len(C)//2] + C[len(C)//2 - 1])/(2.0)
        else:
            return C[len(C)//2]*(1.0)


#----------testing---------------

#A = [1,5,3,9,2]
#B = [8,7,4,6]
A = [10000]
B = [10001]

s = Solution()
print "A: ", A, "B: ", B
print "Median of two sorted array : ", s.findMedianSortedArrays(A, B)



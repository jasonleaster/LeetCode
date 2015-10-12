class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        S1 = (C - A) * (D - B)
        S2 = (G - E) * (H - F)
        
        if (C > E) and H > B:
            S3 = (C - E) * (H - B)
        else:
            S3 = 0
        
        return S1 + S2 - S3
# -------- test --------

s = Solution()
A = 0
B = 0
C = 0
D = 0
E = -1
F = -1
G = 1
H = 1
s.computeArea(A, B, C, D, E, F, G, H)

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end   = len(nums) - 1
        
        pivot = 0
        while start <= end:
            mid = (start + end)/2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                pivot = mid
                i = pivot
                j = pivot
                
                while nums[pivot] == nums[i]:
                    i -= 1
                    if i < 0:
                        break
                    
                while nums[pivot] == nums[j]: 
                    j += 1
                    if j == len(nums):
                        break
                return [i+1, j-1]
                
        return [-1, -1]

#-----------------------------
array = [1]
target = 1

s = Solution()
print s.searchRange(array, target)

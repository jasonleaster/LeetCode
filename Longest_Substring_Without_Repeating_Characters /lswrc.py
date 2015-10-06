"""
Programmer	:	EOF
e-mail		:	jasonleaster@gmail
Date		:	2015.04.02
File		:	lswrc.py

"""

class Solution:

    # @return an integer
    def lengthOfLongestSubstring(self, s):
    	Table = [-1 for i in range(0, 256)]

    	maxLen = 0
    	lastRepeatPos = -1

    	"""
    	 We will use @ord() function to translate the character
    	 into the number of it's ascii code.
    	"""
       	for i in range(0, len(s)):
    		if Table[ord(s[i])] != -1 and lastRepeatPos < Table[ord(s[i])]:
    			lastRepeatPos = Table[ord(s[i])]
    		
    		if i - lastRepeatPos > maxLen :
    			maxLen = i - lastRepeatPos

    		Table[ord(s[i])] = i

    	return maxLen

#---------- just for testing ----------

s = Solution()

print s.lengthOfLongestSubstring("c")
print s.lengthOfLongestSubstring("abcdababcde")
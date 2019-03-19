# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:
#
# All given inputs are in lowercase letters a-z.


class Solution:
    def longestCommonPrefix(self, strs):
        if 0 == len(strs):
            return ''
        prefix = []
        for pos in range(len(strs[0])):
            for _str in strs[1:]:
                if len(_str) == pos or _str[pos] != strs[0][pos]:
                    return ''.join(prefix)
            prefix.append(strs[0][pos])
        #import pdb;pdb.set_trace()
        return ''.join(prefix)




def LCP():
    input_str=  ["flower","flow","flight"]
    solution = Solution()
    aa = solution.longestCommonPrefix(input_str)
    #import pdb;pdb.set_trace()
    print(aa)


#############################################
if (__name__ == "__main__"):
    LCP()
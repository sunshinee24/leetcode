# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
# #
# # A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
# #
# #
# #
# # Example:
# #
# # Input: "23"
# # Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

class Solution:
    def letterCombinations(self, digits):
        def dfs(num, string, res):
            if num == length:
                res.append(string)
                return
            for letter in dict[digits[num]]:
                dfs(num + 1, string + letter, res)

        dict = {'2': ['a', 'b', 'c'],
                '3': ['d', 'e', 'f'],
                '4': ['g', 'h', 'i'],
                '5': ['j', 'k', 'l'],
                '6': ['m', 'n', 'o'],
                '7': ['p', 'q', 'r', 's'],
                '8': ['t', 'u', 'v'],
                '9': ['w', 'x', 'y', 'z']
                }
        res = []
        length = len(digits)
        dfs(0, '', res)
        if len(res[0]) == 0:
            res = []
        return res

def LC():
    input_str=  ""
    solution = Solution()
    aa = solution.letterCombinations(input_str)
    #import pdb;pdb.set_trace()
    print(aa)


#############################################
if (__name__ == "__main__"):
    LC()
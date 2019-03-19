# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]



class Solution:
    def generateParenthesis(self, n):
        results = []
        self.DFS_gen(n, n, "", results)
        return results

    def DFS_gen(self, right, left, result, results):
        if right > left:
            return
        if left == 0 and right == 0:
            results.append(result)
        else:
            if right > 0:
                self.DFS_gen(right-1, left, result+'(', results)
            if left > 0:
                self.DFS_gen(right, left-1, result+')', results)



if __name__ == "__main__":
    n = 3
    result = Solution().generateParenthesis(n)
    print(result)


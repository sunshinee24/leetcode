# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.
#
# Example 1:
#
# Input: "()"
# Output: true
# Example 2:
#
# Input: "()[]{}"
# Output: true
# Example 3:
#
# Input: "(]"
# Output: false
# Example 4:
#
# Input: "([)]"
# Output: false
# Example 5:
#
# Input: "{[]}"
# Output: true
import pdb
class Solution:
    def isValid(self, ss):
        # str_dict = {'{':[], '}':[], '[':[], ']':[], '(':[], ')':[] }
        # _strs = list(s)
        # for _str in _strs:
        #     if _str == '{' or _str == '[' or _str == '(':
        #        str_dict[_str].append(_str)
        #     elif _str == ')':
        #         if len(str_dict['}']) == 0 and len(str_dict[']']) == 0:
        while '()' in ss:
            ss = ss.replace('()', '')
        while '[]' in ss or '()' in ss:
            ss = ss.replace('[]', '')
            ss = ss.replace('()', '')

        while '{}' in ss or '[]' in ss or '()' in ss:
            ss = ss.replace('{}', '')
            ss = ss.replace('[]', '')
            ss = ss.replace('()', '')

        if ss == '':
            return True
        else:
            return False








if __name__ == "__main__":
    input = "([])"
    result = Solution().isValid(input)
    print(result)
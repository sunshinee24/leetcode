class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # area=min(height[right], height[left])*(right-left)
        if (height == [] or len(height) < 2):
            return 0

        left = 0
        right = len(height) - 1
        max_area = 0
        while (left < right):
            max_area = max(max_area, min(height[right], height[left]) * (right - left))
            #import pdb;pdb.set_trace()
            #print(max_area)
            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1
        return max_area

if __name__ == "__main__":
    input = [1,8,6,2,5,4,8,3,7]
    result = Solution().maxArea(input)
    print(result)
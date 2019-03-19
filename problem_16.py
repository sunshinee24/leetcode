class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #min(a+b+c)
        import  sys
        length = len(nums)
        array = nums[:]  # 可以直接对nums排序，不要深拷贝
        array.sort()
        result = 0
        dif = 100000
        for i in range(length):
            j = i+1
            k = length -1
            while j < k:
                #print(i,j,k)
                sum = array[i] + array[j] + array[k]
                dif_temp = abs(sum - target)
                if dif_temp < dif:
                    dif = dif_temp
                    result = sum
                if sum < target:
                    j = j + 1
                else:
                    k = k - 1
        return result



if __name__ == "__main__":
    nums = [-1, 2, 1, -4]
    target = 1
    result = Solution().threeSumClosest(nums, target)
    print(result)
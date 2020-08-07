
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

# 给定 nums = [2, 7, 11, 15], target = 9

# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]

#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime


class Solution:
    def twoSum(self, nums, target):
        length = len(nums)
        result = []
        j = 0
        for i in range(length):
            temp = nums[i+1:]
            if (target - nums[i]) in temp:
                j = temp.index(target - nums[i]) + i + 1
                break
        if j > 0:
            result = [i, j]
        return result


if __name__ == '__main__':
    # list = [3, 2, 4, 5, 6, 7]
    # print(list[7:])

    start_time = datetime.datetime.now()
    s = Solution()
    result = s.twoSum([3, 2, 4], 6)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)

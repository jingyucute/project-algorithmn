'''
Description:
Author: jingyu
Date: 2020-08-10 11:43:25
LastEditors: Please set LastEditors
LastEditTime: 2020-08-11 15:53:27
'''

# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

#  

# 示例：

# 输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
#  

# 提示：

# 3 <= nums.length <= 10^3
# -10^3 <= nums[i] <= 10^3
# -10^4 <= target <= 10^4


import datetime


class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        #   固定第一个， 后面两个用双指针,
        # 决策: 如果 nums[first] + nums[second] + nums[third] > target 则 third 减到合适位置
        #  nums[first] + nums[second] + nums[third] > target 则 second 加到合适位置
        length = len(nums)
        nums.sort()

        list = []
        min_w = 2000
        for first in range(length):
            if first > 1 and nums[first] == nums[first-1]:
                continue
            second = first + 1
            third = length - 1
            while second < third:
                sum = nums[first] + nums[second] + nums[third]
                if sum == target:
                    min_w = 0
                    list = [nums[first], nums[second], nums[third]]
                    return target
                if abs(sum - target) < min_w:
                    min_w = abs(sum - target)
                    list = [nums[first], nums[second], nums[third]]
                if sum > target:
                    third_t = third - 1
                    while second < third_t and nums[third] == nums[third_t]:
                        third_t -= 1
                    third = third_t
                else:
                    second_t = second + 1
                    while second_t < third and nums[second_t] == nums[second]:
                        second_t += 1
                    second = second_t

        # print(list)
        result = 0
        for n in list:
            result += n

        return result


if __name__ == '__main__':

    start_time = datetime.datetime.now()
    solution = Solution()
    l = [0, 2, 1, -3]
    target = 1
    result = solution.threeSumClosest(l, target)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)

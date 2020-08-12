'''
Description:
Author: jingyu
Date: 2020-08-10 11:43:25
LastEditors: Please set LastEditors
LastEditTime: 2020-08-12 22:51:58
'''

# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

# 注意：

# 答案中不可以包含重复的四元组。

# 示例：

# 给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

# 满足要求的四元组集合为：
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]


import datetime


class Solution:
    def fourSum(self, nums, target: int):
        # 双指针
        # 总结一下， 当有多个值变动时， 先固定其它的， 然后留下两个相邻的指针作为移动
        # first second third fourth 可以 先固定 first 和 second， 然后 留下 third 和 fourth 进行双指针移动
        nums.sort()
        result = []
        length = len(nums)
        for first in range(length - 3):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            for second in range(first + 1, length - 2):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                third, fourth = second + 1, length - 1
                while third < fourth:
                    # print(first, second, third, fourth)
                    sum = nums[first] + nums[second] + nums[third]+nums[fourth]
                    if sum > target:
                        fourth -= 1
                    elif sum < target:
                        third += 1
                    else:
                        result.append([nums[first], nums[second],
                                       nums[third], nums[fourth]])
                        while third < fourth and nums[third] == nums[third+1]:
                            third += 1
                        while third < fourth and nums[fourth] == nums[fourth-1]:
                            fourth -= 1
                        third += 1
                        fourth -= 1

        return result

    def fourSum1(self, nums, target: int):
        #   这个应该算是四重循环， 并不是所谓的双指针
        nums.sort()
        result = []
        length = len(nums)
        for first in range(length - 3):
            if first > 0 and nums[first] == nums[first-1]:
                continue
            for second in range(first+1, length - 2):
                if second > first + 1 and nums[second] == nums[second-1]:
                    continue
                fourth = length - 1
                for third in range(second + 1, length - 1):
                    if third > second + 1 and nums[third] == nums[third-1]:
                        continue
                    while third < fourth and nums[first] + nums[second] + nums[third]+nums[fourth] > target:
                        fourth -= 1
                    if third < fourth and nums[first] + nums[second] + nums[third]+nums[fourth] == target:
                        result.append([nums[first], nums[second],
                                       nums[third], nums[fourth]])


if __name__ == '__main__':

    start_time = datetime.datetime.now()
    solution = Solution()
    digits = "233"
    nums = [-1, 0, 1, 2, -1, -4]
    target = -1
    result = solution.fourSum(nums, target)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)

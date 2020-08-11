'''
Description:
Author: jingyu
Date: 2020-08-10 11:43:25
LastEditors: Please set LastEditors
LastEditTime: 2020-08-11 12:40:00
'''

# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

# 注意：答案中不可以包含重复的三元组。

#  

# 示例：

# 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]


import datetime


class Solution:
    # 暴力算法， 时间上通不过
    def threeSum(self, nums):
        result = []
        length = len(nums)
        if length < 3:
            return result
        nums.sort()
        num_set = set()
        for i in range(length-2):
            for j in range(i+1, length - 1):
                for k in range(j + 1, length):
                    if nums[i] + nums[j] + nums[k] == 0:
                        s = str(nums[i]) + str(nums[j]) + str(nums[k])
                        # print(s, num_set)
                        if s not in num_set:
                            num_set.add(s)
                            result.append([nums[i], nums[j], nums[k]])

        return result

    def threeSum1(self, nums):
        result = []
        length = len(nums)
        if length < 3:
            return result
        nums.sort()

        for first in range(length):
            if first > 0 and nums[first] == nums[first-1]:
                # -2 -2 -1 3 4
                # 第一个 -2 可以组成 -2 -2  4 和 -2 -1 3
                # 第二个 -2 可以组成 -2 -1 3，被第一个包含，
                continue
            thrid = length - 1
            target = -nums[first]
            for second in range(first + 1, length - 1):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    # 在一有重复数字的序列中， 只要保证 a 和 b 没有重复的， c就不会重复
                    # -2 -2 -1 -1 3 4  自己组合吧
                    continue
                while second < thrid and nums[thrid] + nums[second] > target:
                    thrid -= 1
                if thrid > second and nums[second] + nums[thrid] == target:
                    result.append([nums[first], nums[second], nums[thrid]])

        return result


if __name__ == '__main__':

    start_time = datetime.datetime.now()
    solution = Solution()
    l = [-1, 0, 1, 2, -1, -4]
    l = [1, 2, -2, -1]
    result = solution.threeSum1(l)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)

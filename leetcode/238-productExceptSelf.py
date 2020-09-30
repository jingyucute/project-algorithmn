'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-30 11:48:04
'''

# 给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

#  

# 示例:

# 输入: [1,2,3,4]
# 输出: [24,12,8,6]
#  

# 提示：题目数据保证数组之中任意元素的全部前缀元素和后缀（甚至是整个数组）的乘积都在 32 位整数范围内。

# 说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。

# 进阶：
# 你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）


# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/product-of-array-except-self
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    # 简单点 超时
    def productExceptSelf(self, nums):
        length = len(nums)
        result = [1] * length

        for i in range(length):
            for j in range(length):
                if i == j:
                    continue
                else:
                    result[j] *= nums[i]
        return result

    def productExceptSelf1(self, nums):
        length = len(nums)
        L, R = [1] * length, [1] * length
        for i in range(1, length):
            L[i] = L[i - 1] * nums[i - 1]
            j = length - i - 1
            R[j] = R[j + 1] * nums[j + 1]

        ans = []
        for i in range(length):
            ans.append(L[i] * R[i])
        return ans

    # 内存优化
    def productExceptSelf2(self, nums):
        length = len(nums)
        ans = [1] * length
        for i in range(1, length):
            ans[i] = ans[i - 1] * nums[i - 1]
        R = 1
        for i in range(1, length):
            j = length - i - 1
            R = R * nums[j + 1]
            ans[j] = ans[j] * R
        return ans


if __name__ == '__main__':
    nums = [0, 0]
    solution = Solution()
    start_time = datetime.datetime.now()
    result = solution.productExceptSelf2(nums)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)

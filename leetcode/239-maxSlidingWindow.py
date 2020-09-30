'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-30 15:44:06
'''

# 给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。
# 你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

# 返回滑动窗口中的最大值。

#  

# 进阶：

# 你能在线性时间复杂度内解决此题吗？

#  

# 示例:

# 输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
# 输出: [3,3,5,5,6,7]
# 解释:

#   滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
#  

# 提示：

# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 1 <= k <= nums.length


# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/sliding-window-maximum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    def maxSlidingWindow(self, nums, k: int):

        # 暴力算法
        # n = len(nums)
        # if n * k == 0:
        #     return []

        # return [max(nums[i:i + k]) for i in range(n - k + 1)]
        n = len(nums)

        if n * k == 0:
            return []
        if k == 1:
            return nums
        left = [0] * n
        left[0] = nums[0]
        right = [0] * n
        right[n - 1] = nums[n - 1]
        for i in range(1, n):
            # from left to right
            if i % k == 0:
                # block start
                left[i] = nums[i]
            else:
                left[i] = max(left[i - 1], nums[i])
            # from right to left
            j = n - i - 1
            if (j + 1) % k == 0:
                # block end
                right[j] = nums[j]
            else:
                right[j] = max(right[j + 1], nums[j])

        output = []
        for i in range(n - k + 1):
            output.append(max(left[i + k - 1], right[i]))

        return output


if __name__ == '__main__':
    # nums = [1, -1]
    # k = 1
    # nums = [1, 3, -1, -3, 5, 3, 6, 7]
    # k = 3
    nums = [7, 2, 4]
    k = 2
    solution = Solution()
    start_time = datetime.datetime.now()
    result = solution.maxSlidingWindow(nums, k)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)

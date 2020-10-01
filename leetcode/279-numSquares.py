'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-10-01 23:48:06
'''

# 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

# 示例 1:

# 输入: n = 12
# 输出: 3
# 解释: 12 = 4 + 4 + 4.
# 示例 2:

# 输入: n = 13
# 输出: 2
# 解释: 13 = 4 + 9.

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/perfect-squares
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

import datetime


class Solution:
    def numSquares(self, n: int) -> int:
        nums = []
        i = 1
        while i**2 <= n:
            nums.append(i**2)
            i += 1
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            for num in nums:
                if i < num:
                    break
                dp[i] = min(dp[i], dp[i-num] + 1)
        return dp[n]


if __name__ == '__main__':
    n = 16
    solution = Solution()
    start_time = datetime.datetime.now()
    result = solution.numSquares(n)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)

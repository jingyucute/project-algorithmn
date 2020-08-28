'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-29 00:19:50
'''

# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

# 注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

# 示例 1:

# 输入: [3,3,5,0,0,3,1,4]
# 输出: 6
# 解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
#      随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
# 示例 2:

# 输入: [1,2,3,4,5]
# 输出: 4
# 解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
#      注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
#      因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
# 示例 3:

# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。


#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:

    def maxProfit(self, prices) -> int:
        if not prices:
            return 0
        length = len(prices)
        dp = [[[0, 0, 0], [0, 0, 0]] for _ in range(length)]
        dp[0][0][0] = 0
        # 第一天买入
        dp[0][1][0] = -prices[0]
        # 第一天不可能有卖出
        dp[0][0][1] = float('-inf')
        dp[0][0][2] = float('-inf')
        dp[0][1][1] = float('-inf')
        dp[0][1][2] = float('-inf')

        for i in range(1, length):

            # 未持股 未卖出
            dp[i][0][0] = 0
            # 未持股， 有卖出
            dp[i][0][1] = max(dp[i-1][1][0] + prices[i], dp[i-1][0][1])
            dp[i][0][2] = max(dp[i-1][1][1] + prices[i], dp[i-1][0][2])
            # 持股, 未卖出
            dp[i][1][0] = max(dp[i-1][0][0] - prices[i], dp[i-1][1][0])
            dp[i][1][1] = max(dp[i-1][0][1] - prices[i], dp[i-1][1][1])

            dp[i][1][2] = float('-inf')

        return max(dp[length-1][0][1], dp[length-1][0][2], 0)


if __name__ == '__main__':

    prices = [1, 2, 3, 4, 5]
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.maxProfit(prices)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)

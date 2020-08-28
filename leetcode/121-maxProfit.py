'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-28 16:31:52
'''

# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

# 如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。

# 注意：你不能在买入股票前卖出股票。

#  

# 示例 1:

# 输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
#      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
# 示例 2:

# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:

    def maxProfit(self, prices) -> int:
        if not prices:
            return 0

        length = len(prices)
        leftMin = [0] * length
        leftMin[0] = prices[0]
        rightMax = [0] * length
        rightMax[-1] = prices[-1]
        for left in range(1, length):
            right = length - left - 1
            if prices[left] < leftMin[left - 1]:
                leftMin[left] = prices[left]
            else:
                leftMin[left] = leftMin[left - 1]

            if prices[right] > rightMax[right + 1]:
                rightMax[right] = prices[right]
            else:
                rightMax[right] = rightMax[right + 1]

        max_price = 0
        for i in range(length):
            if rightMax[i] - leftMin[i] > max_price:
                max_price = rightMax[i] - leftMin[i]

        return max_price

    def maxProfit1(self, prices) -> int:
        inf = int(1e9)
        minprice = inf
        maxprofit = 0
        for price in prices:
            maxprofit = max(price - minprice, maxprofit)
            minprice = min(price, minprice)
        return maxprofit


if __name__ == '__main__':

    prices = [7, 1, 5, 3, 6, 4]
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.maxProfit1(prices)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)

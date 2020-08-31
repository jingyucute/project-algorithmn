'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-31 15:02:15
'''

# 老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。

# 你需要按照以下要求，帮助老师给这些孩子分发糖果：

# 每个孩子至少分配到 1 个糖果。
# 相邻的孩子中，评分高的孩子必须获得更多的糖果。
# 那么这样下来，老师至少需要准备多少颗糖果呢？

# 示例 1:

# 输入: [1,0,2]
# 输出: 5
# 解释: 你可以分别给这三个孩子分发 2、1、2 颗糖果。
# 示例 2:

# 输入: [1,2,2]
# 输出: 4
# 解释: 你可以分别给这三个孩子分发 1、2、1 颗糖果。
#      第三个孩子只得到 1 颗糖果，这已满足上述两个条件。

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:

    # 暴力算法
    def candy1(self, ratings) -> int:
        length = len(ratings)
        if length == 0:
            return 0
        candies = [1] * length
        flag = True
        while flag:
            flag = False
            for i in range(length):
                if i != length - 1 and ratings[i] > ratings[i + 1] and candies[i] <= candies[i + 1]:
                    candies[i] = candies[i + 1] + 1
                    flag = True
                if i > 0 and ratings[i] > ratings[i - 1] and candies[i] <= candies[i - 1]:
                    candies[i] = candies[i - 1] + 1
                    flag = True
        return sum(candies)

    def candy2(self, ratings) -> int:
        length = len(ratings)
        if length == 0:
            return 0

        l2r = [1] * length
        r2l = [1] * length
        for i in range(1, length):
            tl = i
            tr = length - i - 1
            if ratings[tl] > ratings[tl - 1]:
                l2r[tl] = l2r[tl - 1] + 1
            if ratings[tr] > ratings[tr + 1]:
                r2l[tr] = r2l[tr + 1] + 1

        sum = 0
        for i in range(length):
            sum += max(l2r[i], r2l[i])
        return sum

    def candy3(self, ratings) -> int:
        length = len(ratings)
        if length == 0:
            return 0

        candies = [1] * length
        for i in range(1, length):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        for i in range(length - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)


if __name__ == '__main__':

    ratings = [1, 2, 2]
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.candy3(ratings)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)

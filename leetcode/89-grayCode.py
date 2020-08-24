'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-25 00:12:01
'''

# 格雷编码是一个二进制数字系统，在该系统中，两个连续的数值仅有一个位数的差异。

# 给定一个代表编码总位数的非负整数 n，打印其格雷编码序列。即使有多个不同答案，你也只需要返回其中一种。

# 格雷编码序列必须以 0 开头。

#  

# 示例 1:

# 输入: 2
# 输出: [0,1,3,2]
# 解释:
# 00 - 0
# 01 - 1
# 11 - 3
# 10 - 2

# 对于给定的 n，其格雷编码序列并不唯一。
# 例如，[0,2,3,1] 也是一个有效的格雷编码序列。

# 00 - 0
# 10 - 2
# 11 - 3
# 01 - 1
# 示例 2:

# 输入: 0
# 输出: [0]
# 解释: 我们定义格雷编码序列必须以 0 开头。
#      给定编码总位数为 n 的格雷编码序列，其长度为 2n。当 n = 0 时，长度为 20 = 1。
#      因此，当 n = 0 时，其格雷编码序列为 [0]。


#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    def grayCode(self, n: int):
        res, head = [0], 1
        for i in range(n):
            for j in range(len(res) - 1, -1, -1):
                res.append(head + res[j])
            head <<= 1
        return res

        # if n == 0: return [0]
        # codes = self.grayCode(n - 1)
        # return codes + [1 << (n - 1) | x for x in codes[::-1]]


if __name__ == '__main__':

    n = 3
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.grayCode(n)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)

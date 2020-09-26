'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-26 18:13:03
'''

# 给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。

# 示例:

# 输入: 13
# 输出: 6
# 解释: 数字 1 出现在以下数字中: 1, 10, 11, 12, 13 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/number-of-digit-one
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    # wocao, 超时了
    def countDigitOne(self, n: int) -> int:
        result = set()
        ans = 0
        for num in range(1, n + 1):
            temp = num
            while temp:
                mod = temp % 10
                temp = temp // 10
                if mod == 1:
                    ans += 1
                    if num not in set():
                        result.add(num)

        # print(result)
        return ans

    # 先粘的,没看懂
    def countDigitOne1(self, n: int) -> int:
        if n <= 0:
            return 0
        i = 1
        ans = 0
        while i <= n:
            ans += n // (10 * i) * i + max(min(n % (10*i)-i+1, i), 0)
            i *= 10
        return ans


if __name__ == '__main__':
    n = 13
    solution = Solution()
    start_time = datetime.datetime.now()
    result = solution.countDigitOne1(n)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)

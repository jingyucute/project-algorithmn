'''
Description: 
Author: jingyu
Date: 2020-08-10 11:43:25
LastEditors: Please set LastEditors
LastEditTime: 2020-08-10 15:10:24
'''

# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

# 示例 1:

# 输入: 121
# 输出: true
# 示例 2:

# 输入: -121
# 输出: false
# 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
# 示例 3:

# 输入: 10
# 输出: false
# 解释: 从右向左读, 为 01 。因此它不是一个回文数。

import datetime


class Solution:

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        s = str(x)
        length = len(s)
        flag = True
        for i in range(length // 2):
            if s[i] == s[length - i - 1]:
                continue
            else:
                flag = False

        return flag


if __name__ == '__main__':

    start_time = datetime.datetime.now()
    s = Solution()

    result = s.isPalindrome(121)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)

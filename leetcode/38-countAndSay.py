'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-19 16:58:39
'''

# 给定一个正整数 n（1 ≤ n ≤ 30），输出外观数列的第 n 项。

# 注意：整数序列中的每一项将表示为一个字符串。

# 「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。前五项如下：

# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 第一项是数字 1

# 描述前一项，这个数是 1 即 “一个 1 ”，记作 11

# 描述前一项，这个数是 11 即 “两个 1 ” ，记作 21

# 描述前一项，这个数是 21 即 “一个 2 一个 1 ” ，记作 1211

# 描述前一项，这个数是 1211 即 “一个 1 一个 2 两个 1 ” ，记作 111221

#  

# 示例 1:

# 输入: 1
# 输出: "1"
# 解释：这是一个基本样例。
# 示例 2:

# 输入: 4
# 输出: "1211"
# 解释：当 n = 3 时，序列是 "21"，其中我们有 "2" 和 "1" 两组，"2" 可以读作 "12"，也就是出现频次 = 1 而 值 = 2；类似 "1" 可以读作 "11"。所以答案是 "12" 和 "11" 组合在一起，也就是 "1211"。


#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime


class Solution:
    def countAndSay(self, n: int) -> str:
        if n < 1 or n > 30:
            return ''

        l = ['' for _ in range(n+1)]
        l[1] = '1'
        for i in range(2, n + 1):

            preNum = l[i-1]
            cur_ch = preNum[0]
            cur_num = 1
            cur_rs = ""
            for j in range(1, len(preNum)):
                if preNum[j] == cur_ch:
                    cur_num += 1
                else:
                    cur_rs += str(cur_num) + cur_ch
                    cur_ch = preNum[j]
                    cur_num = 1
            cur_rs += str(cur_num) + cur_ch
            l[i] = cur_rs

        return l[n]


if __name__ == '__main__':

    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.countAndSay(30)
    print(result)

    end_time = datetime.datetime.now()
    print(end_time-start_time)

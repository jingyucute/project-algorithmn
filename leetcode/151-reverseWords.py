'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-03 18:44:40
'''

# 给定一个字符串，逐个翻转字符串中的每个单词。

#  

# 示例 1：

# 输入: "the sky is blue"
# 输出: "blue is sky the"
# 示例 2：

# 输入: "  hello world!  "
# 输出: "world! hello"
# 解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
# 示例 3：

# 输入: "a good   example"
# 输出: "example good a"
# 解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
#  

# 说明：

# 无空格字符构成一个单词。
# 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
# 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
#  

# 进阶：

# 请选用 C 语言的用户尝试使用 O(1) 额外空间复杂度的原地解法。


#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    def reverseWords(self, s: str) -> str:
        if not s or not s.strip():
            return ''
        ss = s.strip()
        print(ss.split(" ")[::-1])
        sl = ss.split(" ")
        res = []
        for i in range(len(sl) - 1, -1, -1):
            if sl[i] == '':
                continue
            res.append(sl[i])
        result = " ".join(res)
        return result


if __name__ == '__main__':

    s = "a good   example"
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.reverseWords(s)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)

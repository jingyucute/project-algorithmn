'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-22 14:37:09
'''

# 验证给定的字符串是否可以解释为十进制数字。

# 例如:

# "0" => true
# " 0.1 " => true
# "abc" => false
# "1 a" => false
# "2e10" => true
# " -90e3   " => true
# " 1e" => false
# "e3" => false
# " 6e-1" => true
# " 99e2.5 " => false
# "53.5e93" => true
# " --6 " => false
# "-+3" => false
# "95a54e53" => false

# 说明: 我们有意将问题陈述地比较模糊。在实现代码之前，你应当事先思考所有可能的情况。这里给出一份可能存在于有效十进制数字中的字符列表：

# 数字 0-9
# 指数 - "e"
# 正/负号 - "+"/"-"
# 小数点 - "."
# 当然，在输入中，这些字符的上下文也很重要。

#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime


class Solution:
    # 这个是别人给的答案， 但是感觉不是太妥 比如 '52.' 被认为 True
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        nums = [str(i) for i in range(10)]
        n = len(s)

        e_show_up, dot_show_up, num_show_up = False, False, False
        for i in range(n):
            c = s[i]
            if c in nums:
                num_show_up = True
            elif c in ('+', '-'):
                if i > 0 and s[i - 1] != 'e':
                    return False
            elif c == 'e':
                # 出现过
                if e_show_up or not num_show_up:
                    return False
                e_show_up = True
                num_show_up = False  # e 后面的数没有出现过
            elif c == '.':
                if dot_show_up or e_show_up:
                    return False
                dot_show_up = True
            else:
                return False
        return num_show_up


if __name__ == '__main__':
    s = "53."
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.isNumber(s)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)

'''
Description:
Author: jingyu
Date: 2020-08-10 11:43:25
LastEditors: Please set LastEditors
LastEditTime: 2020-08-14 01:04:40
'''

# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

# 有效字符串需满足：

# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。

# 示例 1:

# 输入: "()"
# 输出: true
# 示例 2:

# 输入: "()[]{}"
# 输出: true
# 示例 3:

# 输入: "(]"
# 输出: false
# 示例 4:

# 输入: "([)]"
# 输出: false
# 示例 5:

# 输入: "{[]}"
# 输出: true

import datetime


class Solution:

    def isValid(self, s: str) -> bool:
        flag = True
        if len(s) % 2 == 1:
            return False
        d = {
            ")": "(",
            "]": "[",
            '}': "{"
        }
        list = []
        for letter in s:
            if letter in d:
                if len(list) == 0:
                    flag = False
                    break

                pre = list.pop(-1)
                if d[letter] != pre:
                    flag = False
                    break
            else:
                list.append(letter)

        if len(list) != 0:
            flag = False

        return flag

    #  看看官方写的和自己的区别
    def isValid1(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = list()
        for ch in s:
            if ch in pairs:
                # 在这里就写的很精髓， 多看看吧
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)

        return not stack


if __name__ == '__main__':

    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.isValid("((")
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)

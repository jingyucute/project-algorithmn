'''
Description: 
Author: jingyu
Date: 2020-08-10 11:43:25
LastEditors: Please set LastEditors
LastEditTime: 2020-08-10 16:48:14
'''
# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

# '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
# 所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

# 说明:

# s 可能为空，且只包含从 a-z 的小写字母。
# p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
# 示例 1:

# 输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。
# 示例 2:

# 输入:
# s = "aa"
# p = "a*"
# 输出: true
# 解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
# 示例 3:

# 输入:
# s = "ab"
# p = ".*"
# 输出: true
# 解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
# 示例 4:

# 输入:
# s = "aab"
# p = "c*a*b"
# 输出: true
# 解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
# 示例 5:

# 输入:
# s = "mississippi"
# p = "mis*is*p*."
# 输出: false


import datetime


class Solution:

    # 动态规划
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        if not s and len(p) == 1:
            return False
        if len(p) > 1 and p[0] == "*":
            return False

        len1, len2 = len(s), len(p)
        list = [[False] * (len2 + 1) for i in range(len1+1)]
        # list[i][j] 表示 s中的前i个字符 和 p中的前j个字符能否匹配
        # list[len1][len2] 就是我们最后要求的结果
        list[0][0] = True

        def checkMatch(i, j):
            if i == 0:
                return False
            if p[j-1] == '.':
                return True
            return s[i - 1] == p[j - 1]

        for i in range(0, len1 + 1):
            for j in range(1, len2 + 1):
                # print("--", i, '--', j, '--', s[0:i], '-', p[0:j])
                if p[j - 1] == "*":
                    # 可能有相同重复字符匹配
                    # 相当于把*号和前面的一个字符去掉， 然后就是其默认的， 如果匹配， 则这个也匹配
                    list[i][j] = list[i][j - 2]
                    if checkMatch(i, j - 1):
                        if list[i-1][j]:
                            list[i][j] = list[i - 1][j]
                else:
                    # 都是对应字符匹配
                    if checkMatch(i, j):
                        list[i][j] = list[i-1][j-1]

        # print(list, list[len1][len2])

        return list[len1][len2]


if __name__ == '__main__':

    s = "mississippi"
    p = "mis*is*p*."

    s = "aab"
    p = "c*a*b"
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.isMatch(s, p)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)

'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-10-03 10:11:50
'''

""" 给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。

这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。

示例1:

输入: pattern = "abba", str = "dog cat cat dog"
输出: true
示例 2:

输入:pattern = "abba", str = "dog cat cat fish"
输出: false
示例 3:

输入: pattern = "aaaa", str = "dog cat cat dog"
输出: false
示例 4:

输入: pattern = "abba", str = "dog dog dog dog"
输出: false
说明:
你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-pattern
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。 """




import datetime
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        n = len(pattern)
        ls = s.split(" ")
        if len(ls) != n:
            return False
        d = {

        }
        for i in range(n):
            if pattern[i] not in d:
                if ls[i] not in d.values():
                    d[pattern[i]] = ls[i]
                else:
                    return False
            else:
                if d[pattern[i]] != ls[i]:
                    return False
        return True


if __name__ == '__main__':
    pattern = "abba"
    s = "dog cat cat fish"
    solution = Solution()
    start_time = datetime.datetime.now()
    result = solution.wordPattern(pattern, s)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)

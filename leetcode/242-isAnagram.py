'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-10-01 01:06:59
'''

# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

# 示例 1:

# 输入: s = "anagram", t = "nagaram"
# 输出: true
# 示例 2:

# 输入: s = "rat", t = "car"
# 输出: false
# 说明:
# 你可以假设字符串只包含小写字母。

# 进阶:
# 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/valid-anagram
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

import datetime


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        import collections
        ds = collections.Counter(s)
        dt = collections.Counter(t)

        for k, v in dt.items():
            if k not in ds:
                return False
            if ds[k] != v:
                return False
        return True


if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    solution = Solution()
    start_time = datetime.datetime.now()
    result = solution.isAnagram(s, t)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)

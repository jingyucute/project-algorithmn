'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-10-01 23:15:39
'''

""" 你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。

假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。

你可以通过调用 bool isBadVersion(version) 接口来判断版本号 version 是否在单元测试中出错。实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。

示例:

给定 n = 5，并且 version = 4 是第一个错误的版本。

调用 isBadVersion(3) -> false
调用 isBadVersion(5) -> true
调用 isBadVersion(4) -> true

所以，4 是第一个错误的版本。 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/first-bad-version
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。 """




import datetime
class Solution:

    def isBadVersion(self, version):
        if version == 4:
            return True
        return False

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        for i in range(1, n + 1):
            if self.isBadVersion(i):
                return i
        return n

    def firstBadVersion1(self, n):
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if self.isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        print(left, right)
        return left


if __name__ == '__main__':
    n = 7
    solution = Solution()
    start_time = datetime.datetime.now()
    result = solution.firstBadVersion1(n)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)

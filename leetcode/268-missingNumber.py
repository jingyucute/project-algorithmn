'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-10-01 10:16:43
'''
""" 给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。

 

示例 1:

输入: [3,0,1]
输出: 2
示例 2:

输入: [9,6,4,2,3,5,7,0,1]
输出: 8
 

说明:
你的算法应具有线性时间复杂度。你能否仅使用额外常数空间来实现?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/missing-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。 """




import datetime
class Solution:
    # 不考虑时间复杂度， 首先考虑的是排序 O(nlgn)
    def missingNumber(self, nums) -> int:
        nums.sort()
        misNum = 0
        for n in nums:
            if n != misNum:
                return misNum
            misNum += 1
        return misNum

    def missingNumber1(self, nums) -> int:
        ns = set(nums)
        n = len(nums) + 1

        for i in range(n):
            if i not in ns:
                return i


if __name__ == '__main__':
    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    solution = Solution()
    start_time = datetime.datetime.now()
    result = solution.missingNumber1(nums)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)

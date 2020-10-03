'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-10-03 08:39:36
'''

""" 给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

示例 1:

输入: [1,3,4,2,2]
输出: 2
示例 2:

输入: [3,1,3,4,2]
输出: 3
说明：

不能更改原数组（假设数组是只读的）。
只能使用额外的 O(1) 的空间。
时间复杂度小于 O(n2) 。
数组中只有一个重复的数字，但它可能不止重复出现一次

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-the-duplicate-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。 """




import datetime
class Solution:
    # 不考虑其他的
    def findDuplicate(self, nums) -> int:
        se = set()
        for num in nums:
            if num not in se:
                se.add(num)
            else:
                return num
        return 0

    def findDuplicate1(self, nums) -> int:
        slow, fast = 0, 0

        # 开始寻找环
        while True:
            slow, fast = nums[slow], nums[nums[fast]]
            # 可能在环中的某个点相遇
            if slow == fast:
                break
        # 寻找环的入口
        slow = 0
        while True:
            slow, fast = nums[slow], nums[fast]
            if slow == fast:
                return slow
        return 0


if __name__ == '__main__':
    nums = [1, 3, 4, 2, 2]
    solution = Solution()
    start_time = datetime.datetime.now()
    result = solution.findDuplicate(nums)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)

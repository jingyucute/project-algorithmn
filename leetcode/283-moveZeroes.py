'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-10-02 21:47:27
'''

""" 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/move-zeroes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。 """




import datetime
class Solution:

    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """

        length = len(nums)

        zindex = -1

        for i in range(length):

            if nums[i] == 0:
                if zindex < 0:
                    zindex = i
            else:
                if zindex >= 0:
                    nums[zindex] = nums[i]
                    nums[i] = 0
                    zindex += 1


if __name__ == '__main__':
    nums = [1]
    solution = Solution()
    start_time = datetime.datetime.now()
    solution.moveZeroes(nums)
    print(nums)
    end_time = datetime.datetime.now()
    print(end_time-start_time)

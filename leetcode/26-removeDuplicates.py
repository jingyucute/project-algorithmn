'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-15 07:45:24
'''

# 给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

# 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

#  

# 示例 1:

# 给定数组 nums = [1,1,2],

# 函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。

# 你不需要考虑数组中超出新长度后面的元素。
# 示例 2:

# 给定 nums = [0,0,1,1,1,2,2,3,3,4],

# 函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。

# 你不需要考虑数组中超出新长度后面的元素。
#  

# 说明:

# 为什么返回数值是整数，但输出的答案是数组呢?

# 请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

# 你可以想象内部操作如下:

# // nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
# int len = removeDuplicates(nums);

# // 在函数里修改输入数组对于调用者是可见的。
# // 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
# for (int i = 0; i < len; i++) {
#     print(nums[i]);
# }


#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime


class Solution:
    def removeDuplicates(self, nums) -> int:
        # 只需要一个变量指定上一个不重复的数字的下标， 如果循环的变量和那个位置的数字不等
        # 做相应的移动处理, 应该算是双指针
        length = len(nums)
        if length <= 1:
            return length

        cur_pos = 0
        for i in range(1, length):
            if nums[i] == nums[cur_pos]:
                continue
            else:
                cur_pos += 1
                nums[cur_pos] = nums[i]
        return cur_pos + 1


if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    # nums = []
    start_time = datetime.datetime.now()
    solution = Solution()
    length = solution.removeDuplicates(nums)
    print(nums)
    for i in range(length):
        print(nums[i])
    end_time = datetime.datetime.now()
    print(end_time-start_time)

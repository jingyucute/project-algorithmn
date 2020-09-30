'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-10-01 01:43:12
'''

""" 给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。

示例 :

输入: [1,2,1,3,2,5]
输出: [3,5]
注意：

结果输出的顺序并不重要，对于上面的例子， [5, 3] 也是正确答案。
你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/single-number-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。 """




import datetime
class Solution:
    def singleNumber(self, nums):
        data = set()
        for num in nums:
            if num not in data:
                data.add(num)
            else:
                data.remove(num)

        return list(data)


if __name__ == '__main__':
    nums = [1, 2, 1, 3, 2, 5]
    solution = Solution()
    start_time = datetime.datetime.now()
    result = solution.singleNumber(nums)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)

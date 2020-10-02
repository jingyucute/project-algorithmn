'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-10-02 21:57:20
'''

""" 给定一个迭代器类的接口，接口包含两个方法： next() 和 hasNext()。设计并实现一个支持 peek() 操作的顶端迭代器 -- 其本质就是把原本应由 next() 方法返回的元素 peek() 出来。

示例:

假设迭代器被初始化为列表 [1,2,3]。

调用 next() 返回 1，得到列表中的第一个元素。
现在调用 peek() 返回 2，下一个元素。在此之后调用 next() 仍然返回 2。
最后一次调用 next() 返回 3，末尾元素。在此之后调用 hasNext() 应该返回 false。
进阶：你将如何拓展你的设计？使之变得通用化，从而适应所有的类型，而不只是整数型？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/peeking-iterator
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。 """

# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """

#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """

#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """




import datetime
class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.list = []
        while iterator.hasNext():
            self.list.append(iterator.next())
        self.cur = 0

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.list[self.cur]

    def next(self):
        """
        :rtype: int
        """
        self.cur += 1
        return self.list[self.cur - 1]

    def hasNext(self):
        """
        :rtype: bool
        """
        return not self.cur == len(self.list)


if __name__ == '__main__':
    # nums = [1]
    # solution = Solution()
    start_time = datetime.datetime.now()
    # solution.moveZeroes(nums)
    # print(nums)
    end_time = datetime.datetime.now()
    print(end_time-start_time)

'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-10-03 11:06:35
'''

""" 中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。

例如，

[2,3,4] 的中位数是 3

[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：

void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。
示例：

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
进阶:

如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-median-from-data-stream
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。 """




import datetime
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list = []
        self.length = 0

    def addNum(self, num: int) -> None:
        if self.length == 0:
            self.list.append(num)
        else:
            left, right = 0,  self.length - 1
            while left <= right:
                mid = (left + right) // 2
                if self.list[mid] == num:
                    left = mid
                    break
                elif self.list[mid] < num:
                    left = mid + 1
                else:
                    right = mid - 1
            self.list.insert(left, num)
        self.length += 1

    def findMedian(self) -> float:
        print(self.list)
        if self.length % 2 == 0:
            left = (self.length - 1) // 2
            right = left + 1
            return (self.list[left] + self.list[right]) / 2

        else:
            return self.list[self.length // 2]


if __name__ == '__main__':

    medianFinder = MedianFinder()
    medianFinder.addNum(1)
    medianFinder.addNum(2)
    print(medianFinder.findMedian())
    medianFinder.addNum(3)
    print(medianFinder.findMedian())
    start_time = datetime.datetime.now()
    end_time = datetime.datetime.now()
    print(end_time-start_time)

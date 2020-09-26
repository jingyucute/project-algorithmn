'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-26 09:22:08
'''

# 城市的天际线是从远处观看该城市中所有建筑物形成的轮廓的外部轮廓。现在，假设您获得了城市风光照片（图A）上显示的所有建筑物的位置和高度，请编写一个程序以输出由这些建筑物形成的天际线（图B）。


# 每个建筑物的几何信息用三元组 [Li，Ri，Hi] 表示，其中 Li 和 Ri 分别是第 i 座建筑物左右边缘的 x 坐标，Hi 是其高度。可以保证 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX 和 Ri - Li > 0。您可以假设所有建筑物都是在绝对平坦且高度为 0 的表面上的完美矩形。

# 例如，图A中所有建筑物的尺寸记录为：[ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] 。

# 输出是以 [ [x1,y1], [x2, y2], [x3, y3], ... ] 格式的“关键点”（图B中的红点）的列表，它们唯一地定义了天际线。关键点是水平线段的左端点。请注意，最右侧建筑物的最后一个关键点仅用于标记天际线的终点，并始终为零高度。此外，任何两个相邻建筑物之间的地面都应被视为天际线轮廓的一部分。

# 例如，图B中的天际线应该表示为：[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ]。

# 说明:

# 任何输入列表中的建筑物数量保证在 [0, 10000] 范围内。
# 输入列表已经按左 x 坐标 Li  进行升序排列。
# 输出列表必须按 x 位排序。
# 输出天际线中不得有连续的相同高度的水平线。例如 [...[2 3], [4 5], [7 5], [11 5], [12 7]...] 是不正确的答案；三条高度为 5 的线应该在最终输出中合并为一个：[...[2 3], [4 5], [12 7], ...]

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    # 有点难
    def getSkyline(self, buildings):
        n = len(buildings)

        if n == 0:
            return []
        if n == 1:
            x_start, x_end, y = buildings[0]
            return [[x_start, y], [x_end, 0]]

        left = self.getSkyline(buildings[:n//2])
        right = self.getSkyline(buildings[n//2:])

        merge = self.mergeSkylines(left, right)

        return merge

    def mergeSkylines(self, left, right):
        output = []
        nL, nR = len(left), len(right)
        pl, pr = 0, 0
        leftY, rightY, currY = 0, 0, 0

        def update_output(x, y):
            if not output or output[-1][0] != x:
                output.append([x, y])
            else:
                output[-1][1] = y

        def append_skyline(p, lst, n, y, currY):
            while p < n:
                x, y = lst[p]
                p += 1
                if currY != y:
                    update_output(x, y)
                    currY = y

        while pl < nL and pr < nR:
            pointL, pointR = left[pl], right[pr]
            if pointL[0] < pointR[0]:
                x, leftY = pointL
                pl += 1
            else:
                x, rightY = pointR
                pr += 1

            maxY = max(leftY, rightY)
            if currY != maxY:
                update_output(x, maxY)
                currY = maxY

        append_skyline(pl, left, nL, leftY, currY)

        append_skyline(pr, right, nR, rightY, currY)

        return output


if __name__ == '__main__':

    buildings = [
        [2, 9, 10],
        [3, 7, 15],
        [5, 12, 12],
        [15, 20, 10],
        [19, 24, 8]
    ]
    solution = Solution()
    start_time = datetime.datetime.now()
    result = solution.getSkyline(buildings)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)

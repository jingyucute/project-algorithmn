'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-10-01 16:38:52
'''

""" 给定一位研究者论文被引用次数的数组（被引用次数是非负整数）。编写一个方法，计算出研究者的 h 指数。

h 指数的定义：h 代表“高引用次数”（high citations），一名科研人员的 h 指数是指他（她）的 （N 篇论文中）总共有 h 篇论文分别被引用了至少 h 次。（其余的 N - h 篇论文每篇被引用次数 不超过 h 次。）

例如：某人的 h 指数是 20，这表示他已发表的论文中，每篇被引用了至少 20 次的论文总共有 20 篇。

 

示例：

输入：citations = [3,0,6,1,5]
输出：3 
解释：给定数组表示研究者总共有 5 篇论文，每篇论文相应的被引用了 3, 0, 6, 1, 5 次。
     由于研究者有 3 篇论文每篇 至少 被引用了 3 次，其余两篇论文每篇被引用 不多于 3 次，所以她的 h 指数是 3。
 

提示：如果 h 有多种可能的值，h 指数是其中最大的那个。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/h-index
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。 """




import datetime
class Solution:
    def hIndex(self, citations):
        if not citations:
            return 0
        citations.sort(reverse=True)
        length = len(citations)
        import collections
        dh = collections.defaultdict(int)

        for c in citations:
            c = min(c, length)
            for i in range(c, -1, -1):
                if i not in dh:
                    dh[i] = 1
                else:
                    dh[i] += 1
        # print(dh)
        h = 0
        for k, v in dh.items():
            if k <= v:
                h = k
                break
        return h

    def hIndex1(self, citations):
        length = len(citations)
        papers = [0] * (length + 1)
        for c in citations:
            papers[min(length, c)] += 1
        k = length
        s = papers[length]
        while k > s:
            k -= 1
            s += papers[k]
        return k


if __name__ == '__main__':
    citations = [1, 1]
    solution = Solution()
    start_time = datetime.datetime.now()
    result = solution.hIndex(citations)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)

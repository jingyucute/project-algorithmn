'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-22 17:39:52
'''

# 给定一个单词数组和一个长度 maxWidth，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。

# 你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。

# 要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。

# 文本的最后一行应为左对齐，且单词之间不插入额外的空格。

# 说明:

# 单词是指由非空格字符组成的字符序列。
# 每个单词的长度大于 0，小于等于 maxWidth。
# 输入单词数组 words 至少包含一个单词。
# 示例:

# 输入:
# words = ["This", "is", "an", "example", "of", "text", "justification."]
# maxWidth = 16
# 输出:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
# 示例 2:

# 输入:
# words = ["What","must","be","acknowledgment","shall","be"]
# maxWidth = 16
# 输出:
# [
#   "What   must   be",
#   "acknowledgment  ",
#   "shall be        "
# ]
# 解释: 注意最后一行的格式应为 "shall be    " 而不是 "shall     be",
#      因为最后一行应为左对齐，而不是左右两端对齐。
#      第二行同样为左对齐，这是因为这行只包含一个单词。
# 示例 3:

# 输入:
# words = ["Science","is","what","we","understand","well","enough","to","explain",
#          "to","a","computer.","Art","is","everything","else","we","do"]
# maxWidth = 20
# 输出:
# [
#   "Science  is  what we",
#   "understand      well",
#   "enough to explain to",
#   "a  computer.  Art is",
#   "everything  else  we",
#   "do                  "
# ]

#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime


class Solution:
    def fullJustify(self, words, maxWidth: int):
        result = []
        unit_list = []
        unit_len = 0
        for word in words:
            cur_len = len(word)
            min_space = len(unit_list)
            if unit_len + min_space + cur_len <= maxWidth:
                unit_list.append(word)
                unit_len += cur_len
            else:
                # 这里 unit_list 处理形式
                word_count = len(unit_list) - 1
                space_count = maxWidth - unit_len
                ans = unit_list[0]
                if word_count == 0:
                    avg_space = space_count
                    for _ in range(avg_space):
                        ans += " "
                else:
                    avg_space = space_count // word_count
                    space_list = [avg_space] * word_count
                    for i in range(space_count % word_count):
                        space_list[i] += 1
                    for i in range(1, len(unit_list)):
                        for _ in range(space_list[i - 1]):
                            ans += " "
                        ans += unit_list[i]
                result.append(ans)

                unit_list = []
                unit_list.append(word)
                unit_len = cur_len

        if unit_list:
            word_count = len(unit_list) - 1
            space_list = [1] * word_count
            space_count = maxWidth - unit_len - word_count
            space_list.append(space_count)

            ans = ""
            for i in range(len(unit_list)):
                ans += unit_list[i]
                for _ in range(space_list[i]):
                    ans += " "
            result.append(ans)

        return result


if __name__ == '__main__':
    # [4, 2, 2, 7, 2, 4, 14]
    words = ["ask", "not", "what", "your", "country", "can", "do", "for",
             "you", "ask", "what", "you", "can", "do", "for", "your", "country"]
    maxWidth = 16
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.fullJustify(words, maxWidth)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)

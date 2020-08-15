'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-15 17:01:55
'''
# 给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。

# 注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

#  

# 示例 1：

# 输入：
#   s = "barfoothefoobarman",
#   words = ["foo","bar"]
# 输出：[0,9]
# 解释：
# 从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
# 输出的顺序不重要, [9,0] 也是有效答案。
# 示例 2：

# 输入：
#   s = "wordgoodgoodgoodbestword",
#   words = ["word","good","best","word"]
# 输出：[]

#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime

# 先粘过来， 这个没太看懂


class Solution:
    #
    def findSubstring(self, s: str, words):
        from collections import Counter
        lens = len(s)
        lenlist = len(words)
        if lens == 0 or lenlist == 0:
            return []
        lenw = len(words[0])
        words = Counter(words)
        result = []

        for i in range(lens - lenlist * lenw + 1):
            t_list = []
            for j in range(lenlist):
                if s[i+j*lenw: i+(j+1)*lenw] in words:
                    t_list.append(s[i+j*lenw: i+(j+1)*lenw])

            t_list = Counter(t_list)
            if t_list == words:
                result.append(i)

        return result

    # 这里尝试一下回溯法
    # 效率有点低 O(n!) , 还是看看别的方法吧
    def findSubstring1(self, s: str, words):
        lens = len(s)
        lenlist = len(words)
        if lens == 0 or lenlist == 0:
            return []
        result = []

        def backtrack(index, s, words, maybe, result):
            if index > lenlist:
                ts = ''.join(maybe)
                ls = len(s)
                lm = len(ts)
                for i in range(ls - lm + 1):
                    if s[i:i+lm] == ts and i not in result:
                        result.append(i)

            else:
                cur_word = words[index - 1]

                for i in range(len(maybe)):
                    temp = maybe.copy()
                    maybe.insert(i, cur_word)
                    backtrack(index+1, s, words, maybe, result)
                    maybe = temp.copy()
                temp = maybe.copy()
                maybe.append(cur_word)
                backtrack(index+1, s, words, maybe,  result)
                maybe = temp.copy()

        backtrack(1, s, words, [], result)
        return result


if __name__ == '__main__':
    s = "wordgoodgoodgoodbestword"
    words = ["word", "good", "best", "word"]
    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    s = "wordgoodgoodgoodbestword"
    words = ["word", "good", "best", "good"]
    s = "pjzkrkevzztxductzzxmxsvwjkxpvukmfjywwetvfnujhweiybwvvsrfequzkhossmootkmyxgjgfordrpapjuunmqnxxdrqrfgkrsjqbszgiqlcfnrpjlcwdrvbumtotzylshdvccdmsqoadfrpsvnwpizlwszrtyclhgilklydbmfhuywotjmktnwrfvizvnmfvvqfiokkdprznnnjycttprkxpuykhmpchiksyucbmtabiqkisgbhxngmhezrrqvayfsxauampdpxtafniiwfvdufhtwajrbkxtjzqjnfocdhekumttuqwovfjrgulhekcpjszyynadxhnttgmnxkduqmmyhzfnjhducesctufqbumxbamalqudeibljgbspeotkgvddcwgxidaiqcvgwykhbysjzlzfbupkqunuqtraxrlptivshhbihtsigtpipguhbhctcvubnhqipncyxfjebdnjyetnlnvmuxhzsdahkrscewabejifmxombiamxvauuitoltyymsarqcuuoezcbqpdaprxmsrickwpgwpsoplhugbikbkotzrtqkscekkgwjycfnvwfgdzogjzjvpcvixnsqsxacfwndzvrwrycwxrcismdhqapoojegggkocyrdtkzmiekhxoppctytvphjynrhtcvxcobxbcjjivtfjiwmduhzjokkbctweqtigwfhzorjlkpuuliaipbtfldinyetoybvugevwvhhhweejogrghllsouipabfafcxnhukcbtmxzshoyyufjhzadhrelweszbfgwpkzlwxkogyogutscvuhcllphshivnoteztpxsaoaacgxyaztuixhunrowzljqfqrahosheukhahhbiaxqzfmmwcjxountkevsvpbzjnilwpoermxrtlfroqoclexxisrdhvfsindffslyekrzwzqkpeocilatftymodgztjgybtyheqgcpwogdcjlnlesefgvimwbxcbzvaibspdjnrpqtyeilkcspknyylbwndvkffmzuriilxagyerjptbgeqgebiaqnvdubrtxibhvakcyotkfonmseszhczapxdlauexehhaireihxsplgdgmxfvaevrbadbwjbdrkfbbjjkgcztkcbwagtcnrtqryuqixtzhaakjlurnumzyovawrcjiwabuwretmdamfkxrgqgcdgbrdbnugzecbgyxxdqmisaqcyjkqrntxqmdrczxbebemcblftxplafnyoxqimkhcykwamvdsxjezkpgdpvopddptdfbprjustquhlazkjfluxrzopqdstulybnqvyknrchbphcarknnhhovweaqawdyxsqsqahkepluypwrzjegqtdoxfgzdkydeoxvrfhxusrujnmjzqrrlxglcmkiykldbiasnhrjbjekystzilrwkzhontwmehrfsrzfaqrbbxncphbzuuxeteshyrveamjsfiaharkcqxefghgceeixkdgkuboupxnwhnfigpkwnqdvzlydpidcljmflbccarbiegsmweklwngvygbqpescpeichmfidgsjmkvkofvkuehsmkkbocgejoiqcnafvuokelwuqsgkyoekaroptuvekfvmtxtqshcwsztkrzwrpabqrrhnlerxjojemcxel"
    words = ["dhvf", "sind", "ffsl", "yekr", "zwzq", "kpeo", "cila", "tfty", "modg",
             "ztjg", "ybty", "heqg", "cpwo", "gdcj", "lnle", "sefg", "vimw", "bxcb"]
    start_time = datetime.datetime.now()
    solution = Solution()
    # result = solution.findSubstring(s, words)
    # print(result)

    result1 = solution.findSubstring1(s, words)
    print(result1)
    # words1 = ["word", "good", "best", "good"]
    # temp = words1
    # words1.insert(1, "1234")
    # print(temp)
    # words2 = ["good", "word", "best", "good"]
    # print(words1.sort() == words2.sort())
    end_time = datetime.datetime.now()
    print(end_time-start_time)

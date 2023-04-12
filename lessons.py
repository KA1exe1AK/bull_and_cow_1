# class Solution:
#     def acceptable_value(self, x: int) -> bool:
#         if x > 2147483647 or x < -2147483648:
#             return False
#         return True
#     def reverse(self, x: int) -> int:
#         s = Solution()
#         if x == 0:
#             return 0
#         if x > 0:
#             while x % 10 == 0:
#                 x //= 10
#             x = int(str(x)[::-1])
#             return x if (s.acceptable_value(x) == True) else 0
#         if x < 0:
#             x = int(str(x * (-1))[::-1]) * (-1)
#             return x if (s.acceptable_value(x) == True) else 0
# a = Solution()
# print(a.reverse(-1534236469))

from itertools import combinations
import itertools


# d = {2: ["a", "b", "c"], 3: ["d", "e", "f"], 4: ["g", "h", "i"], 5: ["j", "k", "l"], 6: ["m", "n", "o"],
#      7: ["p", "q", "r", "s"], 8: ["t", "u", "v"], 9: ["w", "x", "y", "z"]}
# print("".join(d[2]+d[3]))

# class Solution:
#     def letterCombinations(self, digits: str) -> list[str]:
#         a = []
#         ans=[]
#         d = {2: ["a", "b", "c"], 3: ["d", "e", "f"], 4: ["g", "h", "i"], 5: ["j", "k", "l"], 6: ["m", "n", "o"],
#              7: ["p", "q", "r", "s"], 8: ["t", "u", "v"], 9: ["w", "x", "y", "z"]}
#         for i in digits:
#             a.append( "".join(d[int(i)]) )
#         print(a)
#         for i in range(len(a)-1):
#             for j in range(len(a[i])):
#                 for z in range(len(a[i+1])):
#                     print(z)
#                     ans.append(str(a[i][j])+str(a[i][z]))
#                     print(ans)
#         # a = "".join(["".join(d[int(i)]) for i in digits])
#         # print(a,type(a))
#         # ans = list(combinations(a,2))
#         # print(ans)
#         return []
#
#
# a = Solution()
# print(a.letterCombinations("23"))

from urllib.request import urlopen
import numpy as np

filename = "https://stepik.org/media/attachments/lesson/16462/boston_houses.csv"
f = urlopen(filename)
data = np.loadtxt(f, skiprows=0)
print(data.mean(axis=0))
# x_shape = np.array([[1, 2], [3, 4]])
# a = np.mean(f,axis=0)
# print(f)
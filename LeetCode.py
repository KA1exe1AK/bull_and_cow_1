# def i_arr(n: list) -> list:
#     ans = []
#     if len(n) < 2:
#         return n
#     if len(n) == 2:
#         return sorted(i ^ 2 for i in n)
#     if len(n) % 2 == 0:
#         l = len(n) // 2 - 1
#         r = len(n) // 2
#     else:
#         l = len(n) // 2 - 1
#         r = len(n) // 2 + 1
#         ans.append(n[len(n) // 2])
#     # print(l,r)
#     while l >= 0 and r <= len(n)-2:
#         if abs(n[l]) > abs(n[r]):
#             print(l, r, "l")
#             ans.append(n[l] ** 2)
#             l -= 1
#         if abs(n[l]) < abs(n[r]):
#             print(l, r,"r")
#             ans.append(n[r] ** 2)
#             r += 1
#
#         if abs(n[l]) == abs(n[r]):
#             print(l, r,"both")
#             ans.append(n[r] ** 2)
#             ans.append(n[l]** 2)
#             r += 1
#             l -= 1
#         # print(n[l],n[r])
#     return ans
#
#
# n = [-8, -2, 0, 5, 7]
# print(i_arr(n))
from collections import defaultdict


# def maxProfit(prices: list[int]) -> int:
#     profit = 0
#     for i in range(len(prices) - 1):
#
#         if prices[i] < prices[i + 1]:
#             profit += (prices[i + 1] - prices[i])
#
#     return profit
#
#
# print(maxProfit([7, 1, 5, 3, 6, 4]))

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# def jump(nums: list[int]) -> int:
#     x = [nums[i] + i for i in range(len(nums))]
#     print(nums)
#     print(x)
#     l, r, jumps = 0, 0, 0
#     while r < len(nums) - 1:
#         jumps += 1
#         print(l, r, "  ", x[l:r + 1])
#         l, r = r + 1, max(x[l:r + 1])
#     return jumps
#
# print(jump([2, 5, 1, 3, 1, 2, 0, 5, 3, 0, 0, 4, 3, 2, 1]))

# def rotate(nums: list, k: int)->None:
#     k = k % len(nums)
#     curr = nums[len(nums)-k:] + nums[:len(nums)-k]
#     for i in range(len(nums)):
#         nums[i] = curr[i]
#
# rotate(nums := [1,2,3,4,5,6,7], k = 20)
# print(nums)

# 7 статей больше или равно 7 цитат
# def Hindex(citations: list) -> int:
#     l = 0
#     r = len(citations)
#     cnt = 0
#     while l <= r:
#         mid = (l + r) // 2
#         for i in citations:
#             if i >= mid:
#                 cnt += 1
#         if cnt <= mid:
#             r = mid - 1
#         else:
#             l = mid + 1
#         cnt = 0
#     return l - 1
# print(Hindex(citations = [1,2,1]))


# for i in range(len(nums)-2, -1,-1):
#     print(nums[i] + i)
#     c = i
#     while c != 0:
#         if nums[c] + c == len(nums) - 1:
#             ...
#     # print(nums[i], nums[i] + len(nums) - i)
#     # print(i)
#     #     print(nums[i])
# return False
def merge(nums1: list[int], m: int, nums2: list[int], n: int):
    i = m - 1
    j = n - 1
    k = m + n - 1

    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    print(nums1)
    
merge(nums1 = [1,2,3,4,5,6,7,0,0,0], m = 3, nums2 = [4,5,6], n = 3)
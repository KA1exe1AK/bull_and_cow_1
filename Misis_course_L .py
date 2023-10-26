count = int(input())
d = dict()
for i in range(count):
    print(d)
    l, m = input().split()
    if l not in d:
        d[l] = []
    if m not in d:
        d[m] = []
    d[l].append(m)
    d[m].append(l)

print("Введите слово")
word_to_find = input()
print(d[word_to_find])
# ----------------------------
from string import ascii_letters
ltrs = ascii_letters
s1 = set(input())
s2 = set(input())
print(set(ltrs) - s1 - s2)
# ----------------------------

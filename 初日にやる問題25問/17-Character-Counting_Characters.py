# 17-Character-Counting_Characters.py

# 文字のカウント
# 与えられた英文に含まれる、各アルファベットの数を数えるプログラムを作成して下さい。 
# なお、小文字と大文字は区別しません。

# Input
# 複数の行にまたがる１つの英文が与えられます。
# Output
# 与えられた英文に含まれる各アルファベットの数を以下に示す形式で出力して下さい：

# a : aの個数
# b : bの個数
# c : cの個数
#   .
#   .
# z : zの個数
# Constraints
# 英文が含む文字の数 < 1200
# Sample Input
# This is a pen.
# Sample Output
# a : 1
# b : 0
# c : 0
# d : 0
# e : 1
# f : 0
# g : 0
# h : 1
# i : 2
# j : 0
# k : 0
# l : 0
# m : 0
# n : 1
# o : 0
# p : 1
# q : 0
# r : 0
# s : 2
# t : 1
# u : 0
# v : 0
# w : 0
# x : 0
# y : 0
# z : 0

import sys
 
s = str()
alphabet = "abcdefghijklmnopqrstuvwxyz"
 
for line in sys.stdin:
    s += line.lower()
    # print(list(s))

 
for c in alphabet:
    print("{} : {}".format(c, s.count(c)) )
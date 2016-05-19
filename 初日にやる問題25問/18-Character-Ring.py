# 18-Character-Ring.py

# リング
# 図のようなリング状の文字列 s の任意の位置から、時計回りに連続した文字をいくつか選んで、
# 文字列 p が作れるかを判定するプログラムを作成してください。

# Input
# １行目に文字列 s が与えられます。
# ２行目に文字列 p が与えられます。

# Output
# p が作れる場合は Yes と、作れない場合は No と１行に出力してください。

# Constraints
# 1≤pの長さ≤sの長さ≤100
# 文字列は英小文字からなる

# Sample Input 1
# vanceknowledgetoad
# advance
# Sample Output 1
# Yes

# Sample Input 2
# vanceknowledgetoad
# advanced
# Sample Output 2
# No

import re

pattern=[]

s=input()
p=input()

s= s+s

# for p2 in list(p):
# 	pattern.append(p2)
# 	pattern.append(".*")

# pattern = "".join(pattern)
# print(pattern)

matchOB = re.search(p, s)

if matchOB:
	print("Yes")
else:
	print("No")
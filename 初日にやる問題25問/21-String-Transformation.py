# 21-String-Transformation.py

# 文字列変換
# 文字列 str に対して、与えられた命令の列を実行するプログラムを作成してください。
# 命令は以下の操作のいずれかです：

# print a b: str の a 文字目から b 文字目までを出力する。
# reverse a b: str の a 文字目から b 文字目までを逆順にする。
# replace a b p: str の a 文字目から b 文字目までを p に置き換える。
# ここでは、文字列 str の最初の文字を 0 文字目とします。

# Input
# 1 行目に文字列 str が与えられます。str は英小文字のみ含みます。
# 2 行目に命令の数 q が与えられます。続く q 行に各命令が上記の形式で与えられます。

# Output
# 各 print 命令ごとに文字列を１行に出力してください。

# Constraints
# 1≤strの長さ≤1000
# 1≤q≤100
# 0≤a≤b<strの長さ
# replace 命令では b−a+1=pの長さ

# Sample Input 1
# abcde
# 3
# replace 1 3 xyz
# reverse 0 2
# print 1 4
# Sample Output 1
# xaze

# Sample Input 2
# xyz
# 3
# print 0 2
# replace 0 2 abc
# print 0 2
# Sample Output 2
# xyz
# abc

#入力

str = input()
op_num = int( input() )
for i in range(op_num):
	op = input().split()
	a = int(op[1])
	b = int(op[2])
	if op[0]=="replace":
		# str = str.replace(str[ a:b+1 ], op[3])
		str = str[0:a] + op[3] + str[b+1:]
	elif op[0]=="reverse":
		# str = str.replace(str[a:b+1], str[ b-len(str) : a-len(str)-1 : -1 ] )
		str = str[:a] + str[a:b+1][::-1] + str[b+1:]
	# elif op[0]=="print":
	else:
		print(str[a:b+1])

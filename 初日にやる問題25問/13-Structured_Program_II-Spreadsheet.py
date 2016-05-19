# 13-Structured_Program_II-Spreadsheet.py

# 表計算
# 表計算を行う簡単なプログラムを作成します。
# 表の行数rと列数c、r × c の要素を持つ表を読み込んで、
# 各行と列の合計を挿入した新しい表を出力するプログラムを作成して下さい。

# Input
# 最初の行にrとcが空白区切りで与えられます。
# 続くr行にそれぞれc個の整数が空白区切りで与えられます。

# Output
# (r+1) × (c+1) の新しい表を出力して下さい。
# 各行の隣り合う整数は１つの空白で区切って下さい。各行の最後の列としてその行の合計値を、各列の最後の行としてその列の合計値を、最後の行・列に表全体の合計値を挿入して下さい。

# Constraints
# 1 ≤ r, c ≤ 100
# 0 ≤ 要素 ≤ 100
# Sample Input
# 4 5
# 1 1 3 4 5
# 2 2 2 4 5
# 3 3 0 1 1
# 2 3 4 4 6
# Sample Output
# 1 1 3 4 5 14
# 2 2 2 4 5 15
# 3 3 0 1 1 8
# 2 3 4 4 6 19
# 8 9 9 13 17 56

# ↓ Aizuでnumpy 使えなかったお
#---------------------------------------------------------------
# import numpy as np

# r,c = map( int,input().split() )

# data = np.zeros((r,c))

# for i in range(r):
# 	data[i] = np.array( input().split() )

# data=data.astype("int")
# print("data",data)

# for i in range( r ):
# 	for j in range(c):
# 		print("{0} ".format(data[i][j]), end="")
# 	print( np.sum(data[i]) )

# for j in range(c):
# 	print("{0} ".format( np.sum(data, axis=0)[j] ), end="" )

# print( np.sum(data) )
#---------------------------------------------------------------


r,c = map( int,input().split() )

data = []
csum = [0]*c

for i in range(r):
	data.append(  list(map( int,input().split() ))  )

for i in range( r ):
	for j in range(c):
		print("{0} ".format(data[i][j]), end="")
		csum[j] +=data[i][j]
	print( sum(data[i]) )

for j in range(c):
	print("{0} ".format( csum[j] ), end="" )

print( sum(csum) )

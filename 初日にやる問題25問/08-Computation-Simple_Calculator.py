# -*- coding: utf-8 -*-
# 08-Computation-Simple_Calculator.py

# 計算機
# ２つの整数 a, b と１つの演算子 op を読み込んで、a op b を計算するプログラムを作成して下さい。
# ただし、演算子 op は、"+"(和)、"-"(差)、"*"(積)、"/"(商)、のみとし、割り算で割り切れない場合は、小数点以下を切り捨てたものを計算結果とします。

# Input
# 入力は複数のデータセットから構成されています。各データセットの形式は以下のとおりです：
# a op b
# op が '?' のとき 入力の終わりを示します。このケースの出力は行ってはいけません。
# Output
# 各データセットについて、計算結果を１行に出力して下さい。

# Constraints
# 0 ≤ a, b ≤ 20000
# 0 による割り算が与えられることはありません。
# Sample Input
# 1 + 2
# 56 - 18
# 13 * 2
# 100 / 10
# 27 + 81
# 0 ? 0
# Sample Output
# 3
# 38
# 26
# 10
# 108

import sys

output = []


while 1:
	a,op,b = input().split()
	a= int(a)
	b= int(b)

	if op=="+":
		output.append(a+b)
	elif op =="-":
		output.append(a-b)
	elif op =="*":
		output.append(a*b)
	elif op =="/":
		output.append( int(a/b) )
	elif op =="?":
		break;
	else:
		sys.exit()

for i in range( len(output)):
	print(output[i])
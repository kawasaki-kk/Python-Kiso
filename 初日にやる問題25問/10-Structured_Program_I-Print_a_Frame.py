# 10-Structured_Program_I-Print_a_Frame.py

# フレームの描画
# 以下のような、たてH cm よこ W cm の枠を描くプログラムを作成して下さい。
# ##########
# #........#
# #........#
# #........#
# #........#
# ##########
# 上図は、たて 6 cm よこ 10 cm の枠を表しています。

# Input
# 入力は複数のデータセットから構成されています。各データセットの形式は以下のとおりです：
# H W
# H, W がともに 0 のとき、入力の終わりとします。
# 審判データに用いられる入力の条件は、3 ≤ H, W ≤ 100 です。

# Output
# 各データセットについて、たて H cm よこ W cm の枠を出力して下さい。
# 各データセットの後に、１つの空行を入れて下さい。

# Constraints
# H, W ≤ 300

# Sample Input
# 3 4
# 5 6
# 3 3
# 0 0
# Sample Output
# ####
# #..#
# ####

# ######
# #....#
# #....#
# #....#
# ######

# ###
# #.#
# ###


# a = []
# a = [ *map(int,input().split() ) ]
H=[]
W=[]

while 1:
	temp = input().split()
	H.append( int(temp[0]) )
	W.append( int(temp[1]) )
	if H[-1]==0 and W[-1]==0:
		break;

for i in range( len(H) ):
	for j in range( H[i] ):
		#行の記述開始
		if j==0 or j==H[i]-1: 		#最初の行または最後の行
			for k in range( W[i] ):
				print("#",end="")
		else:
			print("#",end="")
			for k in range(W[i]-2):
				print(".",end="")
			print("#",end="")

		print("")
		#行の記述おわり

	if i !=len(H)-1:
		print("")
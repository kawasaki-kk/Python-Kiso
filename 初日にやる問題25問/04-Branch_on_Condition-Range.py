# 04-Branch_on_Condition-Range.py

# 範囲
# ３つの整数a, b, cを読み込み、それらが a < b < cの条件を満たすならば"Yes"を、満たさないならば"No"を出力するプログラムを作成して下さい。

# Input
# ３つの整数が空白で区切られて与えられます。
# Output
# YesまたはNoを１行に出力して下さい。

# Sample Input 1
# 1 3 8
# Sample Output 1
# Yes
# Sample Input 2
# 3 8 1
# Sample Output 2
# No

# print("a,b,cを入力。")
a,b,c=map(int,input().split())
# print("a=%d, b=%d, c=%d."%(a,b,c))

if a<b and b<c:
	print("Yes")
else:
	print("No")


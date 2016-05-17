# 07-Repetitive_Processing-How_Many_Divisors.py

# 約数の数
# ３つの整数 aa、bb、cc を読み込み、aa から bb までの整数の中に、cc の約数がいくつあるかを求めるプログラムを作成してください。

# Input
# aa、bb、cc が１つの空白区切りで１行に与えられます。
# Output
# 約数の数を１行に出力してください。

# Constraints
# 1≤a,b,c≤10000
# a≤b
# Sample Input
# 5 14 80
# Sample Output
# 3

aa,bb,cc = map(int,input().split())
count=0

for i in range(bb-aa+1):
	if cc%(aa+i)==0:
		count+=1

print(count)
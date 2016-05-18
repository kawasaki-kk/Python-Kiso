# 09-Computation-Min_Max_and_Sum.py

# 最小値、最大値、合計値
# n 個の整数 ai(i=1,2,...n)を入力し、それらの最小値、最大値、合計値を求めるプログラムを作成してください。

# Input
# １行目に整数の数 n が与えられます。２行目に n 個の整数 ai が空白区切りで与えられます。
# Output
# 最小値、最大値、合計値を空白区切りで１行に出力してください。

# Constraints
# 0<n≤10000
# −1000000≤ai≤1000000
# Sample Input
# 5
# 10 1 5 4 17
# Sample Output
# 1 17 37

num_min = 1000001
num_max = -1000001
num_sum = 0
num = int(input())

# a = []
# a = [ *map(int,input().split() ) ]
a = input().split()

for i in range(num):
	a[i]=int(a[i])
	if a[i]<num_min:
		num_min = a[i]

	if a[i]>num_max:
		num_max = a[i]

	num_sum+=a[i]

print("{0} {1} {2}".format(num_min,num_max,num_sum) );
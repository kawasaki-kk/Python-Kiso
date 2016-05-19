# 14-Structured_Program_II-Matrix_Multiplication.py

# 行列の積

# n×mの行列 AA と m×lの行列 B を入力し、それらの積である n×l の行列 C を出力する
# プログラムを作成してください。
# 行列 C の各要素 cij は次の式で得られます：

# cij=∑{k=1,m}aik bkj
# ここで、A、B、C の各要素をそれぞれ aij、bij、cij とします。

# Input
# １行目に n、m、l が空白区切りで与えられます。
# 続く行に n×m の行列 A と m×l の行列 B が与えられます。

# Output
# n×l の行列 C の要素 cij を出力してください。
# 各行の隣り合う要素を１つの空白で区切ってください。

# Constraints
# 1≤n,m,l≤100
# 0≤aij,bij≤10000
# Sample Input
# 3 2 3
# 1 2
# 0 3
# 4 5
# 1 2 1
# 0 3 2
# Sample Output
# 1 8 5
# 0 9 6
# 4 23 14

n,m,l = map( int,input().split() )
# print(n,m,l)


a = []
b = []
c=[[0 for i in range(l)] for j in range(n)]

for i in range(n):
	a.append(  list(map( int,input().split() ))  )
for i in range(m):
	b.append(  list(map( int,input().split() ))  )


for i in range(n):
	# print("i:{0}".format(i))
	for j in range(l):
		# print("j:{0}".format(j))
		for k in range(m):
			c[i][j] += a[i][k]*b[k][j]


for i in range(n):
	for j in range(l):
		if j==l-1:
			print("{0}".format(c[i][j]))
		else:
			print("{0} ".format(c[i][j]), end="")

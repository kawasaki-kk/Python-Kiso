# 12-Structured_Program_II-How_many_ways.py

# 組み合わせの数
# 1 から n までの数の中から、重複無しで３つの数を選びそれらの合計が x となる
# 組み合わせの数を求めるプログラムを作成して下さい。
# 例えば、1 から 5 までの数から３つを選んでそれらの合計が 9 となる組み合わせは、

# 1 + 3 + 5 = 9
# 2 + 3 + 4 = 9
# の２通りがあります。

# Input
# 複数のデータセットが入力として与えられます。
# 各データセットでは、空白で区切られた n、x が 1 行に与えられます。

# n、x がともに 0 のとき入力の終わりとします。
# n は 3 以上 100　以下とします。

# Output
# 各データセットについて、組み合わせの数を１行に出力して下さい。

# Sample Input
# 5 9
# 0 0
# Sample Output
# 2

result = []
n=[]
x=[]

while 1:
	temp = input().split() 
	if temp[0]=="0" and temp[1]=="0":
		break;
	else:
		n.append( int( temp[0] ))
		x.append( int( temp[1] ))

for i in range( len(n) ):
	count =0
	for n1 in range(1,n[i]+1-2):
		for n2 in range(n1+1, n[i]+1-1):
			for n3 in range(n2+1, n[i]+1):
				sum = n1+n2+n3
				if sum == x[i]:
					count+=1
	result.append(count)

for i in range( len(result) ):
	print(result[i])

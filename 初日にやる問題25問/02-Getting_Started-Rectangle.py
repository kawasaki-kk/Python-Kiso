# 02-Getting_Started-Rectangle.py

# 長方形の面積と周の長さ
# たて a cm よこ b cm の長方形の面積と周の長さを求めるプログラムを作成して下さい。

# Input
# a と b が１つの空白で区切られて与えられます。
# Output
# 面積と周の長さを１つの空白で区切って１行に出力して下さい。

# Sample Input
# 3 5
# Sample Output
# 15 16

# print("aとbを入力。")
a,b=map(int,input().split())
# print("a=%d, b=%d."%(a,b))

# print("面積は%f ."%(a*b));
# print("周の長さは%f ."%(2*a+2*b));
print("{0} {1}".format(a*b, 2*a+2*b));
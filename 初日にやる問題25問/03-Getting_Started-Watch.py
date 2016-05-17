# 03-Getting_Started-Watch.py

# 時計
# 秒単位の時間 SS が与えられるので、hh:mm:ss の形式へ変換して出力してください。
# ここで、hh は時間、mm は 60 未満の分、ss は 60 未満の秒とします。

# Input
# SS が１行に与えられます。
# Output
# hh、mm、ss を :（コロン）区切りで１行に出力してください。数値が１桁の場合、0 を付けて２桁表示をする必要はありません。

# Constraints
# 0≤S<86400
# Sample Input
# 46979
# Sample Output
# 13:2:59

# print("ssを入力。")
x=int(input())
# print("ss=%d."%x)

# hhを計算
hh=int(x/3600)
hh_remain = x%3600

#mmを計算
mm=int(hh_remain/60)
mm_remain = hh_remain%60

#ssを計算
ss=mm_remain

print ("{0}:{1}:{2}".format(hh,mm,ss));

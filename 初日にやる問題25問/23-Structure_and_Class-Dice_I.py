# 23-Structure_and_Class-Dice_I.py

# サイコロ I
# 次の展開図から得られるサイコロを転がすシミュレーションを行うプログラムを作成してください。

# サイコロの各面には図のとおりに 1 から 6 のラベルが割りあてられています。
# 入力としてサイコロの各面のラベルに対応する数字と、転がす命令の列が与えられるので、
# サイコロの上面の数字を出力してください。
# シミュレーションの初期状態は、図のとおりのラベルの位置でサイコロが置かれているものとします。

# Input
# １行目に各面の数字が、図に示すラベルの順番に空白区切りで与えられます。

# ２行目に命令を表す１つの文字列が与えられます。命令はそれぞれ図に示す４方向を表す文字 E、N、S、W を含む文字列です。

# Output
# すべての命令を実行した後のサイコロの上面の数を１行に出力してください。

# Constraints
# 0≤0≤ 入力されるサイコロの面の数字 ≤100≤100
# 0≤0≤ 命令を表す文字列の長さ ≤100≤100
# Note
# 続くシリーズ Dice III, Dice IV では、複数のサイコロを扱うので、サイコロをクラスや構造体で作成しておきましょう。

# Sample Input 1
# 1 2 4 8 16 32
# SE
# Sample Output 1
# 8
# 各面に 1, 2, 4, 8, 16, 32 と書かれたサイコロを S の方向に転がした後、E の方向に転がすと、上面の数字が 8 になります。



# Sample Input 2
# 1 2 4 8 16 32
# EESWN
# Sample Output 2
# 32

#------------------------------------------------------------------------------------------
# class Dice:
# 	def __init__(self, dice_num):
# 		self.side_top=1
# 		self.side_bot=6
# 		self.side_Nor=5
# 		self.side_Eas=3
# 		self.side_Sau=2
# 		self.side_Wes=4
# 		self.dice_num = dice_num

# 	def op_N(self):
# 		self.side_top, self.side_bot, self.side_Nor, self.side_Sau =\
# 		self.side_Sau, self.side_Nor, self.side_top, self.side_bot

# 	def op_E(self):
# 		self.side_top, self.side_bot, self.side_Eas, self.side_Wes =\
# 		self.side_Wes, self.side_Eas, self.side_top, self.side_bot

# 	def op_S(self):
# 		self.side_top, self.side_bot, self.side_Nor, self.side_Sau =\
# 		self.side_Nor, self.side_Sau, self.side_bot, self.side_top

# 	def op_W(self):
# 		self.side_top, self.side_bot, self.side_Eas, self.side_Wes =\
# 		self.side_Eas, self.side_Wes, self.side_bot, self.side_top

# 	def print_side_top(self):
# 		print( dice_num[self.side_top-1] )

# 	def print_side_all(self):
# 		print( "top:{}, bot:{}, Nor:{}, Eas{}, Sau:{}, Wes,{}.".format(self.side_top, self.side_bot, self.side_Nor, self.side_Eas, self.side_Sau, self.side_Wes ) )


# dice_num = list( map(int, input().split()))

# dice_roll = Dice(dice_num) 
# for i in input():
# 	if i == "N":
# 		dice_roll.op_N()
# 	elif i =="E":
# 		dice_roll.op_E()
# 	elif i =="S":
# 		dice_roll.op_S()
# 	elif i =="W":
# 		dice_roll.op_W()
# 	else:
# 		print("あばば")

# dice_roll.print_side_top()

#------------------------------------------------------------------------------------------

class Dice:
	def __init__(self, dice_num):	  # 1    2    3    4    5    6
		self.dice_state=[1,6,5,3,2,4] #[top, bot, nor, eas, sau, wes]
		self.dice_num = dice_num

	def op_N(self):
		self.dice_state = [ self.dice_state[i-1] for i in [5,3,1,4,2,6] ]

	def op_E(self):
		self.dice_state = [ self.dice_state[i-1] for i in [6,4,3,1,5,2] ]

	def op_S(self):
		self.dice_state = [ self.dice_state[i-1] for i in [3,5,2,4,1,6] ]

	def op_W(self):
		self.dice_state = [ self.dice_state[i-1] for i in [4,6,3,2,5,1] ]

	def get_state_top(self):
		# print("dice_roll.get_state_top", self.dice_state[0])
		return self.dice_state[0]

	def get_num_top(self):
		return self.dice_num[self.dice_state[0]-1]

	def print_side_top(self):
		print( self.dice_num[self.dice_state[0]-1] )

	def print_side_all(self):
		print( "top:{}, bot:{}, Nor:{}, Eas{}, Sau:{}, Wes,{}.".format(self.side_top, self.side_bot, self.side_Nor, self.side_Eas, self.side_Sau, self.side_Wes ) )


dice_num = list( map(int, input().split()))

dice_roll = Dice(dice_num) 

Func_set = {'N': dice_roll.op_N, 'W': dice_roll.op_W, 'E': dice_roll.op_E, 'S': dice_roll.op_S}

for i in input():
	Func_set[i]()

dice_roll.print_side_top()

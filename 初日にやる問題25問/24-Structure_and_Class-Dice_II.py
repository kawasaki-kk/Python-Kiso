# 24-Structure_and_Class-Dice_II.py

# サイコロ II
# Dice I と同様の方法で、入力された数字の列からサイコロをつくります。
# このサイコロを Dice I の方法で回転させた後の上面と前面の数字が
# 質問として与えられるので、右側の面の数字を答えるプログラムを作成してください。

# Input
# １行目に各面の数字が、ラベルの順番に空白区切りで与えられます。
# ２行目に質問の数 qq が与えられます。
# 続く qq 行に質問が与えられます。各質問では上面と前面の数字を表す２つの整数が空白区切りで１行に与えられます。

# Output
# 各質問ごとに、サイコロの右側の面の数字を１行に出力してください。
	
# Constraints
# 0≤0≤ 入力されるサイコロの面の数字 ≤100≤100
# 入力されるサイコロの面の数字はすべて異なる
# 1≤q≤241≤q≤24

# Sample Input
# 1 2 3 4 5 6
# 3
# 6 5
# 1 3
# 3 2
# Sample Output
# 3
# 5
# 6

class Dice:
	def __init__(self, dice_num):	  # 1    2    3    4    5    6
		self.dice_state=[1,6,5,3,2,4] #[top, bot, nor, eas, sau, wes]
		self.dice_num = dice_num

	def reset_dice(self):
		self.dice_state=[1,6,5,3,2,4] #[top, bot, nor, eas, sau, wes]

	def op_N(self):
		self.dice_state = [ self.dice_state[i-1] for i in [5,3,1,4,2,6] ]

	def op_E(self):
		self.dice_state = [ self.dice_state[i-1] for i in [6,4,3,1,5,2] ]

	def op_S(self):
		self.dice_state = [ self.dice_state[i-1] for i in [3,5,2,4,1,6] ]

	def op_W(self):
		self.dice_state = [ self.dice_state[i-1] for i in [4,6,3,2,5,1] ]

	def op_twist(self):
		self.dice_state = []

	def get_state_top(self):
		return self.dice_state[0]
	def get_state_bottom(self):
		return self.dice_state[1]
	def get_state_nor(self):
		return self.dice_state[2]
	def get_state_eas(self):
		return self.dice_state[3]
	def get_state_sau(self):
		return self.dice_state[4]
	def get_state_wes(self):
		return self.dice_state[5]


	def get_num_top(self):
		return self.dice_num[self.dice_state[0]-1]

	def print_side_top(self):
		print( self.dice_num[self.dice_state[0]-1] )

	def print_side_all(self):
		print( "top:{}, bot:{}, Nor:{}, Eas{}, Sau:{}, Wes,{}.".format(self.side_top, self.side_bot, self.side_Nor, self.side_Eas, self.side_Sau, self.side_Wes ) )




dice_roll = Dice(  list( map(int, input().split()))  ) 
Func_set = {'N': dice_roll.op_N, 'W': dice_roll.op_W, 'E': dice_roll.op_E, 'S': dice_roll.op_S}

for i in range( int(input()) ):
	dice_roll.reset_dice()
	top, south = map(int,input().split())

	for j in "NNNEEE":
		if dice_roll.get_state_top() == top:
			print("top break.", dice_roll.get_state_top())
			break;
		Func_set[j]()
	print("top", dice_roll.get_state_top())
	
	Func_set["N"]()

	for j in "EEEEE":
		# print("dice_roll.get_state_top", dice_roll.get_state_top())
		if dice_roll.get_state_top() == south:
			print("south break.", dice_roll.get_state_top())
			break;
		Func_set[j]()
	print("south", dice_roll.get_state_top())
	
	Func_set["W"]()

	print( dice_roll.get_num_top() )

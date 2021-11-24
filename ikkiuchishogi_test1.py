import yaml
import os

os.makedirs('./result_kifu',exist_ok=True)

class ShogiCls:
	def __init__(self):
		self.shogi_bit = list()
		# 初期設定＝盤上に王と玉を置く。
		for i in range(81):
			if i == 4:   
				self.shogi_bit.append('玉')
			elif i == 76:
				self.shogi_bit.append('王')
			else:
				self.shogi_bit.append('・')

		with open('config.yml', 'r') as yml:
			config = yaml.safe_load(yml)
 
		#手番。対局開始時は先手。        
		self.tebann = config['sennte']


	# 駒を動かす位置を入力して指定。
	def shogi_inputXY(self,zahyou:int):
		while True:
			myXY = input(zahyou)
			if myXY == "":
				continue
			if myXY.isdigit() and (1 <= int(myXY) <= 9): 
				return int(myXY)
			print("1から9までの整数を1つ入力して下さい。")
   

	# 盤面を表示する。
	def shogi_display(self):
		print("Ｘ１ ２ ３ ４ ５ ６ ７ ８ ９")
		for l in range(1,10):
			print("{}".format(l), end='' )
			for c in range(1,10):
				print(" {}".format(self.shogi_bit[(l-1)*9+(c-1)]), end='')
			print()


	# 手番表示。
	def shogi_yourturn(self):
		if self.tebann == '王':
			print("先手の手番です。")
		else:
			print("後手の手番です。")   
			

if __name__ == '__main__':

	taikyoku = ShogiCls()

	# 盤面表示。
	taikyoku.shogi_display()

	# 手番表示。
	taikyoku.shogi_yourturn()

	
	


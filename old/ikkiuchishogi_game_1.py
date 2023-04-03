import yaml
import os
import logging
from logging import getLogger, StreamHandler, Formatter

os.makedirs('./result_kifu',exist_ok=True)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ShogiCls:
    def __init__(self, tesuu=0) -> None:

        # 初期設定＝盤上に王と玉を置く。
        self.shogi_bit = list() 
        for i in range(81):
            if i == 4:   
                self.shogi_bit.append('玉')
            elif i == 76:
                self.shogi_bit.append('王')
            else:
                self.shogi_bit.append('・')
        self.tesuu = tesuu

        #手番。対局開始時は先手。 
        with open('config.yml','r',encoding="utf-8") as yml:
            config = yaml.safe_load(yml)       
        self.tebann = config['sennte']

    # 盤面を表示する。
    def shogi_display(self) -> None:
        print("Ｘ１ ２ ３ ４ ５ ６ ７ ８ ９")
        for l in range(1,10):
            print("{}".format(l), end='' )
            for c in range(1,10):
                print(" {}".format(self.shogi_bit[(l-1)*9+(c-1)]), end='')
            print()

    # 手番表示。
    def shogi_yourturn(self) -> None:
        if self.tebann == '王':
            logger.info("先手の手番です。")
        else:
            logger.info("後手の手番です。")   
    
    # 手番交換。
    def shogi_tebann_change(self) -> None:
        if self.tebann == '王':
            self.tebann = '玉'
        else:
            self.tebann = '王'

    # 駒を動かす位置を入力して指定。
    def shogi_inputXY(self)-> None:
        while True:
            if self.tebann == '王':
                for i in range(0,80):
                    if self.shogi_bit[i] == '王':
                        #現在の王の位置を記録。
                        self.ou = i
                        break
                    else:
                        i = i + 1
                #print(self.ou)        
                logger.info("先手の手番です。横方向の移動を指定するために1から9までの整数を1つ入力して下さい。")
                myXY = input()
                if myXY == "":
                    continue
                if myXY.isdigit(): 
                    x = int(myXY)-1
                    self.shogi_bit[self.ou] = '・'
                    self.shogi_bit[x + 9*int((self.ou)/9)] = '王'
                    taikyoku.shogi_display()
                for i in range(1,80):
                    if self.shogi_bit[i] == '王':
                        self.ou = i
                        break
                    else:
                        i = i + 1
                #print(self.ou)
                logger.info("縦横方向の移動を指定するために1から9までの整数を1つ入力して下さい。")
                myXY = input()
                if myXY == "":
                    continue
                if myXY.isdigit(): 
                    x = 9 * (int(myXY)-1) + self.ou  % 9
                    self.shogi_bit[self.ou] = '・'
                    self.shogi_bit[x] = '王'
                    #print(self.ou)
                    taikyoku.shogi_display()
                    taikyoku.shogi_tebann_change()
                    taikyoku.shogi_yourturn()
                    return int(myXY)
                    return True
            else:
                for i in range(1,80):
                    if self.shogi_bit[i] == '玉':
                        #現在の玉の位置を記録。
                        self.gyoku = i
                        break
                    else:
                        i = i + 1
                #print(self.gyoku)
                logger.info("後手の手番です。横方向の移動を指定するために1から9までの整数を1つ入力して下さい。")
                myXY = input()
                if myXY == "":
                    continue
                if myXY.isdigit(): 
                    x = int(myXY)-1
                    self.shogi_bit[self.gyoku] = '・'
                    self.shogi_bit[x+ 9*int((self.gyoku)/9)] = '玉'
                    taikyoku.shogi_display()
                for i in range(0,80):
                    if self.shogi_bit[i] == '玉':
                        self.gyoku = i
                        break
                    else:
                        i = i + 1
                #print(self.gyoku)
                logger.info("縦横方向の移動を指定するために1から9までの整数を1つ入力して下さい。")
                myXY = input()
                if myXY == "":
                    continue
                if myXY.isdigit(): 
                    x = 9 * (int(myXY)-1) + self.gyoku % 9
                    self.shogi_bit[self.gyoku] = '・'
                    self.shogi_bit[x] = '玉'
                    taikyoku.shogi_display()
                    taikyoku.shogi_tebann_change()
                    taikyoku.shogi_yourturn()
                    return int(myXY)
                    return True

    # 対局終了かどうか判定する。
    def shogi_checkendofgame(self):
        X = self.shogi_bit.count('王')
        Y = self.shogi_bit.count('玉')
        Z = X * Y
        if Z == 1:
            return -1
        else:
            if X != 1:
                print("対局終了です。後手の勝ちです。")
            else:
                print("対局終了です。先手の勝ちです。")
            return 1
        

if __name__ == '__main__':

    taikyoku = ShogiCls()

    # 盤面表示。
    taikyoku.shogi_display()

    # 手番表示。
    taikyoku.shogi_yourturn()

    # 対局終了までループ。
    while True:
        # 対局が終わったか判断する
        sts = taikyoku.shogi_checkendofgame()
        if sts == 1:
            break
        elif sts < 0:
            # どこに駒を移動させるか入力。
            taikyoku.shogi_inputXY()
        

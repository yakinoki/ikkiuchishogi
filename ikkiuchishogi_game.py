import yaml
import os
import logging
from logging import getLogger, StreamHandler, Formatter

os.makedirs('./result_kifu',exist_ok=True)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ShogiCls:
    def __init__(self) -> None:
        self.shogi_bit = list() 
        # 初期設定＝盤上に王と玉を置く。
        for i in range(81):
            if i == 4:   
                self.shogi_bit.append('玉')
            elif i == 76:
                self.shogi_bit.append('王')
            else:
                self.shogi_bit.append('・')

        with open('config.yml','r',encoding="utf-8") as yml:
            config = yaml.safe_load(yml)
 
        #手番。対局開始時は先手。        
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
            logger.info("1から9までの整数を1つ入力して下さい。")
            myXY = input()
            if myXY == "":
                continue
            if myXY.isdigit() and (6 <= int(myXY) <= 9): 
                x = int(myXY) + 71
                self.shogi_bit[x] = '王'
                self.shogi_bit[76] = '・'
                taikyoku.shogi_display()
                taikyoku.shogi_tebann_change()
                taikyoku.shogi_yourturn()
                return int(myXY)
                return True
            elif myXY.isdigit() and (1 <= int(myXY) <= 4):
                taikyoku.shogi_tebann_change()
                taikyoku.shogi_yourturn()
                return int(myXY)
                return True
            elif myXY.isdigit() and (int(myXY) == 5):
                taikyoku.shogi_tebann_change()
                taikyoku.shogi_yourturn()
                return int(myXY)
                return True

    # 合法手のリストの取得
    def legal_actions(self)->list:
        actions = []

        return actions
    
    # 負けかどうか
    def is_lose(self)-> None:
        if self.shogi_bit[25] == '玉':
            return False
        return True
        
    # 対局終了かどうか
    def is_tsumi(self)-> None:
        return self.is_lose() 

    # ランダムで行動選択
    def random_action(taikyoku):
        legal_actions = taikyoku.legal_actions()


if __name__ == '__main__':

    taikyoku = ShogiCls()

    # 盤面表示。
    taikyoku.shogi_display()

    # 手番表示。
    taikyoku.shogi_yourturn()

    while True:
        
        # 対局終了時
        if taikyoku.is_tsumi():
            # どこに駒を移動させるか入力。
            taikyoku.shogi_inputXY()
        

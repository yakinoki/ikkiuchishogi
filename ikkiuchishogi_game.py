import yaml
import os
import random
import logging
from logging import getLogger, StreamHandler, Formatter

os.makedirs('./result_kifu', exist_ok=True)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ShogiCls:
    def __init__(self, tesuu=0):
        self.shogi_bit = ["・"] * 81
        self.shogi_bit[4], self.shogi_bit[76] = "玉", "王"
        self.tesuu = tesuu
        self.ou, self.gyoku = 76, 4  # 玉と王の位置

        # 手番。対局開始時は先手。
        with open('config.yml', 'r', encoding="utf-8") as yml:
            config = yaml.safe_load(yml)
        self.tebann = config['sennte']

    # 盤面を表示する。
    def shogi_display(self):
        print("Ｘ１ ２ ３ ４ ５ ６ ７ ８ ９")
        for l in range(1, 10):
            print("{}".format(l), end="")
            print(" ".join(self.shogi_bit[(l - 1) * 9:l * 9]))

    # 手番表示。
    def shogi_yourturn(self):
        logger.info("{}の手番です。".format("先手" if self.tebann == "王" else "後手"))

    # 手番交換。
    def shogi_tebann_change(self):
        self.tebann = "玉" if self.tebann == "王" else "王"

    # 駒を動かす位置を入力して指定。その後相手がランダムで打ち返して来る。
    def shogi_inputXY(self) -> None:
        myXY = input()
        while True:
            if self.tebann == '王':
                for i in range(0, 80):
                    if self.shogi_bit[i] == '王':
                        # 現在の王の位置を記録。
                        self.ou = i
                        break
                    else:
                        i = i + 1
                logger.info("先手の手番です。横方向の移動を指定するために1から9までの整数を1つ入力して下さい。")
                myXY = input()
                if not myXY:
                    continue
                if myXY.isdigit():
                    x = int(myXY) - 1
                    self.shogi_bit[self.ou] = '・'
                    self.shogi_bit[x + 9 * int((self.ou) / 9)] = '王'
                    self.shogi_display()
                for i in range(1, 80):
                    if self.shogi_bit[i] == '王':
                        self.ou = i
                        break
                    else:
                        i = i + 1
                logger.info("縦方向の移動を指定するために1から9までの整数を1つ入力して下さい。")
                myXY = input()
                if not myXY:
                    continue
                if myXY.isdigit():
                    x = 9 * (int(myXY) - 1) + self.ou % 9
                    self.shogi_bit[self.ou] = '・'
                    self.shogi_bit[x] = '王'
                    self.shogi_display()
                    self.shogi_tebann_change()
                    self.shogi_yourturn()
                    return int(myXY)

            else:
                for i in range(1, 80):
                    if self.shogi_bit[i] == '玉':
                        # 現在の玉の位置を記録。
                        self.gyoku = i
                        break
                    else:
                        i = i + 1
                logger.info("後手の手番です。横方向の移動を指定するために1から9までの整数が1つ入力されます。")
                x = random.randint(1, 9)
                self.shogi_bit[self.gyoku] = '・'
                self.shogi_bit[x + 9 * int((self.gyoku) / 9)] = '玉'
                self.shogi_display()
                for i in range(1, 80):
                    if self.shogi_bit[i] == '玉':
                        self.gyoku = i
                        break
                    else:
                        i = i + 1
                logger.info("縦方向の移動を指定するために1から9までの整数が1つ入力されます。")
                x = random.randint(1, 9)
                self.shogi_bit[self.gyoku] = '・'
                self.shogi_bit[9 * (x - 1) + self.gyoku % 9] = '玉'
                self.shogi_display()
                self.shogi_tebann_change()
                self.shogi_yourturn()

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

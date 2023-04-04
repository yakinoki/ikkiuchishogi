from ikkiuchishogi_game import ShogiCls

if __name__ == '__main__':

    taikyoku = ShogiCls()

    # 盤面表示。
    taikyoku.shogi_display()
    # 手番表示。
    taikyoku.shogi_yourturn()
    
    # 対局終了までループ。
    while True:
        # 対局が終わったか判断する
        if taikyoku.shogi_checkendofgame() == 1:
            break
        else:
            # どこに駒を移動させるか入力。
            taikyoku.shogi_inputXY()
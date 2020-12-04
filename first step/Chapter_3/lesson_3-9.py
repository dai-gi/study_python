# 『 lesson３-９ プログラムにメモ書きするには？　プログラムを補足するコメントの書き方 』

# 【「#」以降はコメント】

# 【コメントの例】
# coding:utf-8

# 画面に文字を表示する
print("こんにちは。今日の晩ご飯は何でしたか？") # ６行目の表示
print("おいしかったですか？")
print("何カロリーでしたか？")

# エラーが出てうまくいかないときのチェックポイント
"""

・大文字と小文字の区別は正しいか
・全角文字で入力していないか
・行頭の空白の数は正しいか（指定していない限り、行頭に空白を入れない）
・括弧の対応は間違っていないか
・「’」シングルクォーテーション、「”」ダブルクォーテーションが間違っていないか
・文字コードは正しいか
・日本語を使っているとき、１行目か２行目に「# coding:utf-8」もしくは「# coding=utf-8」を記述したか
・ファイル名に日本語を使っていないか

"""
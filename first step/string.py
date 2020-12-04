# いちばんやさしいPython入門教室

"""
目次

・文字列
・文字列の連結
　−「+」は連結
　-「＊」は繰り返し
　- 文字列と数値は連結できない
・文字列方に変換
・改行
　- エスケープシーケンスを利用する
　-「三重クォート」を利用する
　- print関数内だけ改行をしたい場合

"""


# 文字列：P57
# 「"」と「'」の使い分けは自由
print("abc") # abc
print('abc') # abc

# NG例
print("abc') 
# 出力結果：SyntaxError: EOL while scanning string literal


# 文字列の連結：P61
# 「+」は連結
print("abc" + "cde") # abccde

# 「＊」は繰り返し
print("abc" * 3) # abcabcabc

# 文字列と数値は連結できない
print("abc" + 3) # TypeError: can only concatenate str (not "int") to str


# 文字列型に変換：P64
x = 3 
print(type(x)) # <class 'int'>
x_str = str(x)
print(type(x_str)) # <class 'str'>


# 改行：P69
# NG例：
print("こんにちは。今日の晩ご飯は何でしたか？
おいしかったですか？
何カロリーでしたか？
")
"""
出力結果：実行されない

"""

# エスケープシーケンスを利用する
print("こんにちは。今日の晩ご飯は何でしたか？\nおいしかったですか？\n何カロリーでしたか？")
"""
出力結果：こんにちは。今日の晩ご飯は何でしたか？
おいしかったですか？
何カロリーでしたか？
"""

# 「三重クォート」を利用する
print( """こんにちは。今日の晩ご飯は何でしたか？
おいしかったですか？
何カロリーでしたか？
""")
"""
出力結果：こんにちは。今日の晩ご飯は何でしたか？
おいしかったですか？
何カロリーでしたか？

"""

# print関数内だけ改行をしたい場合

# 「\」を利用する
print( "こんにちは。今日の晩ご飯は何でしたか？\
おいしかったですか？\
何カロリーでしたか？")
# 出力結果：こんにちは。今日の晩ご飯は何でしたか？おいしかったですか？何カロリーでしたか？

# 「end=""」を利用する
print("こんにちは。今日の晩ご飯は何でしたか？",end="")
print("おいしかったですか？",end="")
print("何カロリーでしたか？")  
# 出力結果：こんにちは。今日の晩ご飯は何でしたか？おいしかったですか？何カロリーでしたか？
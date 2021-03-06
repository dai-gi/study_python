# @IT｜[Python入門] リストの基本
# list関数(リストを定義)
strlist = list('Python') # ['P', 'y', 't', 'h', 'o', 'n']
print(strlist)
intlist = list(range(10)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(intlist)
somelist = list(intlist) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(somelist)

# リストに変換 
scores = {'network':60, 'database':80, 'security':60}
print(list(scores)) # ['network', 'database', 'security']
# ディクショナリの値をリスト化する
print(list(scores.values())) # [60, 80, 60]
print('-----------')

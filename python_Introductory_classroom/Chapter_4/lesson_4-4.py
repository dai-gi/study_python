# while構文
# coding:utf-8
total = 0
a = 1
while total <= 50:
    total = total + a
    a = a + 1
print(total)

# for構文と同じ処理ををwhileで記述する
# coding:utf-8
for a in range(1,5+1):
    print(a)

a = 1
while a <= 5:
    print(a)
    a = a + 1

for i in range( 1 , 5 + 1 ):
    print(i)
else:
    print("この処理を終了する")

# 繰り返しが終わったときに実行する else
a = "処理を繰り返す"
while True :
    print(a)
else:
    print("この処理を終了する")

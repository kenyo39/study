# coding:utf-8
import random as rnd
import re

#４文字のランダム数値を生成する（重複あり）
a = [rnd.randint(0,9),
     rnd.randint(0,9),
     rnd.randint(0,9),
     rnd.randint(0,9)]

print(str(a[0]) + str(a[1]) + str(a[2]) + str(a[3]))
while True:
#入力チェック
  isOK = False
  while isOK == False:
    b = input("４桁の数値を入力してください(0000-9999)")
    if not re.match(r"^\d\d\d\d$",b):
       print("４桁の数値ではありません")
    else:
       isOK = True

#ヒット数を数える
  hit = 0
  for i in range(4):
    if a[i] == int(b[i]):
       hit = hit + 1

  blow = 0
  for j in range(4):
    for i in range(4):
      if (int(b[i]) == a[i]) and (a[i] != int(b[i])) and (a[j] != int(b[j])):
        blow = blow + 1
        break

  print("ヒット" + str(hit))
  print("ブロー" + str(blow))

  if hit == 4:
    print("当たり")
    break
				

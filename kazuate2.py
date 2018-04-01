# coding:utf-8
import random as rnd
import re
import tkinter as tk
import tkinter.messagebox as tmsg

#ボタンがクリックされたら
def ButtonClick():
  b=editbox1.get()
  isOK=False
  if not re.match(r"^\d\d\d\d$",b):
    tmsg.showerror("エラー","４桁の数字を入力してください")
  else:
    isOK=True
  if isOK:
    hit = 0
    for i in range(4):
      if a[i] == int(b[i]):
        hit = hit + 1
    blow=0
    for j in range(4):
      for i in range(4):
        if (int(b[j]) == a[i]) and (a[i] != int(b[i])) and (a[j] != int(b[j])):
          blow = blow +1
          break
  if hit == 4:
    tmsg.showinfo("当たり","おめでとうございます。当たりです")
    root.destroy()
  else:
    rirekibox.insert(tk.END,b + "/H:" + str(hit) +"/B:" + str(blow) + "\n")

#メイン処理
    
#４文字のランダム数値を生成する
a=list(range(4))
c=[0,1,2,3,4,5,6,7,8,9]
rnd.shuffle(c)

for i in range(4):
  a[i]=c[i]

print(str(a[0]) + str(a[1]) + str(a[2]) + str(a[3]))


root = tk.Tk()

root.geometry("600x400")
root.title("数当てゲーム")

label1=tk.Label(root,text="数を入力してね",font=("Helvetica",14))
label1.place(x=20,y=20)

editbox1=tk.Entry(width=4,font=("Helvetica",28))
editbox1.place(x=120,y=60)

button1=tk.Button(root,text="チェック",font=("Helevetica",14),command=ButtonClick)
button1.place(x=220,y=60)

rirekibox=tk.Text(root,font=("Helvetica",14))
rirekibox.place(x=400,y=0,height=400)
root.mainloop()
	

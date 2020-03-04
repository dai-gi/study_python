# ランダムに1桁の整数を選ぶプログラム
# coding:utf-8

import random
import tkinter as tk
import tkinter.messagebox as tmsg
from functools import partial



class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        
        # ラベルを作成
        self.label1 = tk.Label(master, text="ボタン当ててね", font = ('Helvetica', 35))
        self.label1.place(x = 70, y = 15)

        # 履歴を表示
        self.rirekibox = tk.Text(master, font=("Helvetica", 14))
        self.rirekibox.place(x=255, y=75, width=90, height=200)

        self.bg = 'blue1'

        # ４つのボタン
        self.button1 = tk.Button(master, text = ' 1 ', bg = 'blue1', font=('Helvetica',80), command=partial(self.click_button,'1'))
        self.button1.place(x = 46, y = 74)
        self.button2 = tk.Button(master, text = ' 2 ', font=('Helvetica',80), bg = 'white smoke', command=partial(self.click_button,'2'))
        self.button2.place(x = 150, y = 74)
        self.button3 = tk.Button(master, text = ' 4 ', font=('Helvetica',80), bg = 'gainsboro', command=partial(self.click_button,'4'))
        self.button3.place(x = 150, y = 179)
        self.button4 = tk.Button(master, text = ' 3 ', font=('Helvetica',80), bg = 'light gray', command=partial(self.click_button,'3'))
        self.button4.place(x = 46, y = 179)

        

    

        def _assert_color(color):
            try:
                for _color in [
                        # 元の値
                        color, 
                        # 大文字
                        color.upper(), 
                        # 小文字
                        color.lower(),
                        ]:
                    Frame(bg=_color)
            except TclError as e:
                self.assertTrue(False, msg=color)

        map(_assert_color, Colors)

    
        
    def click_button(self,num):

        self.random = random.randint(1, 4)

        # 押下したボタンを判定
        if self.random == int(num):
            tmsg.showinfo("正解")
            self.rirekibox.insert(tk.END, '  ' + num + ' : ' + "正解 " + "\n" )
        elif self.random != int(num):
            self.rirekibox.insert(tk.END, '  ' + num + ' : ' + "不正解 " + "\n" )
            tmsg.showerror("error message", "不正解")
                
# ウィンドウを作成する
root = tk.Tk()
root.geometry('400x350')
root.title('Random Button')

app = Application(master=root)
app.mainloop()


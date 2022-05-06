import tkinter as tk
from tkinter import messagebox
fields = '開始日期 (yyyy/mm/dd)', '結束日期 (yyyy/mm/dd)', '請輸入你的時薪', '請輸入你的工作小時'
###輸入框
def fetch(entries):
    for entry in entries:
        field = entry[0]
        text  = entry[1].get()
        print('%s: "%s"' % (field, text))
###輸入框

def pop_up():
    messagebox.showinfo("薪水總額")

###main ui
def makeform(root, fields):
    entries = []
    for field in fields:
        row = tk.Frame(root)
        lab = tk.Label(row, width=20, text=field, anchor='w')
        ent = tk.Entry(row)
        row.pack(side=tk.TOP, fill=tk.X, padx=50, pady=50)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        entries.append((field, ent))
    return entries

###main ui

if __name__ == '__main__':
    root = tk.Tk()
    root.title("薪水計算器")
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))
    root.config(padx=50 , pady=50)
    b1 = tk.Button(root, text='輸入',
                  command=(lambda e=ents: fetch(e)))
    b1.pack(side=tk.LEFT, padx=10, pady=10)
    b2 = tk.Button(root, text='離開', command=root.quit)
    b2.pack(side=tk.LEFT, padx=10, pady=10)
    #動態事件,回到代码头部
    root.mainloop()
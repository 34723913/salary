##GUI
import tkinter as tk
window = tk.Tk() #創立一個叫做tk的視窗
window.title("月薪計算機") #視窗的名稱
window.config(padx=50 , pady=50 , bg="#2479e0") #16進位顏色代碼
## padx/pady,元件邊框與容器之距離(px, 預設=0). bg:背景顏色
label_tittle=tk.Label(text="月薪計算機",
                    bg="#2479e0",
                    fg="#c5d7bd",
                    font=("Arial", 35, "bold"))
label_tittle.grid(row=0, column=0, columnspan=3, pady=30)

label_before_input_date1 =tk.Label(text="請輸入區間1 yyyy/mm/dd:",
                           bg="#2479e0",
                           fg="#c5d7bd",
                           font=("Arial", 15, "bold"))
label_before_input_date2 =tk.Label(text="請輸入區間2 yyyy/mm/dd:",
                           bg="#2479e0",
                           fg="#c5d7bd",
                           font=("Arial", 15, "bold"))
label_before_input_wage = tk.Label(text="請輸入你的時薪:",
                           bg="#2479e0",
                           fg="#c5d7bd",
                           font=("Arial", 15, "bold"))
label_before_input_hours = tk.Label(text="請輸入你的工作小時:",
                           bg="#2479e0",
                           fg="#c5d7bd",
                           font=("Arial", 15, "bold"))
label_before_input_date2.grid(row=1, column=0)

char_input = tk.Entry (bg="#fb743e")
char_input.grid(row=1, column=1)

label_after_input =tk.Label(text="characters.",
                          bg="#2479e0",
                          fg="#c5d7bd",
                          font=("Arial", 15, "bold"))
label_after_input.grid(row=1, column=2)

generate_Click_button = tk.Button(text="產出月薪並複製貼上",
                                  bg="#e028ed",
                                  height=4,
                                  width=55)

window.mainloop()

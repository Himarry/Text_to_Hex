import tkinter as tk
from tkinter import ttk

# 文字列を16進数に変換する関数
def text_to_hex(text):
    # 各文字をUTF-8でエンコードし、バイトごとに16進数2桁大文字で表示
    hex_bytes = text.encode('utf-8')
    return ' '.join(f'{b:02X}' for b in hex_bytes)

# 16進数を文字列に変換する関数
def hex_to_text(hex_str):
    try:
        # 空白区切りで16進数を分割し、バイト配列に変換
        bytes_arr = bytes(int(b, 16) for b in hex_str.strip().split())
        return bytes_arr.decode('utf-8')
    except Exception:
        return '変換エラー'

# ボタンが押されたときの処理
def convert():
    input_text = input_box.get()
    if mode_var.get() == 'text2hex':
        hex_result = text_to_hex(input_text)
        output_box.config(state='normal')
        output_box.delete(0, tk.END)
        output_box.insert(0, hex_result)
        output_box.config(state='readonly')
    else:
        text_result = hex_to_text(input_text)
        output_box.config(state='normal')
        output_box.delete(0, tk.END)
        output_box.insert(0, text_result)
        output_box.config(state='readonly')

root = tk.Tk()
root.title('文字列→16進数 変換ツール')
root.geometry('400x150')

mainframe = ttk.Frame(root, padding='10')
mainframe.pack(fill=tk.BOTH, expand=True)

input_label = ttk.Label(mainframe, text='文字列:')
input_label.grid(row=0, column=0, sticky=tk.W)
input_box = ttk.Entry(mainframe, width=40)
input_box.grid(row=0, column=1, padx=5, pady=5)

convert_button = ttk.Button(mainframe, text='変換', command=convert)
convert_button.grid(row=1, column=0, columnspan=2, pady=10)

output_label = ttk.Label(mainframe, text='結果:')
output_label.grid(row=2, column=0, sticky=tk.W)
output_box = ttk.Entry(mainframe, width=40, state='readonly')
output_box.grid(row=2, column=1, padx=5, pady=5)

mode_var = tk.StringVar(value='text2hex')
mode_frame = ttk.Frame(mainframe)
mode_frame.grid(row=3, column=0, columnspan=2, pady=5)
text2hex_radio = ttk.Radiobutton(mode_frame, text='文字列→16進数', variable=mode_var, value='text2hex')
hex2text_radio = ttk.Radiobutton(mode_frame, text='16進数→文字列', variable=mode_var, value='hex2text')
text2hex_radio.pack(side=tk.LEFT, padx=5)
hex2text_radio.pack(side=tk.LEFT, padx=5)

root.mainloop()

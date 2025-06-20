import tkinter as tk
from tkinter import ttk

# テキストを16進数に変換する関数
def text_to_hex(text):
    # 日本語もいけるようにUTF-8でエンコードする。
    # バイトごとにスペースで区切って見やすくする。
    hex_bytes = text.encode('utf-8')
    return ' '.join(f'{b:02X}' for b in hex_bytes)

# 16進数をテキストに戻す関数
def hex_to_text(hex_str):
    try:
        # スペースで区切られた16進数をバイトに戻して、UTF-8でデコード。
        bytes_arr = bytes(int(b, 16) for b in hex_str.strip().split())
        return bytes_arr.decode('utf-8')
    except Exception:
        # 変な値が入力されたらエラーを返す。
        return '変換エラー'

# 「変換」ボタンが押されたときの処理
def convert():
    input_text = input_box.get()
    # どっちのモードが選ばれてるかで処理を分岐させる。
    if mode_var.get() == 'text2hex':
        hex_result = text_to_hex(input_text)
        # 結果を入れるために一時的に書き込み可能にする。
        output_box.config(state='normal')
        output_box.delete(0, tk.END)
        output_box.insert(0, hex_result)
        output_box.config(state='readonly') # 終わったら読み取り専用に戻す。
    else:
        text_result = hex_to_text(input_text)
        # こっちも同じように結果をセットする。
        output_box.config(state='normal')
        output_box.delete(0, tk.END)
        output_box.insert(0, text_result)
        output_box.config(state='readonly')

# --- ここからGUIの作成 ---
root = tk.Tk()
root.title('文字列⇔16進数 変換ツール')
root.geometry('400x150')

mainframe = ttk.Frame(root, padding='10')
mainframe.pack(fill=tk.BOTH, expand=True)

input_label = ttk.Label(mainframe, text='入力:')
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

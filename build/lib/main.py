#!/usr/bin/env python3

import tkinter as tk
import subprocess
import requests
import os
import sys
import time

VERSION = "1.0.0"

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora 1")

        self.result = tk.Entry(root, width=16, font=('Arial', 24), bd=10, insertwidth=4, borderwidth=4, justify='right')
        self.result.grid(row=0, column=0, columnspan=4)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, padx=20, pady=20, font=('Arial', 18), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col)

    def on_button_click(self, text):
        if text == '=':
            try:
                result = str(eval(self.result.get()))
                self.result.delete(0, tk.END)
                self.result.insert(tk.END, result)
            except:
                self.result.delete(0, tk.END)
                self.result.insert(tk.END, 'Erro')
        else:
            self.result.insert(tk.END, text)

def check_for_update():
    try:
        response = requests.get('https://raw.githubusercontent.com/JoaoAmpeze/Calculadora_Pyton/master/version.txt')
        latest_version = response.text.strip()
        if latest_version != VERSION:
            download_update()
    except Exception as e:
        print(f"Erro ao verificar atualização: {e}")

def download_update():
    try:
        url = 'https://raw.githubusercontent.com/JoaoAmpeze/Calculadora_Pyton/master/test_script.py'
        response = requests.get(url)
        if response.status_code == 200:
            content_type = response.headers.get('Content-Type', '')
            if 'text/plain' in content_type:
                with open('main.py', 'wb') as f:
                    f.write(response.content)
                print("Atualização concluída. Reiniciando o aplicativo...")

                subprocess.Popen([sys.executable, 'main.py'])
                
                time.sleep(2)
                
                sys.exit()
            else:
                print("O arquivo baixado não é um script Python.")
        else:
            print(f"Erro ao baixar o arquivo: Status Code {response.status_code}")
    except Exception as e:
        print(f"Erro ao baixar atualização: {e}")

def start_calculator():
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    check_for_update()
    start_calculator()

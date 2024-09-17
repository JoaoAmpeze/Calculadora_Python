import requests
import os
import sys
import subprocess
import tkinter as tk

# Função para verificar atualizações
def check_for_update():
    try:
        # URL do arquivo que contém a versão mais recente
        version_url = "https://github.com/JoaoAmpeze/Calculadora_Pyton/blob/master/version.txt"
        response = requests.get(version_url)
        if response.status_code != 200:
            raise Exception(f"Erro ao acessar {version_url}: {response.status_code}")
        latest_version = response.text.strip()

        # Lê a versão local
        if not os.path.exists("version.txt"):
            with open("version.txt", "w") as file:
                file.write("0.0.0")  # Versão inicial se o arquivo não existir
        with open("version.txt", "r") as file:
            local_version = file.read().strip()

        if local_version != latest_version:
            print("Nova versão disponível!")
            # URL do arquivo para download
            script_url = "https://github.com/JoaoAmpeze/Calculadora_Pyton/blob/master/latest_script.py"
            response = requests.get(script_url)
            if response.status_code != 200:
                raise Exception(f"Erro ao acessar {script_url}: {response.status_code}")
            with open("latest_script.py", "wb") as file:
                file.write(response.content)
            with open("version.txt", "w") as file:
                file.write(latest_version)
            print("Atualização concluída. Reiniciando...")
            subprocess.Popen([sys.executable, "latest_script.py"])
            sys.exit()

    except Exception as e:
        print(f"Erro ao verificar atualizações: {e}")

# Verificar atualizações no início
check_for_update()

# Código da calculadora
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Erro")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Calculadora")

entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]

row = 1
col = 0
for button in buttons:
    b = tk.Button(root, text=button, width=4, height=2, font=('Arial', 18))
    b.grid(row=row, column=col)
    b.bind("<Button-1>", click)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()

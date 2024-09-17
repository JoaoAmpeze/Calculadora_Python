
import requests

def check_for_update():
    try:
        response = requests.get('https://raw.githubusercontent.com/JoaoAmpeze/Calculadora_Pyton/master/version.txt')  # URL onde a versão mais recente está disponível
        latest_version = response.text.strip()
        if latest_version != '1.0.0':  # Substitua '1.0.0' com a versão atual
            download_update()
    except Exception as e:
        print(f"Erro ao verificar atualização: {e}")

def download_update():
    try:
        response = requests.get('https://raw.githubusercontent.com/JoaoAmpeze/Calculadora_Pyton/master/main.py')  # URL do arquivo atualizado
        with open('calculator.py', 'wb') as f:
            f.write(response.content)
        print("Atualização concluída. Reiniciando o aplicativo...")
        subprocess.call(['python', 'calculator.py'])
    except Exception as e:
        print(f"Erro ao baixar atualização: {e}")

if __name__ == "__main__":
    check_for_update()

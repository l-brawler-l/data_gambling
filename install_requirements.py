import subprocess
import sys

def install_requirements():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Зависимости успешно установлены.")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при установке зависимостей: {e}")

if __name__ == "__main__":
    install_requirements()
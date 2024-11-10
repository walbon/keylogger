import json
import os
import time
from pynput import keyboard
from collections import Counter

# Nome do arquivo JSON para o registro persistente
LOG_FILE = "key_usage.json"
key_count = Counter()

# Função para carregar o dicionário do arquivo JSON (se existir)
def load_key_counts():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as file:
            data = json.load(file)
            return Counter(data)
    return Counter()

# Função para salvar o dicionário no arquivo JSON
def save_key_counts():
    with open(LOG_FILE, "w") as file:
        json.dump(dict(key_count), file)

# Função de incremento ao pressionar teclas
def on_press(key):
    try:
        key_count[str(key).replace("'", "")] += 1
    except AttributeError:
        pass

# Função para atualizar o arquivo JSON periodicamente
def periodic_save(interval=300):
    while True:
        save_key_counts()
        time.sleep(interval)

# Função principal para rodar o daemon
def run_daemon():
    global key_count
    # Carrega o histórico do arquivo JSON
    key_count = load_key_counts()
    
    # Configura o listener do teclado
    with keyboard.Listener(on_press=on_press) as listener:
        # Inicia a atualização periódica do arquivo em paralelo
        periodic_save()
        listener.join()

if __name__ == "__main__":
    run_daemon()

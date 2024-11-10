import json
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

# Nome do arquivo JSON
LOG_FILE = "key_usage.json"

# Carrega o dicionário de uso de teclas do arquivo JSON
def load_key_counts():
    with open(LOG_FILE, "r") as file:
        return json.load(file)

# Função para criar gráfico de barras
def plot_bar_chart(data):
    keys = list(data.keys())
    counts = list(data.values())
    counts = [round((x - min(counts)) / (max(counts) - min(counts)),3) for x in counts] 
    plt.figure(figsize=(10, 10))
    plt.barh(keys, counts, color='skyblue')
    plt.ylabel("Teclas")
    plt.xlabel("Frequência de Uso")
    plt.title("Frequência de Uso das Teclas (Gráfico de Barras)")
    plt.xticks()
    #plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

def plot_2_barh_chart(data):
    keys = list(data.keys())
    counts = list(data.values())
    counts = [round((x - min(counts)) / (max(counts) - min(counts)),3) for x in counts] 
    # Dividir dados em duas metades
    mid_index = len(keys) // 2
    keys_left = keys[:mid_index]
    counts_left = counts[:mid_index]
    keys_right = keys[mid_index:]
    counts_right = counts[mid_index:]

    fig, axs = plt.subplots(1, 2, figsize=(16, 6))

    # Gráfico da coluna esquerda
    axs[0].barh(keys_left, counts_left, color='skyblue')
    axs[0].set_title("Frequência de Uso (Coluna 1)")
    axs[0].set_xlabel("Frequência de Uso")
    axs[0].set_ylabel("Teclas (Coluna 1)")

    # Gráfico da coluna direita
    axs[1].barh(keys_right, counts_right, color='skyblue')
    axs[1].set_title("Frequência de Uso (Coluna 2)")
    axs[1].set_xlabel("Frequência de Uso")
    axs[1].set_ylabel("Teclas (Coluna 2)")
    # Ajustar layout
    plt.tight_layout()
    plt.show()

# Função para criar gráfico de pizza
def plot_pie_chart(data):
    keys = list(data.keys())
    counts = list(data.values())
    
    plt.figure(figsize=(8, 8))
    plt.pie(counts, labels=keys, autopct="%1.1f%%", startangle=140)
    plt.title("Distribuição de Uso das Teclas (Gráfico de Pizza)")
    plt.show()

if __name__ == "__main__":
    # Carrega os dados
    data = load_key_counts()
    
    # Plota o gráfico de barras
    #plot_bar_chart(data)ar_chart(data)
    plot_2_barh_chart(data)
    
    # Plota o gráfico de pizza
#    plot_pie_chart(data)

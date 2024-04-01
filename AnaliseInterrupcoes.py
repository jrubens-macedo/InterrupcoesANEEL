import csv
from datetime import datetime
import matplotlib.pyplot as plt

# Caminho do arquivo CSV de entrada
caminho_arquivo_csv = r"C:\pythonjr\interrupcoes_ANEEL\exemplo_base_de_dados.csv"
def contar_linhas_colunas(csv_file):
    """Conta o número de linhas e colunas no arquivo CSV."""
    with open(csv_file, 'r', encoding='latin-1') as f:
        leitor_csv = csv.reader(f, delimiter=';')
        # Contar as colunas (baseado na primeira linha)
        num_colunas = len(next(leitor_csv))
        # Voltar para o início do arquivo
        f.seek(0)
        # Contar as linhas
        num_linhas = sum(1 for linha in leitor_csv)
    return num_linhas, num_colunas

def diferenca_de_tempo(tempo1, tempo2):
    """Calcula a diferença entre dois tempos em minutos."""
    tempo1 = datetime.strptime(tempo1, "%Y-%m-%d %H:%M:%S")
    tempo2 = datetime.strptime(tempo2, "%Y-%m-%d %H:%M:%S")
    diferenca = tempo2 - tempo1
    return round(diferenca.total_seconds() / 60, 2)  # Retorna a diferença em minutos com duas casas decimais

def processar_arquivo_csv(csv_file, novo_csv_file):
    """Processa o arquivo CSV de entrada e cria um novo arquivo CSV com as diferenças de tempo."""
    with open(csv_file, 'r', encoding='latin-1') as f:
        leitor_csv = csv.reader(f, delimiter=';')
        # Ignorar o cabeçalho do CSV
        next(leitor_csv)
        with open(novo_csv_file, 'w', newline='', encoding='utf-8') as novo_csv:
            escritor_csv = csv.writer(novo_csv)
            for linha in leitor_csv:
                # Obter os tempos das colunas 9 e 10
                tempo1 = linha[8]
                tempo2 = linha[9]
                # Calcular a diferença entre os tempos
                diferenca = diferenca_de_tempo(tempo1, tempo2)
                # Escrever a diferença de tempo formatada com duas casas decimais no novo arquivo CSV
                escritor_csv.writerow(["{:.2f}".format(diferenca)])

# Obter a quantidade de linhas e colunas do arquivo CSV de entrada
linhas, colunas = contar_linhas_colunas(caminho_arquivo_csv)
print("Resumo do arquivo de entrada ---------------")
print(f"  Quantidade de linhas = {linhas}")
print(f"  Quantidade de colunas = {colunas}")
print("--------------------------------------------")

# Caminho do novo arquivo CSV de saída
novo_csv_file = r"C:\pythonjr\interrupcoes_ANEEL\diferenca_tempos.csv"

# Processar o arquivo CSV de entrada e criar o novo arquivo CSV com as diferenças de tempo
processar_arquivo_csv(caminho_arquivo_csv, novo_csv_file)

print("Arquivo CSV criado com sucesso!")

# Leitura do arquivo CSV com as diferenças de tempo
with open(novo_csv_file, 'r', encoding='utf-8') as f:
    leitor_csv = csv.reader(f)
    # Extrair os dados de diferenças de tempo
    diferencas_tempo = [float(row[0]) for row in leitor_csv]

# Calcular a diferença máxima e mínima de tempo
min_tempo = min(diferencas_tempo)
max_tempo = max(diferencas_tempo)

# Calcular o número de bins necessário para garantir que cada bin tenha 10 minutos
num_bins = int((max_tempo - min_tempo) / 10)

# Criar o histograma com bins de 10 minutos
plt.figure(figsize=(25, 6))
plt.hist(diferencas_tempo, bins=num_bins, range=(min_tempo, max_tempo), color='blue', edgecolor='white')
plt.xlabel('Duração (minutos)', fontsize=14)
plt.ylabel('Frequência de Ocorrências', fontsize=14)
plt.grid(True, linestyle='--')
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlim(0, 4000)
plt.show()




import csv
from datetime import datetime

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

# Caminho do arquivo CSV de entrada
caminho_arquivo_csv = r"C:\pythonjr\InterrupcoesANEEL\interrupcoes-energia-eletrica-2024.csv"

# Obter a quantidade de linhas e colunas do arquivo CSV de entrada
linhas, colunas = contar_linhas_colunas(caminho_arquivo_csv)
print("Resumo do arquivo de entrada ---------------")
print(f"  Quantidade de linhas = {linhas}")
print(f"  Quantidade de colunas = {colunas}")
print("--------------------------------------------")

# Caminho do novo arquivo CSV de saída
novo_csv_file = r"C:\pythonjr\InterrupcoesANEEL\diferenca_tempos.csv"

# Processar o arquivo CSV de entrada e criar o novo arquivo CSV com as diferenças de tempo
processar_arquivo_csv(caminho_arquivo_csv, novo_csv_file)

print("Arquivo CSV criado com sucesso!")



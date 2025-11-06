import re
from datetime import datetime

# Caminho do arquivo de log (pode ser qualquer .txt)
arquivo_log = "logs.txt"

# Lista de palavras-chave suspeitas
palavras_suspeitas = [
    "error", "fail", "denied", "unauthorized", "invalid", "attack", "warning"
]

# Lê o arquivo
with open(arquivo_log, "r", encoding="utf-8") as f:
    linhas = f.readlines()

# Filtra as linhas suspeitas
linhas_suspeitas = []
for linha in linhas:
    if any(re.search(palavra, linha, re.IGNORECASE) for palavra in palavras_suspeitas):
        linhas_suspeitas.append(linha.strip())

# Gera o relatório
nome_relatorio = f"relatorio_logs_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

with open(nome_relatorio, "w", encoding="utf-8") as f:
    f.write("=== Relatório de Análise de Logs ===\n")
    f.write(f"Data de geração: {datetime.now()}\n")
    f.write(f"Total de linhas analisadas: {len(linhas)}\n")
    f.write(f"Linhas suspeitas encontradas: {len(linhas_suspeitas)}\n\n")

    for linha in linhas_suspeitas:
        f.write(linha + "\n")

print(f"✅ Análise concluída! Relatório salvo em: {nome_relatorio}")





  
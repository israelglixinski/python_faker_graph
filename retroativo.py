import os
import random
import subprocess
from datetime import datetime, timedelta

# Caminho do repositório Git (pode ser '.' se for o diretório atual)
repo_path = "."

# Definir a data inicial (1º de janeiro de 2025, 00:00)
start_date  = datetime(2020,  1,  1,  0, 0)
end_date    = datetime(2020, 12, 31, 23, 0)  # Última hora do mês

# Criar um arquivo de log para modificar em cada commit
file_path = os.path.join(repo_path, "commit.txt")

# Loop para iterar por todas as horas do mês de janeiro de 2025
current_date = start_date
while current_date <= end_date:

    aleatorio = random.randint(1, 3)
    if aleatorio == 1:

        # Modificar o arquivo para criar uma mudança
        with open(file_path, "a") as f:
            f.write(f"Commit realizado em {current_date}\n")

        # Adicionar arquivos ao commit
        subprocess.run(["git", "add", file_path], cwd=repo_path)

        # Criar commit com data específica
        commit_message = f"Retroactive commit for {current_date}"
        subprocess.run(["git", "commit", "-m", commit_message, "--date", current_date.strftime("%Y-%m-%dT%H:%M:%S")], cwd=repo_path)
        # subprocess.run(["git", "push", "origin", "main"], cwd=repo_path)


    # Avançar para a próxima hora
    current_date += timedelta(hours=1)

# Enviar todos os commits para o repositório remoto
# subprocess.run(["git", "push", "github", "main2"], cwd=repo_path)
subprocess.run(["git", "push", "origin", "main"], cwd=repo_path)

print("Todos os commits retroativos foram criados e enviados com sucesso!")

Backup Retention & Cleanup Script

English 
I developed this Python script to automate the cleanup of local or remote backup directories, applying custom retention rules per client/folder and preventing storage overflow. The main issue was the time previously required to clean up the 20 folders; this script reduces that time, streamlining my daily workflow. In the future, I plan to add email notifications for corrupted or empty backups.

Script Features
Customizable Rules: Define different retention periods (in days) for each mapped directory.
Flexible Mapping: Supports nested paths (subfolders).
Efficiency: Uses the native `pathlib` library for safe path and file handling within the operating system.

How to Use
1. Ensure Python is installed on your machine.
2. Configure the `regras_de_backup` dictionary in the code with the directory paths and their respective retention limits (in days).
3. Update the root path in the `limpar_backups(r"YOUR_PATH")` function call.
4. Run the script via the terminal:
   ```bash
   python limpeza_backup.py

Português
Desenvolvi este script em Python para automatizar a limpeza de diretórios de backup locais ou remotos, aplicando regras de retenção personalizadas por cliente/pasta e prevenindo a superlotação do armazenamento. A principal questão era o tempo que levava hoje para limpar as 20 pastas, e comparado com hoje, o tempo diminuiu com a funcionalidade que facilita meu processo no dia a dia. Futuramente pretendo colocar um aviso de e-mail para backup corrompidos ou em branco.

Funcionalidades do script
Regras Customizáveis:  Define diferentes períodos de retenção (em dias) para cada diretório mapeado.
Mapeamento Flexível: Suporte a caminhos aninhados (subpastas).
Eficiência: Utiliza a biblioteca nativa `pathlib` para manipulação segura de caminhos e arquivos no sistema operacional.

Como Usar
1. Certifique-se de ter o Python instalado em sua máquina.
2. Configure o dicionário `regras_de_backup` no código com os caminhos dos diretórios e seus respectivos limites de dias.
3. Altere o caminho raiz na chamada da função `limpar_backups(r"SEU_CAMINHO")`.
4. Execute o script via terminal:
   ```bash
   python limpeza_backup.py
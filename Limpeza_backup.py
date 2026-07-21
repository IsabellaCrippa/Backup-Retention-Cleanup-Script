import os
import time
from pathlib import Path

regras_de_backup = {
    r"cliente_a\vimp": 4,  
    "cliente_b": 4,  
    "cliente_c": 3,   
    "cliente_d": 5  
}

def limpar_backups(pasta_raiz):
    raiz = Path(pasta_raiz)
    
    for nome_pasta, dias_limite in regras_de_backup.items():
        caminho = raiz / nome_pasta
        
        if not caminho.exists():
            print(f"Pasta {caminho} não encontrada, pulando...")
            continue
            
        agora = time.time()
        segundos_limite = dias_limite * 86400
        
        for arquivo in caminho.glob("*"):
            tempo_modificacao = arquivo.stat().st_mtime
            
            if (agora - tempo_modificacao) > segundos_limite:
                print(f"Deletando: {arquivo.name} (mais antigo que {dias_limite} dias)")
                arquivo.unlink()

limpar_backups(r"E:\ftp")
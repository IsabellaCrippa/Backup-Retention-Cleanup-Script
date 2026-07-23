import os
import time
import shutil
from pathlib import Path

regras_de_backup = {
    "empresa_a": 7,    
    "empresa_b": 1,  
    "empresa_c": 1,  
    r"empresa_c\sub_1": 1,  
    "empresa_d": 7,  
    "empresa_e": 1,
    "empresa_f": 1,
    "empresa_g": 1,
    r"empresa_g\sub_1": 1,
    "empresa_h": 1,
    "empresa_i": 1,
    "empresa_j": 1,
    r"empresa_j\sub_1": 1,
    "empresa_k": 1,
    "empresa_l": 2,
    r"empresa_l\sub_1": 2,
    "empresa_m": 1,
    "empresa_n": 1,
    "empresa_o": 1,
    r"empresa_o\sub_1": 1,
    "empresa_p": 1,
    "empresa_q": 1,
    "empresa_r": 1,
    "empresa_s": 1,
    "empresa_t": 1,
    "empresa_u": 1,
    "empresa_v": 1, 
    "empresa_w": 1, 
    "empresa_x": 1,    
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
        
        for item in caminho.glob("*"):
            try:
                tempo_modificacao = item.stat().st_mtime
                
                if (agora - tempo_modificacao) > segundos_limite:
                    if item.is_dir():
                        print(f"Deletando pasta: {item.name} (mais antiga que {dias_limite} dias)")
                        shutil.rmtree(item)
                    else:
                        print(f"Deletando arquivo: {item.name} (mais antigo que {dias_limite} dias)")
                        item.unlink()
            except Exception as e:
                # Se der erro (arquivo aberto, sem permissão, etc.), ele avisa e continua o loop
                print(f"Não foi possível deletar '{item.name}': {e}")

limpar_backups(r"\\Servidor\ftp\VPS")
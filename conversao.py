import os
from PIL import Image
from pathlib import Path

# Como você já está rodando o script de DENTRO da pasta cdm-icons:
caminho_origem = Path('.') # O ponto '.' significa "a pasta atual"

# O '../' sobe um nível. A pasta nova será criada dentro de "Módulo Foundry", 
# ficando lado a lado com a sua pasta cdm-icons original.
caminho_destino = Path('../cdm-icons-webp') 

# Percorre todos os arquivos PNG recursivamente
for arquivo in caminho_origem.rglob('*.png'):
    try:
        caminho_relativo = arquivo.relative_to(caminho_origem)
        
        caminho_novo_arquivo = (caminho_destino / caminho_relativo).with_suffix('.webp')
        
        caminho_novo_arquivo.parent.mkdir(parents=True, exist_ok=True)
        
        img = Image.open(arquivo)
        img.save(caminho_novo_arquivo, 'webp', quality=85)
        
        print(f'Convertido: {caminho_relativo} -> {caminho_novo_arquivo.name}')
        
    except Exception as e:
        print(f'Erro ao converter {arquivo}: {e}')

print("\nConversão de todas as subpastas finalizada com sucesso!")
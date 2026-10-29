from pathlib import Path

from PIL import Image


def converter(arquivo):
    destino = arquivo.with_suffix('.webp')
    # Não sobrescreve uma imagem WebP que já exista.
    with Image.open(arquivo) as img:
        tamanho = img.size
        with destino.open('xb') as saida:
            img.save(saida, 'WEBP', quality=85)

    # Só apaga o PNG depois de reabrir e decodificar a imagem salva.
    with Image.open(destino) as convertido:
        convertido.load()
        if convertido.format != 'WEBP' or convertido.size != tamanho:
            raise ValueError(f'Falha na validação de {destino}')
    arquivo.unlink()
    return destino


def main():
    caminho_origem = Path(__file__).resolve().parent
    arquivos = [p for p in caminho_origem.rglob('*')
                if p.is_file() and p.suffix.lower() == '.png'
                and not {'.git', '.venv', 'venv'}.intersection(
                    p.relative_to(caminho_origem).parts)]
    convertidos = 0
    erros = 0
    for arquivo in arquivos:
        try:
            destino = converter(arquivo)
            convertidos += 1
            print(f'Convertido e PNG removido: {destino.relative_to(caminho_origem)}')
        except Exception as e:
            erros += 1
            print(f'PNG preservado: {arquivo} — {e}')

    print(f'\nFinalizado: {convertidos} convertido(s), {erros} erro(s).')
    if not arquivos:
        print('Nenhum PNG encontrado.')
    return 1 if erros else 0


if __name__ == '__main__':
    raise SystemExit(main())

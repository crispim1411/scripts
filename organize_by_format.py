import os
import shutil

try:
    username = 'Crispim'
    src = os.path.join('/', 'Users', username, 'Downloads')
    dst = os.path.join('/', 'Users', username, 'Documents', 'organized')
    folders = [
        "zip", "rar",           # compactados
        "pdf", "txt", "doc", "docx", # texto
        "exe", "msi",           # executáveis
        "png", "jpg", "jpeg",   # imagens
        "mp4", "mvk", "iso"]    # vídeos

    # caso não exista a pasta de destino
    if not os.path.exists(dst):
        os.mkdir(dst)

    # cria as pastas de cada extensão caso não existam
    os.chdir(dst)
    list_src = os.listdir()
    for folder in folders:
        if folder not in list_src:
            os.mkdir(folder)

    # organiza os arquivos em pastas
    os.chdir(src)
    list_dst = os.listdir()
    for file in list_dst:
        for folder in folders:
            if file.lower().endswith(folder):
                file_src = os.path.join('/', src, file)
                file_dst = os.path.join('/', dst, folder, file)
                shutil.move(file_src, file_dst)
                break

except FileNotFoundError as file_err:
    print(f'File not found: {file_err}')
except Exception as e:
    print(f'Error: {e}')

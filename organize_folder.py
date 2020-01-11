# ctrl + Q doc
# ctrl + N search
# ctrl + space
# shift + F6
# ctrl + P parameters
# ctrl + D duplicate
import os
import shutil

try:
    username = 'Crispim'
    folder_to_organize = 'Downloads'
    src = os.path.join('/', 'Users', username, folder_to_organize)
    dst = os.path.join('/', 'Users', username)

    folders = ['compressed', 'executable', 'docs', 'iso']

    image_formats = ['.png', '.jpg', '.jpeg']
    compressed_formats = ['.zip', '.rar']
    doc_formats = ['.doc', '.docx', '.pdf', '.txt']
    video_formats = ['mp4', 'mkv']

    # cria as pastas caso não existam
    os.chdir(os.path.join('/', dst, 'Documents'))
    list_src = os.listdir()
    for folder in folders:
        if folder not in list_src:
            os.mkdir(folder)

    # organiza os arquivos em pastas
    os.chdir(src)
    list_dst = [i.lower() for i in os.listdir()]
    for file in list_dst:
        file_src = os.path.join('/', src, file)
        file_dst = None
        if file.endswith('.exe'):
            file_dst = os.path.join('/', dst, 'Documents', 'executable', file)
        elif file.endswith('.iso'):
            file_dst = os.path.join('/', dst, 'Documents', 'iso', file)
        elif any([file.endswith(f) for f in compressed_formats]):
            file_dst = os.path.join('/', dst, 'Documents', 'compressed', file)
        elif any([file.endswith(f) for f in doc_formats]):
            file_dst = os.path.join('/', dst, 'Documents', 'docs', file)
        elif any([file.endswith(f) for f in image_formats]):
            file_dst = os.path.join('/', dst, 'Pictures', file)
        elif any([file.endswith(f) for f in video_formats]):
            file_dst = os.path.join('/', dst, 'Videos', file)
        else:
            print(f"Arquivo não movido formato: {file.split('.')[-1]}")

        if file_dst:
            shutil.move(file_src, file_dst)

except FileNotFoundError as file_err:
    print(f"File not found: {file_err}")
except Exception as e:
    print(f"Error: {e}")

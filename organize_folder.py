import os
import shutil


def create_folders(dst, folders):
    """
    Crias as pastas de destino para os arquivos

    Args:
        dst (str) : caminho de destino
        folders (list) : lista das pastas a serem criadas

    Raises:
        Exception : Falha na criaçã das pastas de destino
    """
    try:
        os.chdir(os.path.join('/', dst, 'Documents'))
        list_src = os.listdir()
        for folder in folders:
            if folder not in list_src:
                os.mkdir(folder)
    except Exception as e:
        print(f"Falha na criação das pastas: {e}")


def move_file(src, dst):
    """
    Move os arquivos para a pasta de destino de acordo com sua extensão.

    Args:
        src (str) : caminho onde reside o arquivo
        dst (str) : caminho de destino do arquivo

    Raises:
        Exception : Falha ao mover arquivo
        FileNotFoundError : Arquivo não encontrado
    """
    try:
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
            # se existir caminho de destino move
            if file_dst:
                shutil.move(file_src, file_dst)
    except FileNotFoundError as file_err:
        print(f"Arquivo não encontrado: {file_err}")
    except Exception as e:
        print(f"Falha ao mover arquivo: {e}")


if __name__ == '__main__':
    # usuario e pasta a organizar
    username = 'Crispim'
    folder_to_organize = 'Downloads'
    src_path = os.path.join('/', 'Users', username, folder_to_organize)
    dst_path = os.path.join('/', 'Users', username)

    # pastas de destino
    dst_folders = ['compressed', 'executable', 'docs', 'iso']

    # formatos a serem organizados
    image_formats = ['.png', '.jpg', '.jpeg']
    compressed_formats = ['.zip', '.rar']
    doc_formats = ['.doc', '.docx', '.pdf', '.txt']
    video_formats = ['mp4', 'mkv']

    create_folders(dst_path, dst_folders)
    move_file(src_path, dst_path)

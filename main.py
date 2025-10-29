import os
import shutil

path_dir = "E:\\random_dir\\"

path_documents = f"{path_dir}\\Documents\\"

if os.path.exists(path_documents) is False:
    os.mkdir(path_documents)

for arquivo in os.listdir(path_dir):

    if arquivo.endswith(".txt"):
        path_arquivo_origem = os.path.join(path_dir,arquivo)
        path_arquivo_destino = os.path.join(path_documents,arquivo)

        if os.path.isfile(path_arquivo_origem):
            shutil.move(path_arquivo_origem,path_arquivo_destino)
            print(f"Arquivo: {arquivo} \n Movido com sucesso")


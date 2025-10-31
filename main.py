import os
import shutil

path_dir = "C:\\Users\\arthu\\Downloads\\"

mapeamento_extensoes = {
    ".txt":"Documents",
    ".docx":"Documents",
    ".pdf":"Documents",
    ".png":"Imagens",
    ".jpeg":"Imagens",
    ".mp4":"Videos",
    ".zip":"Zipados",
    ".rar":"Zipados",
    ".xlsx":"Planilhas",
    ".csv":"Planilhas",
    ".exe":"Executaveis"
}


for arquivo in os.listdir(path_dir):

    arquivo_origen = os.path.join(path_dir,arquivo)

    if os.path.isfile(arquivo_origen):
        extensao = os.path.splitext(arquivo)
        nome_pasta = mapeamento_extensoes.get(extensao[1],"Outros")
        pasta_destino = os.path.join(path_dir,nome_pasta)


        arquivo_pasta_destino = os.path.join(pasta_destino,arquivo)

        if os.path.exists(pasta_destino) is False:
            os.mkdir(pasta_destino)

        if os.path.exists(arquivo_pasta_destino) is True: 
            i = 0

            while True:

                i += 1
                rename = extensao[0] + (f"({i})") + extensao[1]
                arquivo_pasta_destino_rename = os.path.join(pasta_destino,rename)

                if os.path.exists(arquivo_pasta_destino_rename) is False:
                    shutil.move(arquivo_origen,arquivo_pasta_destino_rename)
                    print(f"Arquivo: {arquivo_pasta_destino_rename} \nMovido com sucesso")
                    break
        else:
            shutil.move(arquivo_origen,pasta_destino)
            print(f"Arquivo: {arquivo} \n Movido com sucesso")
                    
    
    if os.path.isdir(arquivo_origen):
        pasta_destino = os.path.join()





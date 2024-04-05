def contar_palavras(arquivo):
    
    with open(arquivo, 'r') as f:
        
        texto = f.read()
        
        palavras = texto.split()
       
        num_palavras = len(palavras)
    return num_palavras


caminho_arquivo = 'C:\\Users\\leticia.ferreira\\Desktop\\texto.txt'


num_palavras = contar_palavras(caminho_arquivo)


print(f'O arquivo "{caminho_arquivo}" contém {num_palavras} palavras.')
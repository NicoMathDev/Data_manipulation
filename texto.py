from cgitb import text


caminho = 'C:/Users/nico_/Music/Arquivos_Lojas\Arquivos_Lojas/202004_Morumbi_SP.csv'

for i in range(len(caminho)):
    j = (len(caminho) - (1+i))
    if caminho[j] == '\\':
        print(caminho[j+1:])
        break

import os

# Caminho absoluto do diretório
diretorio = 'C:\\Users\\Administrador\\Documents\\Git e Github\\Dio-desafio-De-primerio-Repositorio\\Estilizações basicas com Css\\fundo-dos-elementos\\Redimensionando-as-Imagens-de-Fundo-dos-Elementos'

# Lista apenas os nomes de arquivos no diretório
arquivos = [arquivo for arquivo in os.listdir(diretorio) if os.path.isfile(os.path.join(diretorio, arquivo))]

# Nome do arquivo de script .bat com caminho absoluto
arquivo_bat = os.path.join(diretorio, 'comandos_git.bat')

# Comandos Git
comandos_git = []

# Adiciona arquivos de imagem
arquivos_imagem = [arquivo for arquivo in arquivos if any(extensao in arquivo for extensao in ['.png', '.jpg', '.jpeg'])]
if arquivos_imagem:
    comandos_git.append(f'git add {" ".join([f"\"{arquivo}\"" for arquivo in arquivos_imagem])} && git commit -m "Arquivos de imagem do exemplo"')

# Adiciona arquivos HTML
arquivos_html = [arquivo for arquivo in arquivos if arquivo.endswith('.html')]
if arquivos_html:
    comandos_git.append(f'git add {" ".join([f"\"{arquivo}\"" for arquivo in arquivos_html])} && git commit -m "Arquivos HTML do exemplo"')

# Adiciona arquivos CSS
arquivos_css = [arquivo for arquivo in arquivos if arquivo.endswith('.css')]
if arquivos_css:
    comandos_git.append(f'git add {" ".join([f"\"{arquivo}\"" for arquivo in arquivos_css])} && git commit -m "Arquivo CSS do exemplo"')

# Adiciona comando git push origin main
comandos_git.append('git push origin main')

# Escreve os comandos Git no arquivo .bat
with open(arquivo_bat, 'w') as f:
    f.write('\n'.join(comandos_git))

print(f'Arquivo de script gerado: {arquivo_bat}')

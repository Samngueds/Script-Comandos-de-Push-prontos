import os

# Caminho do diretório
diretorio = 'Aqui-o-seu-Diretorio'

arquivos = [arquivo for arquivo in os.listdir(diretorio) if os.path.isfile(os.path.join(diretorio, arquivo))]

arquivo_bat = os.path.join(diretorio, 'comandos_git.bat')

comandos_git = []

arquivos_html = [arquivo for arquivo in arquivos if arquivo.endswith('.html')]
if arquivos_html:
    for arquivo_html in arquivos_html:
        with open(os.path.join(diretorio, arquivo_html), 'r', encoding='utf-8') as file:
           
            lines = file.readlines()
            for line in lines:
                if '<title>' in line:
                    title = line.strip().replace('<title>', '').replace('</title>', '')
                    break
            else:
                title = 'Sem título'

        comandos_git.append(f'git add "{arquivo_html}" && git commit -m "Arquivo HTML do exemplo: {title}"')

arquivos_css = [arquivo for arquivo in arquivos if arquivo.endswith('.css')]
if arquivos_css:
    comandos_git.append(f'git add {" ".join([f"\"{arquivo}\"" for arquivo in arquivos_css])} && git commit -m "Arquivos de CSS do exemplo"')


arquivos_imagem = [arquivo for arquivo in arquivos if any(extensao in arquivo for extensao in ['.png', '.jpg', '.jpeg'])]
if arquivos_imagem:
    comandos_git.append(f'git add {" ".join([f"\"{arquivo}\"" for arquivo in arquivos_imagem])} && git commit -m "Arquivos de imagem do exemplo"')


comandos_git.append('git push origin main')


with open(arquivo_bat, 'w', encoding='utf-8') as f:
    f.write('\n'.join(comandos_git))

print(f'Arquivo de script gerado: {arquivo_bat}')

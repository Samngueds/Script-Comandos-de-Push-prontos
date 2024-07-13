import os

# Caminho do diretório
diretorio = 'Seu Diretorio aqui'

arquivos = [arquivo for arquivo in os.listdir(diretorio) if os.path.isfile(os.path.join(diretorio, arquivo))]

arquivo_bat = os.path.join(diretorio, 'comandos_git.bat')

comandos_git = []

# Função para adicionar comandos git e verificar se há arquivos
def adicionar_comandos_arquivos(extensao, mensagem):
    arquivos_tipo = [arquivo for arquivo in arquivos if arquivo.endswith(extensao)]
    if arquivos_tipo:
        comandos_git.append(f'git add {" ".join([f"\"{arquivo}\"" for arquivo in arquivos_tipo])} && git commit -m "{mensagem}"')
    else:
        print(f'Não existe arquivo {extensao} aqui')

# Arquivos HTML
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
else:
    print("Não existe arquivo HTML aqui")

# Adicionar comandos para outros tipos de arquivos
                             #tipo  #Commit
adicionar_comandos_arquivos('.css', 'Arquivos de CSS do exemplo')
adicionar_comandos_arquivos('.js', 'Arquivos JavaScript do exemplo')
adicionar_comandos_arquivos('.py', 'Arquivos Python do exemplo')
adicionar_comandos_arquivos('.java', 'Arquivos Java do exemplo')
adicionar_comandos_arquivos('.cpp', 'Arquivos C++ do exemplo')
adicionar_comandos_arquivos('.c', 'Arquivos C do exemplo')
adicionar_comandos_arquivos('.php', 'Arquivos PHP do exemplo')
adicionar_comandos_arquivos('.rb', 'Arquivos Ruby do exemplo')
adicionar_comandos_arquivos('.txt', 'Arquivos de texto do exemplo')

# Arquivos de imagem
arquivos_imagem = [arquivo for arquivo in arquivos if any(extensao in arquivo for extensao in ['.png', '.jpg', '.jpeg','.web','.ico'])]
if arquivos_imagem:
    comandos_git.append(f'git add {" ".join([f"\"{arquivo}\"" for arquivo in arquivos_imagem])} && git commit -m "Arquivos de imagem do exemplo"')
else:
    print("Não existe arquivo de imagem aqui")

# Comando para enviar alterações ao repositório remoto
comandos_git.append('git push origin main')

with open(arquivo_bat, 'w', encoding='utf-8') as f:
    f.write('\n'.join(comandos_git))

print(f'Arquivo de script gerado: {arquivo_bat}')

import os

# Absolute path of the directory
directory = 'Here-your-Directory'

files = [file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]

bat_file = os.path.join(directory, 'git_commands.bat')

git_commands = []

html_files = [file for file in files if file.endswith('.html')]
if html_files:
    for html_file in html_files:
        with open(os.path.join(directory, html_file), 'r', encoding='utf-8') as file:
            
            lines = file.readlines()
            for line in lines:
                if '<title>' in line:
                    title = line.strip().replace('<title>', '').replace('</title>', '')
                    break
            else:
                title = 'Untitled'

        git_commands.append(f'git add "{html_file}" && git commit -m "HTML file example: {title}"')

css_files = [file for file in files if file.endswith('.css')]
if css_files:
    git_commands.append(f'git add {" ".join([f"\"{file}\"" for file in css_files])} && git commit -m "CSS files example"')

image_files = [file for file in files if any(extension in file for extension in ['.png', '.jpg', '.jpeg'])]
if image_files:
    git_commands.append(f'git add {" ".join([f"\"{file}\"" for file in image_files])} && git commit -m "Image files example"')

git_commands.append('git push origin main')

with open(bat_file, 'w', encoding='utf-8') as f:
    f.write('\n'.join(git_commands))

print(f'Script file generated: {bat_file}')

import os

# Directory path
directory = 'Your Directory here'

files = [file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]

bat_file = os.path.join(directory, 'git_commands.bat')

git_commands = []

# Function to add git commands and check if there are files
def add_file_commands(extension, message):
    files_of_type = [file for file in files if file.endswith(extension)]
    if files_of_type:
        git_commands.append(f'git add {" ".join([f"\"{file}\"" for file in files_of_type])} && git commit -m "{message}"')
    else:
        print(f'There are no {extension} files here')

# HTML files
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
                title = 'No title'
        git_commands.append(f'git add "{html_file}" && git commit -m "Example HTML file: {title}"')
else:
    print("There are no HTML files here")

# Add commands for other file types
add_file_commands('.css', 'Example CSS files')
add_file_commands('.js', 'Example JavaScript files')
add_file_commands('.py', 'Example Python files')
add_file_commands('.java', 'Example Java files')
add_file_commands('.cpp', 'Example C++ files')
add_file_commands('.c', 'Example C files')
add_file_commands('.php', 'Example PHP files')
add_file_commands('.rb', 'Example Ruby files')
add_file_commands('.txt', 'Example text files')

# Image files
image_files = [file for file in files if any(extension in file for extension in ['.png', '.jpg', '.jpeg', '.webp', '.ico'])]
if image_files:
    git_commands.append(f'git add {" ".join([f"\"{file}\"" for file in image_files])} && git commit -m "Example image files"')
else:
    print("There are no image files here")

# Command to push changes to the remote repository
git_commands.append('git push origin main')

with open(bat_file, 'w', encoding='utf-8') as f:
    f.write('\n'.join(git_commands))

print(f'Script file generated: {bat_file}')

import os
from jinja2 import Template

raw_dir = "raw"

names = []
files = {}

for file in reversed(os.listdir(raw_dir)):
    file_name, extension = os.path.splitext(file)

    if extension == ".md":
        path = os.path.join(raw_dir, file)

        with open(path, "r", encoding='utf-8') as inp_file:
            lines = inp_file.read().splitlines()
            while '' in lines:
                lines.remove('')
            names.append((file_name, lines[0]))
            files[file_name] = lines[1:]

with open('templates\writing.html', 'r', encoding='utf-8') as tmp_file:
    template = Template(tmp_file.read())

    with open("writing.html", "w", encoding="utf-8") as outp_file:
        outp_file.write(template.render(names_list=names, files_dict=files))
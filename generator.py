import os
from collections import namedtuple
from jinja2 import Template


def next_line(raw_dir):
    def inner(file, current_dir=''):
        path = os.path.join(raw_dir, current_dir, file+'.md')
        with open(path, "r", encoding='utf-8') as inp_file:
            inp_file.readline()
            for line in inp_file:
                if line not in ['', '\n']:
                    yield line.strip()

    return inner


def get_writing_titles(dir):
    FoldersNFiles = namedtuple('FoldersNFiles', ['folders', 'files'])
    content = FoldersNFiles(folders={}, files=[])

    for current_dir, folders, files in os.walk(dir):
        titles = []
        prev_dir, folder = os.path.split(current_dir)
        for file in files:
            file_name, extension = os.path.splitext(file)
            if extension == '.md':
                path = os.path.join(current_dir, file)
                with open(path, 'r', encoding='utf-8') as inp_file:
                    titles.append((file_name, inp_file.readline().strip()))
        
        if not prev_dir:
            content.files.extend(titles)
        else:
            content.folders[folder] = titles
    return content
        


def render_template(template_path, outp, params):
    with open(template_path, 'r', encoding='utf-8') as tmp_file:
        template = Template(tmp_file.read())

        with open(outp, 'w', encoding='utf-8') as outp_file:
            outp_file.write(template.render(params))


if __name__ == '__main__':
    content = get_writing_titles('raw')
    render_template('templates/writing.html', 'writing.html',
                    {'content': content, 'next_line': next_line('raw')})
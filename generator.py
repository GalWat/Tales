import os
from jinja2 import Template


def next_line(dir):
    def inner(file):
        path = os.path.join(dir, file+'.md')
        with open(path, "r", encoding='utf-8') as inp_file:
            inp_file.readline()
            for line in inp_file:
                if line not in ['', '\n']:
                    yield line.strip()

    return inner


def get_writing_titles(dir):
    titles = []
    for file in reversed(os.listdir(dir)):
        file_name, extension = os.path.splitext(file)
        if extension != '.md':
            continue

        path = os.path.join(dir, file)
        with open(path, 'r', encoding='utf-8') as inp_file:
            titles.append((file_name, inp_file.readline().strip()))

    return titles


def render_template(template_path, outp, params):
    with open(template_path, 'r', encoding='utf-8') as tmp_file:
        template = Template(tmp_file.read())

        with open(outp, 'w', encoding='utf-8') as outp_file:
            outp_file.write(template.render(params))


if __name__ == '__main__':
    names = get_writing_titles('raw')
    render_template('templates/writing.html', 'writing.html',
                    {'names_list': names, 'next_line': next_line('raw')})
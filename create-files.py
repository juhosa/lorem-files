import lorem
from random import randint


def gen_frontmatter():
    lines = []
    lines.append('---')
    lines.append('title: {}'.format(lorem.get_sentence()))
    cat_count = randint(0, 2)
    cats = []
    for _ in range(cat_count):
        cats.append(lorem.get_word())

    if len(cats) > 0:
        lines.append('categories:')
        for c in cats:
            lines.append('  - {}'.format(c))

    lines.append('---')
    return '\n'.join(lines)


def write_file(content, number):
    DIR = 'files/'
    with open(DIR + 'file_{}.md'.format(number), 'w') as f:
        f.write(content)


def get_content():
    cont = ''
    fm = gen_frontmatter()
    cont += fm

    for _ in range(randint(1, 3)):
        cont += '\n'
        s = lorem.get_paragraph()
        cont += s
        cont += '\n'
        cont += '\n'

    return cont


MAX = 4
for i in range(1, MAX + 1):
    content = get_content()
    # print(content)
    write_file(content, i)

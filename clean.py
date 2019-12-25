from os import listdir
from re import sub


def clean(path):
    file =  open(path, 'r', encoding = 'utf-8-sig')
    content = file.read()
    content = sub('(\n)+', ' ', content)
    content = sub('( )+', ' ', content)
    content = sub('(\s)([.,])+', '\\2', content)
    content = sub('(\s)(-)(\s)', '\\2', content)
    content = sub('(\s)(\))', '\\2', content)
    content = sub('(\()(\s)', '\\1', content)
    content = sub('([\'’])\s', '’', content)
    file.close()
    file = open(path, 'w', encoding = 'utf-8-sig')
    file.write(content)
    file.close()

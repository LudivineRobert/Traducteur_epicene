from nltk.metrics import f_measure
from os import listdir
from re import sub


def main():
    """
    Launched on start, 
    evaluate each file of the ./outputs folder if needed
    """
    files = listdir('./expected_outputs')
    for file in files:
        if 'epicene_' + file in listdir('./outputs'):
            print('evaluating file "{}"'.format(file))
            path1 = './expected_outputs/'+file
            path2 = './outputs/epicene_'+file
            clean(path1)
            clean(path2)
            result = compare_files(path1, path2)
            print("result for file {}:  {}\n".format(file, result))

def compare_files(path1,path2):
    """
    Takes two path of txt files,
    cleans the files, 
    return the f measurement score of the two .txt files
    """
    with open(path1) as expected:
        expected = expected.read()
        expected = expected.lower()
        expected = expected.split(' ')
        expected = set(expected)
    with open(path2) as got:
        got = got.read()
        got = got.lower()
        got = got.split(' ')
        got = set(got)
    return f_measure(expected, got)

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
    #print(content)
    #breakpoint()
    file.close()
    file = open(path, 'w', encoding = 'utf-8-sig')
    file.write(content)
    file.close()

if __name__ == '__main__':
   main()

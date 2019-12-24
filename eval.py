from nltk.metrics import f_measure
from os import listdir
from re import sub


def main():
    files = listdir('./expected_outputs')
    for file in files:
        if 'epicene_' + file  in listdir('./outputs'):
            print('evaluating file "{}"'.format(file))
            path1 = './outputs/epicene_'+file
            path2 = './expected_outputs/'+file
            result = compare_files(path1, path2)
            
            print("result for file {}:  {}\n".format(file, result))


def compare_files(path1,path2):
    with open(path1) as expected:
        expected = expected.read()
        expected = sub('(\n)+', ' ', expected)
        expected = sub('( )+', ' ', expected)
        expected = expected.split(' ')
        expected = set(expected)
    with open(path2) as got:
        got = got.read()
        got = sub('(\n)+', ' ', got)
        got = sub('( )+', ' ', got)
        got = got.split(' ')
        got = set(got)
    return f_measure(expected, got)

if __name__ == '__main__':
    main()
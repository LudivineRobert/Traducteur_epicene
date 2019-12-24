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
<<<<<<< HEAD:eval.py
            path1 = './expected_outputs/'+file
            path2 = './outputs/epicene_'+file
=======
            path1 = './outputs/epicene_' + file
            path2 = './expected_outputs/' + file
>>>>>>> b109cc0c9f5faf1876571ea97f179d5b6c6659ca:evaluation.py
            result = compare_files(path1, path2)

            print("result for file {}:  {}\n".format(file, result))


<<<<<<< HEAD:eval.py
def compare_files(path1,path2):
    """
    Takes two path of txt files,
    cleans the files, 
    return the f measurement score of the two .txt files
    """
=======
def compare_files(path1, path2):
>>>>>>> b109cc0c9f5faf1876571ea97f179d5b6c6659ca:evaluation.py
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

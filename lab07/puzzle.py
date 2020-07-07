import os
from itertools import combinations

import numpy as np


def readMat(path):
    f = open(path, 'rt')
    h, w = [int(x) for x in f.readline().strip().split('\t')]
    assert h > 0 and w > 0
    mat = - np.ones((h, w), dtype=np.int32)
    for ih in range(h):
        iw = 0
        for it in f.readline().strip().split('\t'):
            if it != '.':
                mat[ih][iw] = int(it)
            iw += 1
    f.close()
    return mat


def toCNF(mat, lvars):
    cnfs = []
    for x in range(0, mat.shape[0]):
        for y in range(0, mat.shape[1]):
            if mat[x][y] != -1:
                for it in generatePredicates((x, y), mat[x][y], lvars):
                    cnfs.append(it)
    return cnfs


def generatePredicates(current_coordinate, current_value, lvars):
    predicates = []
    around = generateAround(lvars, current_coordinate)
    minusAround = [-it for it in around]

    if current_value != 0:
        # all possibilities
        predicates.append(around)

        # constraints to eliminate values > current_value
        uppers = combinations(minusAround, current_value + 1)
        for combination in uppers:
            predicates.append(combination)

        # constraints to eliminate values < current_value
        for j in range(0, current_value):
            lower = combinations(minusAround, j)
            for val in lower:
                temp = [j for j in val]
                for i in range(0, len(around)):
                    if -around[i] not in temp:
                        temp.append(around[i])
                predicates.append(temp)
    else:
        for red in minusAround:
            predicates.append([red])

    return predicates


def generateAround(lvars, current_coordinate):
    temp = []
    (x, y) = current_coordinate
    dx = [-1, 0, 1]
    dy = [-1, 0, 1]

    for i in dx:
        for j in dy:
            if 0 <= x + i < lvars.shape[0] and 0 <= y + j < lvars.shape[0]:
                temp.append(lvars[x + i][y + j])
    return temp


def runMiniSAT(infile, outfile):
    os.system('./MiniSat_v1.14_linux %s %s' % (infile, outfile))


def fortmatFilledCell(text, cl_code):
    return '\033[1;37;%dm%s\033[1;0;0m' % (cl_code, text)


if __name__ == '__main__':
    infile = "maze.txt"
    outfile = "output.txt"
    mat = readMat(infile)

    lvars = np.arange(1, mat.shape[0] * mat.shape[1] + 1, 1)
    lvars = np.reshape(lvars, (mat.shape[0], mat.shape[1]))

    # END_TODO
    num = mat.shape[0] * mat.shape[1]

    # TODO
    clauses = toCNF(mat, lvars)
    # END_TODO
    with open('inSAT.txt', 'wt') as f:
        f.write('p cnf %d %d\n' % (num, len(clauses)))
        for it in clauses:
            for i in it:
                f.write('%d ' % (i))
            f.write('0\n')
    runMiniSAT('inSAT.txt', 'outSAT.txt')

    res = []
    with open('outSAT.txt') as f:
        if f.readline().strip() != 'SAT':
            print('UNSAT')
            exit()
        tmp = f.readline().strip().split(' ')
        for it in tmp:
            res.append(int(it))

    # print res
    vis_str = ''
    with open(outfile, 'wt') as g:
        for ih in range(mat.shape[0]):
            for iw in range(mat.shape[1]):
                txt = ''
                if mat[ih][iw] >= 0:
                    g.write('%d' % (mat[ih][iw]))
                    txt += '%-2d' % (mat[ih, iw])
                else:
                    g.write(' ')
                    txt += '  '

                if lvars[ih][iw] in res:
                    g.write('.')
                    vis_str += fortmatFilledCell(txt, 42)
                else:
                    g.write(' ')
                    vis_str += fortmatFilledCell(txt, 41)
            g.write('\n')
            vis_str += '\n'

    print('\n=======INPUT=======')

    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            if mat[i][j] < 0:
                print('_', end='')
            else:
                print(mat[i][j], end='')
        print('')
    print('===================')
    print('\n=======ANSWER=======')
    print(vis_str, '=====================')
# os.system('cat %s'%(outfile))

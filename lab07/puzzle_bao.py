import numpy as np
import itertools
import os
import sys
from itertools import combinations


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


def checkAround(x,y,lvars,mat):
	temp = []
	temp. append(lvars[x][y])
	if(x-1>-1 and y+1<mat.shape[1]):
		temp.append((lvars[x-1][y+1]))
	if (y + 1 < mat.shape[1]):
		temp.append((lvars[x][y + 1]))
	if (x + 1 < mat.shape[0] and y + 1 < mat.shape[1]):
		temp.append((lvars[x + 1][y + 1]))
	if (x - 1 > -1 ):
		temp.append((lvars[x - 1][y]))
	if (x + 1 < mat.shape[0]):
		temp.append((lvars[x + 1][y]))
	if (x - 1 > -1 and y - 1 > -1):
		temp.append((lvars[x - 1][y - 1]))
	if ( y - 1 > -1):
		temp.append((lvars[x][y - 1]))
	if (x + 1 < mat.shape[0] and y -1  > -1):
		temp.append((lvars[x + 1][y - 1]))
	return temp

def toCNF(mat):
	lvars1 = np.arange(1, mat.shape[0] * mat.shape[1] + 1, 1)
	lvars1 = np.reshape(lvars1, (mat.shape[0], mat.shape[1]))
	result = list()
	result2 = list()
	deni = []
	for i in range (0, mat.shape[0]):
		for	j in range (0, mat.shape[1]):
			a = mat[i][j]
			temp = []
			com =[]
			com2 =[]
			temp2 =[]
			if a == len(checkAround(i,j,lvars1,mat)):
				for green in checkAround(i,j,lvars1,mat):
					result.append([green])
			else:
				if(mat[i][j] == 0):
					temp = []
					for red in checkAround(i,j,lvars1,mat):
						result.append([-red])
				else:
					#check chang tren
					for t in checkAround(i,j,lvars1, mat):
						temp.append(-t)
					a1 = a+1
					for t in combinations(temp, a1):
						com.append(list(t))
					for t in com:
						if len(t) >0:
							result.append(t)
					#check chang duoi
					around = checkAround(i, j, lvars1, mat)
					for o in range(0, a):
						tempLower = []
						lower = combinations(around, o)
						for p in lower:
							for h in p:
								tempLower.append(-h)
						for t in around:
							if -t not in list(tempLower):
								tempLower.append(t)
						result.append(tempLower)
	print(result)
	return result



def runMiniSAT(infile, outfile):
	os.system('./MiniSat_v1.14_linux %s %s'%(infile, outfile))

def fortmatFilledCell(text, cl_code):
	return '\033[1;37;%dm%s\033[1;0;0m'%(cl_code, text)

if __name__ == '__main__':
	infile = "tiny_maze1.txt"
	outfile = "output.txt"
	mat = readMat(infile)

	lvars = np.arange(1, mat.shape[0] * mat.shape[1] +1, 1)
	lvars = np.reshape(lvars, (mat.shape[0], mat.shape[1]))
	print(lvars[2][2])
	print(checkAround(2,2,lvars,mat))
	# TODO
	clauses = toCNF(mat)
	#toCNF(mat)
	# END_TODO
	num = mat.shape[0] * mat.shape[1]
	print(mat)
	print(lvars)


	runMiniSAT('inSAT.txt', 'outSAT.txt')

	res = []
	with open('outSAT.txt') as f:
		if f.readline().strip() != 'SAT':
			print ('UNSAT')
			exit()
		tmp = f.readline().strip().split(' ')
		for it in tmp:
			res.append(int(it))

	#print res
	vis_str = ''
	with open(outfile, 'wt') as g:
		for ih in range(mat.shape[0]):
			for iw in range(mat.shape[1]):
				txt = ''
				if mat[ih][iw] >= 0:
					g.write('%d'%(mat[ih][iw]))
					txt += '%-2d'%(mat[ih, iw])
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

	print ('\n=======INPUT=======')

	for i in range(mat.shape[0]):
		for j in range(mat.shape[1]):
			if mat[i][j] < 0:
				print ('_', end='')
			else:
				print (mat[i][j], end='')
		print ('')
	print ('===================')
	print ('\n=======ANSWER=======')
	print (vis_str,'=====================')
	#os.system('cat %s'%(outfile))
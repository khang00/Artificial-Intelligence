import numpy as np
from itertools import combinations
import os
import sys

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

def getAllAround(num):
	arounds = [num]
	if num-11>0:
		arounds.append(num-11)
	if num-10>0 :
		arounds.append(num-10)
	if num - 9 > 0:
		arounds.append(num - 9)
	if num - 1 > 0:
		arounds.append(num-1)
	if num + 1 < 101:
		arounds.append(num+1)
	if num + 9 < 101:
		arounds.append(num +9)
	if num + 10 < 101:
		arounds.append(num + 10)
	if num + 11 < 101:
		arounds.append(num + 11)
	return arounds


def toCNF(mat,lvars):
	result = []
	for x in range(len(mat)):
		for y in range(len(mat[x])):
			if mat[x][y] != -1:
				#lấy tất cả các ô xung quanh quăng vào 1 cái list
				arounds = getAllAround(lvars[x][y])
				groupsOf = mat[x][y]

				#met de binh thuong
				for a in combinations(arounds,groupsOf):
					result.append(list(a))

				#chuyen dau arounds
				arounds = [-it for it in arounds]
				for a in combinations(arounds,len(arounds)-groupsOf):
					result.append(list(a))
	return result


				
def runMiniSAT(infile, outfile):
	os.system('./MiniSat_v1.14_linux %s %s'%(infile, outfile))

def fortmatFilledCell(text, cl_code):
	return '\033[1;37;%dm%s\033[1;0;0m'%(cl_code, text)

if __name__ == '__main__':
	infile = "maze1.txt"
	outfile = "output.txt"
	mat = readMat(infile)
	lvars = np.arange(1, 101, 1)
	lvars = np.reshape(lvars, (10, 10))
	# list chua list 
	# list nay chua cac so nguyen
	# TODO
	clauses = toCNF(mat,lvars)
	# END_TODO
	num = mat.shape[0]*mat.shape[1]


	#print(lvars)
	with open('inSAT.txt', 'wt') as f:
		f.write('p cnf %d %d\n'%(num, len(clauses)))
		for it in clauses:
			for i in it:
				f.write('%d '%(i))
			f.write('0\n')
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
	#print(mat[1])
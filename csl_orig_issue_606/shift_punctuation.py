# coding=utf-8
"""Shift the punctuation marks outside Sanskrit tag `{##}`.
    Usage - python3 shift_punctuation.py inputfile outputfile
    Version - 0.0.1
    Author - drdhaval2785@gmail.com
"""
from __future__ import print_function
import sys
import re
import codecs
import os
from collections import Counter


def find_punctuations(filein, reg):
	fin = codecs.open(filein, 'r', 'utf-8')
	count = Counter()
	intermediates = []
	for lin in fin:
		m = re.search(reg, lin)
		if m:
			intermediates.append(m.group(2))
	print(len(intermediates))
	fin.close()
	print(Counter(intermediates).most_common())


def correct_punctuations(filein, fileout):
	fin = codecs.open(filein, 'r', 'utf-8')
	fout = codecs.open(fileout, 'w', 'utf-8')
	reg1 = "({#[^#]*)(,)([^#]*#})"
	for lin in fin:
		lin = re.sub("({#[^#]*)([,][ ]*)([^#]*#})", "\g<1>#}\g<2>{#\g<3>", lin)
		fout.write(lin)
	fin.close()
	fout.close()
	

if __name__ == "__main__":
	dic = sys.argv[1]
	filein = os.path.join('..', '..', '..', 'cologne', 'csl-orig', 'v02', dic, dic + '.txt')
	reg = "({#[^#]*)([^a-zA-Z0-9 ]+)([^#]*#})"
	fileout = dic + '_corrected.txt'
	# find_punctuations(filein, reg)
	correct_punctuations(filein, fileout)
	

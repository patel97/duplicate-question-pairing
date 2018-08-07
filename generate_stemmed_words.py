# -*- coding: utf-8 -*-
from nltk.stem.porter import PorterStemmer
import json
import re
import sys
ps = PorterStemmer()
#path_to_vectors = '/home/rudresh/Desktop/quora/numberbatch-en.txt'
path_to_vectors = sys.argv[1]
import numpy as np

def dump_stemmed(filepath):
	vectors = []
	with open(filepath,'r') as myfile:
		vectors = myfile.readlines()
		vector = [vector.strip() for vector in vectors]
		# print(vectors)
	word_vector_dict = {}

	for word_vector in vectors[1:]:
		word = word_vector.split()[0]	
		vector = word_vector.split()[1:]
		# print(vector)
		if '#' not in word:
			word=ps.stem(word)
			print(word)
			if word in word_vector_dict:
				pass
			else:
				word_vector_dict[word]=vector
				
	with open('stemmed_vectors','w') as myfile:
		json.dump(word_vector_dict,myfile)


dump_stemmed(path_to_vectors)
# filename = 'stemmed_vectors'
# generate_in_correct_format(filename)
# clean_vectors()
# generate_word_list('final_clean_vectors')
# create_vector_matrix()
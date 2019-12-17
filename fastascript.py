#!/usr/bin/env python3 
import argparse
import FileIO
import Random
import OS
import numpy as np
import random
#importing libraries
#parser = argparse.ArgumentParser(description = "insert header")
#parser.add_argument("-header",required)
#args = pareser.parse_args()
#this function makes a repeat sequence

nuc_list = ["A","T","C",G"]
#a function that makes a ramdom length of letters and repeats the letters with random.choice
def repeat_seq(length):
    your_letters='ATCG'
    return ''.join((random.choice(your_letters) for i in range(length)))
#returns a sequence of letters in random formation(creating repeats)
 
#new_fasta is the name of our fasta function
repeat_seq1= repeat_seq(30)
repeat_seq2= repeat_seq(30)
repeat_seq3= repeat_seq(30)
repeat_seq4= repeat_seq(30)
repeat_seq5= repeat_seq(30)
#the try bock in trying all of the code(sequence)that is in there
def new_fasta():
	try:
		with open("psuedo_protein.fasta",w) as in_handle:
			in_handle.write(repeat_seq1,repeat_seq2,repeat_seq3,repeat_seq4,repeat_seq5)
#opens file and writes the repeat sequences to the file

#	except as IOError:
	#this is the exception error that will help the code
#		print("IOError")


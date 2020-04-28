#!/usr/bin/env python3

import re

#set variable equal to kmer 
sixmer = "TGGCGA"

#create a dictionary that contains split strings and kmer variable
#open file with sequence to read it , set handle
with open ("og_seq.fasta", "r") as in_handle:
	#interpret handle and set interpretation to variable
	sequence = in_handle.read()


#turn variable holding read file into a collection of strings
seq = str(sequence)

#break string at desired kmer, creating a list and save as variable
seq_list = sequence.split(sixmer)


print(seq_list)

#take last item in list of split strings, out of list
seq_list.remove(seq_list[0])

#print list of split strings
#print list of split strings (sans first item)
print(seq_list)

#create function that takes in two parameters
def prepend(list, str):


#sort list of split strings without the first item
	str += "{0}"

#store an item from the list in a string that as changing each iteration
	list = [str.format(i) for i in list]
#call function with parameters list of split strings and kmer variable
	return (list)
#assign output from function to variable 
repeat_list = prepend(seq_list, sixmer)

#iterate through function output
for item in repeat_list:
#print itteration of function output
	print(item)
	
#create a dictionary that contains split strings and kmer variable
#sort list of split strings without the first item
#retreive list from function
#gaining access to regular expression module
#the two parameters take in two different collections




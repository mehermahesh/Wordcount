 # read a .txt file from a folder
# Count the number of times each word appears in the file
# Create a file called output.txt and write each word and its count in this file.

import sys
import argparse
import os




# Removing all punctuations and making sure, everything in lower case
def remove_punctuation(line):
				punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~1234567890\n'''
				new_line = ""
				for char in line:
								if char not in punctuations:
												new_line = new_line + char
												new_line = new_line.lower()
				print("{}\n".format(new_line))
				return (new_line)




# counting the repeated words and storing them into a dictionary
def words_count(words):


				#print(words)
				dict = {}
				for word in words:
								if word not in dict:
												dict[word] = 1
								else:
												dict[word] +=1
				print("{}\n".format(dict))
				return dict



if __name__=="__main__":
				# adding up and creating the optional arguments
				parser = argparse.ArgumentParser(description="word frequency in a text file")
				parser.add_argument('-i', '--input', type=str, required=True, help='input')
				parser.add_argument('-o', '--output', type=str, required=True, help='output')
				args = parser.parse_args()


				#to make sure whether its a folder path or file path
				if os.path.isfile(args.input):
								f = open(args.input,"r")
				else:
								print(os.listdir(args.input))
								txt_file= str(input("which text file you'd like to process:"))
								input_file=os.path.join(args.input,txt_file)
								f = open(input_file,"r")



				line = f.read()
				print("{}".format(line))
				words = remove_punctuation(line).split(' ')


				f1 = open(args.output, "w")
				f1.write("word---wordcount\n")
				for key,value in words_count(words).items():
								f1.write("{}----{}\n".format(key,value))
				f.close()
				f1.close()








